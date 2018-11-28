#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;
typedef vector<int> VI;

int main(){
    int nt, ce, i, j, a, b, x;
    cin >> nt;
    for(i=1; i<=nt; ++i){
        printf("Case #%d: ", i);
        VI vet(16,0);
        for(j=0; j<2; ++j){
            cin >> ce;
            ce--;
            for(a=0; a<4; ++a){
                for(b=0; b<4; ++b){
                    cin >> x;
                    x--;
                    if(a!=ce) vet[x]=1;
                }    
            }
        }
        int res=-1;
        for(j=0; j<16; ++j){
            if(vet[j]==0 && res==-1) res=j+1;
            else if(vet[j]==0 && res>0) res=-2;
        }
        if(res==-2) printf("Bad magician!\n");
        else if(res==-1) printf("Volunteer cheated!\n");
        else printf("%d\n", res);
    }
    return 0;    
}
