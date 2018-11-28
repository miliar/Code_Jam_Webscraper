#include<cstdio>
#include<algorithm>

int n,High,Low,Equal;

double __r,__c;

long double V,X,_R,_RC;

struct pt{long double r,c;} p[110];

bool cmp(pt a,pt b){return a.c>b.c;}
	
int main()
{
	int TestCase,Case,i;
//	freopen("b.in","rb",stdin);
//	freopen("b1.out","wb",stdout);
	scanf("%d",&TestCase);
	for(Case=1;Case<=TestCase;Case++)
	{
		scanf("%d%lf%lf",&n,&__r,&__c);V=__r;X=__c;
		High=Low=Equal=0;
		for(i=0;i<n;i++)
		{
			scanf("%lf%lf",&__r,&__c);
			p[i].r=__r;
			p[i].c=__c-X;
			if(p[i].c>1e-6)High=1;
			else if(p[i].c<-1e-6)Low=1;
			else Equal=1;
		}
		if(!Equal&&(!Low||!High))
		{
			printf("Case #%d: IMPOSSIBLE\n",Case);
			continue;
		}
		std::sort(p,p+n,cmp);
		_R=_RC=0;
		for(i=0;i<n;i++)
		{
			_R+=p[i].r;
			_RC+=p[i].r*p[i].c;
		}
		if(_RC<0)
		{
			for(i=0;i<n;i++)
				p[i].c=-p[i].c;
			_RC=-_RC;
			std::sort(p,p+n,cmp);
		}
		for(i=0;i<n&&_RC>0&&p[i].c>0;i++)
		{
			if(_RC<=p[i].c*p[i].r)
			{
				_R-=_RC/p[i].c;
				_RC=0;
				break;
			}
			else
			{
				_R-=p[i].r;
				_RC-=p[i].r*p[i].c;
			}
		}
		V/=_R;
		__r=V;
		printf("Case #%d: %.20lf\n",Case,__r);
	}
	return 0;
}
