#include <cstdio>

int main (){
    int t, c=1;
    int n, m;
    FILE *output = fopen("Boutput.txt", "w");
    char grid[100][100];
    bool flag[100][100];
    scanf("%d", &t);
    while(c<=t){
        scanf ("%d %d", &n, &m);
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                scanf("%d", &grid[i][j]);
                if(grid[i][j]==2)flag[i][j]=true;
                else flag[i][j]=false;
            }
        }
        bool answer = true;
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(grid[i][j]==1 && flag[i][j]==false){
                    bool flag2=true;
                    for(int z=0; z<m; z++){
                        if(grid[i][z]==2){
                            flag2=false;
                            break;
                        }
                    }
                    if(flag2==true){
                        for(int z=0; z<m; z++){
                            flag[i][z]=true;
                        }
                    }
                    else{
                        bool flag3=true;
                        for(int z=0; z<n; z++){
                            if(grid[z][j]==2){
                                flag3=false;
                                break;
                            }
                        }
                        if(flag3==true){
                            for(int z=0; z<n; z++){
                                flag[z][j]=true;
                            }
                        }
                        else{
                            answer = false;
                            break;
                        }
                    }
                }
            }
            if(answer==false)
                break;
        }
        if(answer==false)
            fprintf(output, "Case #%d: NO\n", c);
        else fprintf(output, "Case #%d: YES\n", c);
        c++;
    }
    fclose(output);
    return 0;
}
