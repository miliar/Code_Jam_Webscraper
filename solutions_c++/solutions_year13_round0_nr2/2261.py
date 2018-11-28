#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
#include<queue>
#include<complex>
#include<set>
#include<map>
#include<sstream>
#include<string>
#include<deque>
#include<sys/time.h>
#include<fstream>
#include<bitset>

using namespace std;

#define mp make_pair
#define pb push_back
#define forn(i,n) for(int i=0;i<(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define all(v) v.begin(),v.end()

typedef long long int tint;

int main()
{
    int T;
    cin>>T;
    forn(t,T)
    {
        int n,m;
        string res;
        cin>>n>>m;
        vector<vector<int> >a(n,vector<int>(m));
        vector<vector<int> >b(n,vector<int>(m)),c(n,vector<int>(m));
        forn(i,n)forn(j,m)cin>>a[i][j];
        forn(i,n)
        {
            int M=0;
            forn(j,m)if(a[i][j]>M)M=a[i][j];
            forn(j,m)b[i][j]=(a[i][j]==M);
        }
        forn(j,m)
        {
            int M=0;
            forn(i,n)if(a[i][j]>M)M=a[i][j];
            forn(i,n)c[i][j]=(a[i][j]==M);
        }
        res="YES";
        forn(i,n)forn(j,m)if(b[i][j]+c[i][j]==0)res="NO";
        cout<<"Case #"<<t+1<<": "<<res<<endl;
    }
    return 0;
}
