#include<bits/stdc++.h>

using namespace std;

int T;
int Smax;
char st[1005];
int sum;
int need;


int main(){

    //cin>>T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++){

        //cin>>Smax;
        scanf("%d",&Smax);
        //cin>>st;
        scanf("%s",st);
        sum=(int)(st[0]-48);     need=0;

        for (int j=1;j<=Smax;j++){


            if(sum>=j)
                sum+=(int)(st[j]-48);
            else{
                need+=j-sum;
                sum=(int)(st[j]-48)+j;
            }
        }
        printf("Case #%d: %d\n",i,need);
    }

    return 0;
}
