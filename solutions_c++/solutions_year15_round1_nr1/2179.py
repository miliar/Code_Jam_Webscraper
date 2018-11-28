#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define F first
#define S second
using namespace std;
int T,n;
double m[10010];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    for(int t=1;t<=T;++t){
        cin>>n;
        long long x=0;
        double y=0;
        double r=0;
        for(int i=0;i<n;++i)
            cin>>m[i];
        for(int i=1;i<n;++i){
            x+=max(m[i-1]-m[i],0.0);
            r=max(r,(max(m[i-1]-m[i],0.0)*1.0)/10.0);
//            cout<<r<<endl;
        }
//        cout<<r<<endl;
        for(int i=0;i<n-1;++i){
            y+=min(r*10,m[i]);
        }
        cout<<"Case #"<<t<<": "<<x<<" "<<(long long)ceil(y)<<endl;
    }
}
