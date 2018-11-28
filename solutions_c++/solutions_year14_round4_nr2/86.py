#include<stdio.h>
#include"stdafx.h"
#include<vector>
#include<algorithm>
#include<map>
using namespace std;
#define SIZE 2048
typedef long long ll;
typedef pair<ll,ll>pii;
class BIT
{
public:
  ll bit[SIZE+1];
  void init()
  {
	  fill(bit,bit+SIZE+1,0);
  }
  void update(int a,ll b)
  {
    for(;;)
      {
	if(a>SIZE)
	  {
	    break;
	  }
	bit[a]+=b;
	a+=a&-a;
      }
  }
  ll get(int a)
  {
    ll ret=0;
    for(;;)
      {
	if(a<=0)
	  {
	    break;
	  }
	ret+=bit[a];
	a-=a&-a;
      }
    return ret;
  }
};
BIT bi;
int main()
{
	FILE *fr=fopen("b-large.in","r");
	FILE *fw=fopen("out.txt","w");
	int data;
	fscanf(fr,"%d",&data);
	for(int p=0;p<data;p++)
	{
		bi.init();
  int num;
  fscanf(fr,"%d",&num);
  vector<int>vec,zv;
  for(int i=0;i<num;i++)
    {
      int zan;
      fscanf(fr,"%d",&zan);
      vec.push_back(zan);
      zv.push_back(zan);
    }
  sort(zv.begin(),zv.end());
  map<int,vector<int> >ma;
  for(int i=0;i<num;i++)
    {
      vec[i]=lower_bound(zv.begin(),zv.end(),vec[i])-zv.begin()+1;
      ma[vec[i]].push_back(i);
    }
  ll ans=0;
  map<int,vector<int> >::iterator it=ma.begin();
  for(;;)
    {
      if(it==ma.end())
	{
	  break;
	}
      vector<int>v=(*it).second;
      for(int i=0;i<v.size();i++)
	{
	  int ban=v[i]+bi.get(v[i]+1);
	  //printf("%d %d\n",v[i],ban);
	  ans+=min(ban,num+int(bi.get(SIZE))-1-ban-(int(v.size())-i-1));
	  //printf("%d\n",ans);
	  bi.update(v[i]+1,-1);
	}
      it++;
    }
  fprintf(fw,"Case #%d: %lld\n",p+1,ans);
	}
}