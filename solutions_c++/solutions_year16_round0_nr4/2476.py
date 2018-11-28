#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define ll unsigned long long
#define mp make_pair
#define pii pair<int,int>
using namespace std;
int main()
{
    freopen("D.in","r",stdin);
    freopen("out.txt","w",stdout);
    int tc;
    cin>>tc;
        for(int t=1;t<=tc;t++){
        printf("Case #%d:",t);
        int K,C,S;
        cin>>K>>C>>S;
        if(C==1){
            if(S<K)
            cout<<" IMPOSSIBLE"<<endl;
            else {
                for(int i=1;i<=S;i++)cout<<" "<<i;
                cout<<endl;
            }
            continue;
        }
        else if(K/2+K%2>S){
            cout<<" IMPOSSIBLE"<<endl;
            continue;
        }
        ll X=1;int i;
        for(i = 1;i<C;i++)
            X*=K;// X= K^C
            ll tmp = 2;
        for(i = 1 ; i<=  K/2 ;i++){
            cout<<" "<<tmp;
            tmp = 2*(i*(X+1)+1);
        }

        if(K%2==1)
            cout<<" "<<2*(i-1)*X+1;
        cout<<endl;
        }


}
