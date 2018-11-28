#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define ll unsigned long long
#define mp make_pair
#define pii pair<int,int>
vector<bool> a(10,0);int all;
void init(){
    a= vector<bool>(10,0);
    all = 10;
}
bool marked(ll N){

    while(N && all>0){
        if(a[N%10]==0){
            a[N%10]=1;
            all--;
        }
        N/=10;
    }
    if(all)
        return 0;
    return 1;
}
int main()
{
    freopen("A.in","r",stdin);
    freopen("out.txt","w",stdout);
    int tc;cin>>tc;
    for(int t=1;t<=tc;t++){
        printf("Case #%d: ",t);
        ll n;
        init();
        cin>>n;
        cerr<<t<<endl;
        if(n==0)cout<<"INSOMNIA"<<endl;
        else {
                ll i=1;ll N=n;
            while(N*i<(ll)1<<60){
                N=n*i;
                if(marked(N)){
                cout<<N <<endl;
                    break;
                }
                i++;
            }
        }
    }
}
