#include<bits/stdc++.h>
#define ll long long
using namespace std;

bool digchk[12];

ll num,ansnum,na;
int ans,t;

void markdigit(ll dig){
    while(dig){
        digchk[dig%10]=1;
        dig/=10;
    }
}

bool chkvalid(ll val){
    int cnt = 0;
    for(int i = 0 ; i  <10;i++){
        if(digchk[i])cnt++;
    }

    if(cnt==10){
        ansnum=val;
        return 1;
    }
    return 0;
}
int main(){
    freopen("aa.in","r",stdin);
    freopen("A.txt","w",stdout);


    scanf("%d",&t);

    for(int ca=1;ca<=t;ca++){
        scanf("%lld",&num);

        printf("Case #%d: ",ca);
        if(num==0){
            printf("INSOMNIA\n");
            continue;
        }
        na = num;

        memset(digchk,0,sizeof(digchk));

        markdigit(num);
        ans = 0;
        while(!chkvalid(num)&& ans<1000000) {
            ans++;

            num+=na;
           // cout<<"num:"<<num<<endl;
            markdigit(num);
        }
        if(ans>=1000000){
             printf("INSOMNIA\n");
            continue;
        }

        printf("%lld\n",ansnum);
    }

    return 0;
}
