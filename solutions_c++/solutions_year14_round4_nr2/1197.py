#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<map>
#include<set>
#include<cmath>

using namespace std;

#define mp make_pair
#define pb push_back
#define forn(i,n) for(int i=0;i<(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define all(v) v.begin(),v.end()

int n;

bool check(vector<int> &v)
{
    bool sube=true;
    forn(i,n-1)
    {
        if(v[i]>v[i+1])sube=false;
        if(!sube and v[i]<v[i+1])return false;
    }
    return true;
}

int main()
{
    int T;
    cin>>T;
    forn(t,T)
    {
        cin>>n;
        vector<int>u(n),v,w;
        forn(i,n)cin>>u[i];
        v=u;
        sort(all(v));
        int ans=n*n;
        do
        {
            if(check(v))
            {
                w=u;
                int c=0;
                forn(i,n)
                {
                    int mj;
                    forn(j,n)if(w[j]==v[i]){mj=j;break;}
                    while(mj<i){swap(w[mj],w[mj+1]);mj++;c++;}
                    while(mj>i){swap(w[mj],w[mj-1]);mj--;c++;}
                }
                if(c<ans)ans=c;
            }
        }while(next_permutation(all(v)));
        
        cout<<"Case #"<<t+1<<": "<<ans<<endl;
    }
}
