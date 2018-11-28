#include <stdio.h>
#include <string.h>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

const int mod_=1000002013;

int price(int n, int d, int c)
{
  if (d==0) return 0;
  --d;
  long long p=2*n-d;
  p*=(d+1);
  p>>=1;
  p%=mod_;
  p*=c;
  p%=mod_;
  return p;
}

int main()
{
	int _cn,_cc,i,c,c2;
        int n,m,e,o,p;
	scanf("%d",&_cn);
	for (_cc=1;_cc<=_cn;++_cc)
	{
		scanf("%d%d",&n,&m);
                map<int,pair<long long,long long> > x;
                map<int,long long> y;
                c=0;
                c2=0;
                for (i=0;i<m;++i)
                {
                  scanf("%d%d%d",&o,&e,&p);
                  x[o].first+=p;
                  x[e].second+=p;
                  c+=price(n,e-o,p);
                  if (c>=mod_) c-=mod_;
                }
                for (map<int,pair<long long,long long> >::iterator it1=x.begin();it1!=x.end();++it1)
                {
                  y[it1->first]+=it1->second.first;
                  long long v=it1->second.second;
                  map<int,long long>::iterator it2=y.end();
                  --it2;
                  while (v)
                  {
                    fflush(NULL);
                    if (v>=it2->second)
                    {
                      v-=it2->second;
                      c2+=price(n,it1->first-it2->first,it2->second);
                      if (c2>=mod_) c2-=mod_;
                      y.erase(it2--);
                    } else
                    {
                      c2+=price(n,it1->first-it2->first,v);
                      it2->second-=v;
                      if (c2>=mod_) c2-=mod_;
                      v=0;
                    }
                  }
                }
                c+=mod_-c2;
                if (c>=mod_) c-=mod_;
                printf("Case #%d: %d\n",_cc,c);
	}
	return 0;
}
