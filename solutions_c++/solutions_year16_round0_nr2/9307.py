#include <bits/stdc++.h>

using namespace std;

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("out", "w", stdout);
    
    int T;
    int minMoves, counter = 0;
    bool firstFace = false;
    bool downFirstFace = false; // checks if any face down before the first head is found
    scanf("%d", &T);
    for(int t = 1; t <= T; t++){
        char pc[101];
        scanf("%s", &pc);
        int i = 0;
        while( pc[i] != '\0'){
            counter = 0;
            while(pc[i] == '-'){
                pc[i] = '+';
                counter++;
                i++;
            }
            if(!firstFace){
                firstFace = true;
                if(counter > 0){
                    minMoves = 1;
                }
            }else if( counter >0 && firstFace){
                minMoves += 2;
            }
            i++;
        }
        printf("Case #%d: %d\n", t, minMoves);
        minMoves = 0;
        firstFace = false;
    }
    return 0;
}