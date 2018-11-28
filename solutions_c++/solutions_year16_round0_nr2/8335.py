/*
  Author : Sharath Chandran
  Handle : sharad07

 Barbeque, movie & coke @ Saturday night...can't get any better than that.

*/

#include<bits/stdc++.h>
#define lld long long int
#define llu unsigned long long int
#define pb(x) push_back(x)
#define pii pair<int,int>
#define pll pair<lld,lld>
#define pq priority_queue<int> 
#define mp(x,y) make_pair(x,y)
#define sz size()
#define inp1(x) scanf("%d",&x)
#define inp2(x,y) scanf("%d%d",&x,&y)
#define inp3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define print(x) printf("%d",x)
#define println(x) printf("%d\n",x)
#define _for(i,x,y) for(int i=x;i<y;i++)
using namespace std;
const int maxx=1e5+3;
lld mod=1e9+7;
string dat;
int ans;

inline void calc()
{
    int len=dat.length(),N;
    int last=(unique(dat.begin(),dat.end())-dat.begin());
    N=last;
    ans=N;
    if(dat[N-1]=='+') ans--;
    return;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin>>T; 
	for (int testcase = 1; testcase <= T; testcase++) 
    {
        ans=0;
        cin>>dat; 
        calc();
		printf("Case #%d: %d\n", testcase, ans);
    }
    
    return 0;
}