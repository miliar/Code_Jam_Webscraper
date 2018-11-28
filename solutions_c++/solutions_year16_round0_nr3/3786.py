#include <iostream>
#include <algorithm>
#include <ctime>
#include <cstdio>
#include <vector>
#include <set>
using namespace std;
int n,J;
set<vector<int> > S;
int not_prime(long long x)
{
    for(long long i=2;i*i<=x;i++){
        if(x%i==0) return i;
    }
    return -1;
}
vector<int> G,fac;
void gen()
{
    G.clear();
    for(int i=0;i<n;i++){
        int x=rand()%2;
        if(i==0||i==n-1) x=1;
        G.push_back(x);
    }
}
int getbase(int x)
{
    long long now=0;
    for(int i=0;i<G.size();i++){
        now*=x;
        if(G[i]){
            now+=1;
        }
    }
    fac.push_back(not_prime(now));
}
int check()
{
    fac.clear();
    for(int i=2;i<=10;i++){
        getbase(i);
    }
    for(int i=0;i<fac.size();i++){
        if(fac[i]==-1)
            return 0;
    }
    return 1;
}
int main()
{
    freopen("data.out","w",stdout);
    srand(time(NULL));
    int T;
    cin>>T;
    cin>>n>>J;
    cout<<"Case #1:"<<endl;
    for(int i=0;i<J;){
        gen();
        if(S.find(G)!=S.end()) continue;
        S.insert(G);
        if(check()){
            for(int i=0;i<G.size();i++){
                cout<<G[i];
            }
            for(int i=0;i<fac.size();i++){
                cout<<" "<<fac[i];
            }
            cout<<endl;
            i++;
        }
    }

    return 0;
}
