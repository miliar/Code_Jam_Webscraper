#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
    ll t,T;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    for(t=1;t<=T;t++)
    {
        ll n,m,i,j,a,b;
        string s;
        char arr[1005],ch;
        cin>>n;
        getchar();
        for(i=0;i<=n;i++)
        {
            scanf("%c",&ch);
            arr[i]=ch;
        }
        getchar();
        a=0;
        b=0;
        for(i=0;i<=n;i++)
        {
            if(a<i){
                b+=(i-a);
                a++;
            }
            //cout<<arr[i]<<endl;
            a+=(arr[i]-'0');
            //cout<<"ok\n";
        }
        printf("Case #%lld: %lld\n",t,b);
    }
    return 0;
}
