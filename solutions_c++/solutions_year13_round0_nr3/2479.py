#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;
#define MX 10000000
int cse;
long long a,b;

bool pal(long long x){
    if(x==0) return false;

    vector<int> vi;
    //vector<int> vi2;
    while(x!=0){
        vi.push_back(x%10);
        x=x/10;
    }
    for(int i=0;i<vi.size()/2;i++){
        if(vi[i]!=vi[vi.size()-1-i]) return false;
    }
    return true;


}


int main(){
    freopen("c.txt","rt",stdin);
    freopen("c.out","wt",stdout);


    vector<long long> alls;
    for(int i=1;i<=MX;i++){
        long long a=i;
        if(!pal(a)) continue;
        long long b= a*a;
        if(!pal(b)) continue;
        alls.push_back(b);
    }
    //cout<<alls.size()<<endl;
    //cout<<alls[0]<<endl;
    //cout<<alls[38]<<endl;


    cin>>cse;
   for(int run=1;run<=cse;run++){
        cin>>a>>b;
        int ret=0;

        for(int i=0;i<alls.size();i++) if(alls[i]>=a && alls[i]<=b) ret++;

        cout<<"Case #"<<run<<": "<<ret<<endl;

    }
    return 0;
}
