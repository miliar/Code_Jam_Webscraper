#include <cstdio>
#include <iostream>

int main(){

    int i = 2;
    int j = 3;
    int k = 4;

    int dijkstra[5][5];
    dijkstra[1][1] = 1;
    dijkstra[1][2] = i;
    dijkstra[1][3] = j;
    dijkstra[1][4] = k;
    dijkstra[2][1] = i;
    dijkstra[2][2] = -1;
    dijkstra[2][3] = k;
    dijkstra[2][4] = -j;
    dijkstra[3][1] = j;
    dijkstra[3][2] = -k;
    dijkstra[3][3] = -1;
    dijkstra[3][4] = i;
    dijkstra[4][1] = k;
    dijkstra[4][2] = j;
    dijkstra[4][3] = -i;
    dijkstra[4][4] = -1;

    int t,l = 0,x = 0;

    scanf("%d",&t);

    int result = 0;

    bool booli, boolj, boolk;



    for(int i = 0; i < t; i++){
        scanf("%d %d", &l, &x);
        char line[l+1];
        std::cin.getline(line,0);
        std::cin.getline(line,l+1);

        booli = false;
        boolj = false;
        boolk = false;

        result = 0;

        if(l*x > 2){
        for(int j = 0; j < x; j++){
            for(int m = 0; m < l; m++){

                if(result == 0 && !booli && line[m]-103 == 2){
                    result = line[m]-103;
                }else if(result == 0 && !boolj && line[m]-103 == 3){
                    result = line[m]-103;
                }else if(result == 0 && (m+1) < l){
                    result = dijkstra[line[m]-103][line[m+1]-103];
                    m++;
                } else if(result == 0){
                    result = line[m]-103;
                }else{
                    if(result < 0) {
                        result = result*(-1);
                        result = dijkstra[result][line[m]-103];
                        result = result*(-1);
                    } else result = dijkstra[result][line[m]-103];
                }

                if(booli == false && result == 2){
                    booli = true;
                    result = 0;
                } else if(booli && boolj == false && result == 3){
                    boolj = true;
                    result = 0;
                }
            }
        }
        }

        if(booli && boolj && boolk == false && result == 4){
            boolk = true;
            result = 0;
        }

        if(boolk) printf("Case #%d: %s\n",i+1,"YES");
        else printf("Case #%d: %s\n",i+1,"NO");

    }


}
