#include<vector>
#include<iostream>
#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<algorithm>
#include<string>
#include<cstring>
#include<cmath>
#include<set>
#include<map>
#include<deque>
#include<queue>
using namespace std;

#define S(n)					scanf("%d",&n)
#define SL(n) 					scanf("%lld",&n)
#define SF(n) 					scanf("%lf",&n)
#define INF						(int)1e9
#define LINF					(long long)1e18
#define NINF					1e-9
#define FOR(i,a,b)				for(int i=a;i<b;i++)
#define FORR(i,a,b)             for(int i=a;i>=b;i--)
#define REP(i,n)				FOR(i,0,n)
#define PB						push_back
#define MP                      make_pair
#define SZ(v)					((int)(v.size()))
#define OUT(p)					cout<<p<<endl;
#define PSE                     system("pause");

typedef long long LL;
typedef vector <int> VI;
typedef vector <long> VL;
typedef vector <LL> VLL;
typedef vector <bool> VB;

/*Main code begins now */

int main()
{
    
    LL test,x=1;
    SL(test);
    while(test--)
    {
                 priority_queue < pair <int , pair <int,int> > > heap;
                 int m,n;
                 cin>>n>>m;
                 int a[n][m];
                 REP(i,n)
                 {
                         REP(j,m)
                         {
                                 S(a[i][j]);
                                 heap.push(MP(a[i][j],MP(i,j)));
                         }
                 }
                 bool flag=0;
                 while(!heap.empty())
                 {
                                     bool flagr=0;
                                     bool flagc=0;
                                     int val=heap.top().first;
                                     int row=heap.top().second.first;
                                     int column=heap.top().second.second;
                                     //cout<<val<<" "<< row<< " " <<column<< endl;
                                     REP(i,n)
                                     {
                                             if(a[i][column]>val)
                                             {
                                                             flagr=1;
                                                             break;
                                             }
                                     }
                                     
                                     REP(i,m)
                                     {
                                             if(a[row][i]>val)
                                             {
                                                              flagc=1;
                                                              break;
                                             }
                                     }
                                     
                                     if(flagr && flagc)
                                     {
                                              flag=1;
                                              break;
                                     }
                                     heap.pop();
                 }
                 
                 if(flag)
                         cout<<"Case #"<<x<<": NO"<<endl;
                 else
                         cout<<"Case #"<<x<<": YES"<<endl;
                 x++;          
    }
}

