#include<stdio.h>
#include<map>
#include<set>
#include<algorithm>
#include<vector>

using namespace std;
map<int,long long> enterCount;
map<int,long long> exitCount;
struct pass
{
	int enter;
	long long count;
};
struct pass_compare {
    bool operator() (const pass & p1,const pass &p2) const{
		return p1.enter>p2.enter;
    }
};
set<pass,pass_compare> curSet;
	long long mod=1000002013;
long long getCount(int enter, long long exit,long long n) 
{

	if(enter==exit)
		return 0;

	return ((n+n-(exit-enter-1))*(exit-enter)/2)%mod;

}
set<int> eventInt;

int main()
{
  int t;
  freopen("D:\\gcj\\A-small-attempt0.in","r",stdin);
  freopen("D:\\gcj\\output.txt","w",stdout);
  scanf("%d",&t);
  for(int tt=1;tt<=t;tt++)
  {
	  int n,m;
	  scanf("%d %d",&n,&m);
	  enterCount.clear();
	  exitCount.clear();
	  curSet.clear();
	  eventInt.clear();
	  long long feeGen=0;
	  for(int i=0;i<m;i++)
	  {
		  int o,e,p;
		  scanf("%d %d %d",&o,&e,&p);
		  //updateInt
		  eventInt.insert(o);
		  eventInt.insert(e);
		  enterCount[o]+=p;
		  exitCount[e]+=p;
		  long long ct=p;
		  long long fee=getCount(o,e,n);
		  fee=(fee*ct)%mod;
		  feeGen=(feeGen+fee)%mod;
	  }
	  long long feeGen2=0;

	  for (set<int>::iterator it=eventInt.begin();it!=eventInt.end();it++)
	  {
		  int curN=*it;
		  if(enterCount[curN]>0)
		  {
		    pass p;
		    p.enter=*it;
			p.count=enterCount[curN];
			curSet.insert(p);
		  }
		  long long exitC=exitCount[curN];
		  if(exitC>0)
		  {
			  while(exitC>0)
			  {
				  pass p=*curSet.begin();
				  curSet.erase(curSet.begin());

				  long long minus=min(p.count,exitC);
				  
				  if(p.count>minus) {
					  p.count-=minus;
					  curSet.insert(p);
				  }
				  exitC-=minus;
				  long long fee=getCount(p.enter,curN,n);
				  fee=(fee*minus)%mod;
				  feeGen2=(feeGen2+fee)%mod;
			  }
		  }

	  }
	  printf("Case #%d:%lld\n",tt,(feeGen+mod-feeGen2)%mod);
  }
}