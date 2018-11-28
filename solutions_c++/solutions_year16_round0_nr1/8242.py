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
lld dat;
lld ans;

inline void calc()
{
    int ctr=0,len;
    bool done[11];
    memset(done,0,sizeof(done));
    lld num=0,mul=1,val,idx;
    
    if(dat==0) return; 
    
    for(lld i=1;i<=1000001;i++)
    {
        val=dat*i;
        while(val>0)
        {
            idx=val%10;
            if(done[idx]==0)
            {
                ctr++;
                done[idx]=1;
            }
            val-=idx;
            val/=10;
        }
        if(ctr==10) 
        {
            ans=dat*i;
            break;
        }
    }
    return;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin>>T; 
	for (int testcase = 1; testcase <= T; testcase++) 
    {
        ans=0;
        cin>>dat; 
        calc();
		if(ans==0) printf("Case #%d: INSOMNIA\n", testcase);
        else printf("Case #%d: %lld\n", testcase, ans);
    }
    
    return 0;
}