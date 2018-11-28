#include<bits/stdc++.h>
using namespace std;

#define ll long long

ll st[100];

int main()
{

    freopen("my.txt","r",stdin);
    freopen("ou.txt","w",stdout);

    ll a,b,T,c=0,n,i,k;
    cin>>T;
    for(b=1;b<=T;b++){
    cin>>a;
    c=0;
    memset(st,0,sizeof(st));
    if(a==0){
        printf("Case #%lld: ",b);
        cout<<"INSOMNIA"<<endl;
    }
    else
    for(i=1; ;i++)
    {
        n=a*i;
        while(n){
            k=n%10;
            n/=10;
            if(st[k]==0){
                st[k]++;
                c++;
            }

        }
        if(st[0]==1 && c==10){
                 printf("Case #%lld: ",b);
            cout<<a*i<<endl;
            break;
        }

    }
    }
    return 0;
}
