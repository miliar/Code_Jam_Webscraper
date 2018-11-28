#include <cstdio>
#include <iostream>
using namespace std;
int main(){
    int t;
    scanf("%d",&t);
    int m[4][4];
    for(int count =1; count <=t; count++){
        int k, temp;
        scanf("%d",&k);
        int pos[4];
        for(int i=0; i < 16; i++){
            scanf("%d",&temp);
            if((i/4)+1==k){
                pos[i%4]=temp;
            }
        }
        int p=0;
        int last = -1;
        scanf("%d",&k);
        for(int i=0; i < 16; i++){
            scanf("%d",&temp);
            if((i/4)+1==k){
                for(int j=0; j<4;j++){
                    if(pos[j]==temp){
                        p++;
                        last = temp;
                    }
                }
            }
        }
        printf("Case #%d: ", count);
        if(p==0) printf("Volunteer cheated!\n");
        if(p==1) printf("%d\n",last);
        if(p>1) printf("Bad magician!\n");
    }
    return 0;
}
