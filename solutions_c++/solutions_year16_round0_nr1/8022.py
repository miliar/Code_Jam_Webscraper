#include <iostream>
#define LOOP(a,b,c) for(int c=a;c<b;c++)
#include <algorithm>
#include <map>
#include <cstdio>
using namespace std;

map<long,long> t;
map<int,int> d;

long long N;

int ans(long long m){
    long long n=N*m;
    if (t[n]==1) return -1;
    int p=n;
    while(n!=0){
        int k=n%10;
        n=n/10;
        d[k]=1;
    }
    t[p]=1;
    bool f=true;
    LOOP(0,10,i) if(d[i]!=1) f=false;
    if (f) return p;
    else return ans(m+1);
}

int main(){
    freopen("A-large.in","rb",stdin);
    freopen("A-large.out","wb",stdout);
    int T;
    cin>>T;
    int i=1;
    while(T--){
        t.clear();
        d.clear();
        cin>>N;
        int an=ans(1);
        cout<<"Case #"<<i<<": ";
        if(an==-1) cout<<"INSOMNIA"<<endl;
        else cout<<an<<endl;
        i++;
    }

}
