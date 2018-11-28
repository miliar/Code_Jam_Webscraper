#include<iostream>
using namespace std;

int T;
long long r,t;

int main(){
    int i,j,k;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for(int cs=1;cs<=T;++cs){
        cin>>r>>t;
        long long lo = 1;
        long long r1 = r;
        long long hi = t/r1+100;
        if(hi>807106780) hi = 807106780;
        while(lo+1<hi){
            long long mid = (lo+hi)/2;
            long long t1 = mid*(2*mid+2*r-1);
            if(t1<=t) lo = mid;
            else hi=mid;
        }
        cout<<"Case #"<<cs<<": ";
        cout<<lo<<endl;
        cerr<<"Case #"<<cs<<": ";
        cerr<<lo<<endl;
        
    }
    return 0;
}

