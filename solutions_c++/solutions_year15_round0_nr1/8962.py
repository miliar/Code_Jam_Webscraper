#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<list>
#include<sstream>
#include<utility>
#include<climits>
#include<fstream>
#include<bitset>

using namespace std;

#define Max 1000000000
#define Min -1
#define lli long long int
#define psb push_back
#define pob pop_back
#define forl(i,n) for(i=1;i<=n;i++)
#define all(a) a.begin(),a.end()

typedef pair<int,int> pii;
typedef pair<lli,lli> pli;
typedef vector<int> vi;
typedef vector<lli> vli;

//int kdx[] = { -2, -2, -1, 1, 2,  2,  1, -1 };
//int kdy[] = { -1,  1,  2, 2, 1, -1, -2, -2 };
/*
int Set(int N,int pos){return N=N | (1<<pos);}
int reset(int N,int pos){return N= N & ~(1<<pos);}
bool check(int N,int pos){return (bool)(N & (1<<pos));}
*/

char odi[1024];

int smax,cumu,mini;

int main()
{
//ios::sync_with_stdio(false);
int t,i,j,ln;
freopen("A-large.in","r",stdin);
freopen("output","w",stdout);
scanf("%d",&t);

for(j=1;j<=t;j++){
    mini = 0;
    scanf("%d %s",&smax,odi);
    cumu = odi[0]-'0';
    for(i=1;i<=smax;i++){
        if(i>cumu){
            mini += i - cumu;
            cumu = i + odi[i]-'0';
        }
        else{
            cumu += odi[i] - '0';
        }

    }

    printf("Case #%d: %d\n",j,mini);
}


return 0;
}
