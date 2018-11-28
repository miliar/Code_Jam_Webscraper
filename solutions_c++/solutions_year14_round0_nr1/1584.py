#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<sstream>
#include<assert.h>
#include<cmath>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<queue>
#include<stack>
using namespace std;
typedef long long ll;
const int inf=0x7fffffff;
const double pi=acos(-1.0);
#define eps (1e-15)
#define L(x) ((x)<<1)
#define R(x) ((x)<<1|1)
#define see(x)(cerr<<"[line:"<<__LINE__<<" "<<#x<<" "<<x<<endl)
#define se(x) cerr<<x<<" "
template<class T>T& ls(T& a,T b)
{ if(b<a) a=b; return a;}
template<class T>T& gs(T& a,T b)
{ if(b>a) a=b; return a;}
inline int to_i(const string& s)
{int n;sscanf(s.c_str(),"%d",&n);return n;}
inline string to_s(int n)
{char buf[32];sprintf(buf,"%d",n);return string(buf);}
int a[10][10];
int b[10][10];

int n=4;
int x,y;
int main()
{
    int i,j,k;
    // freopen("in","r",stdin);
    int cas=0,t;
    while(cin>>t)
    {
        while(t--)
        {
            cas++;
            cin>>x;
            x--;
            for(i=0; i<n; i++)
                for(j=0; j<n; j++)
                    cin>>a[i][j];
            cin>>y;
            y--;
            for(i=0; i<n; i++)
                for(j=0; j<n; j++)
                    cin>>b[i][j];

            vector<int>vc;
            for(i=0; i<n; i++)
                for(j=0; j<n; j++)
                {
                    if(a[x][i] == b[y][j])
                        vc.push_back(a[x][i]);
                }
            cout<<"Case #"<<cas<<": ";
            if(vc.size()==0)
                cout<<"Volunteer cheated!"<<endl;
            else if(vc.size()>1)
                cout<<"Bad magician!"<<endl;
            else
            {
                cout<<vc[0]<<endl;
            }
        }
    }
}