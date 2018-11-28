#include <cstdio>

int main(){
    int T;
    scanf("%d",&T);
    for(int ix=0;ix<T;ix++){
        printf("Case #%d: ",ix+1);
        bool iss[16];
        int a1,a2;
        scanf("%d",&a1);
        a1--;
        int in;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                scanf("%d",&in);
                if(i==a1) iss[in-1]=true;
                else iss[in-1]=false;
            }
        }
        scanf("%d",&a2);
        a2--;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                scanf("%d",&in);
                if(i!=a2) iss[in-1]=false;
            }
        }
        int cnt=0,at;
        for(int i=0;i<16;i++){
            if(iss[i]){
                cnt++;
                at=i;
            }
        }
        if(cnt==0) printf("Volunteer cheated!");
        else if(cnt>1) printf("Bad magician!");
        else printf("%d",at+1);
        printf("\n");
    }
}
