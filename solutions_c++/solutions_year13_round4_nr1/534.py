#include <fstream>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

struct node
{
	int id,data;
	bool f;
};

node a[40000];
long long v[40000];
const int p=1000002013;

bool cmp(node x,node y)
{
	if (x.id<y.id||((x.id==y.id)&&(!y.f)&&(x.f))) 
		return true;
	else
		return false;
}

long long ans;

int main()
{
	string input="A-small-attempt0 (3).in",output="1.out";
	ifstream infile("A-small-attempt1 (2).in",ios::in);
	ofstream oufile("1.out",ios::out);
	int tt;
	long long t;
	int n,m;
	int l,r;
	infile>>tt;
	for (int loop=1;loop<=tt;loop++)
	{
		infile>>n>>m;
		ans=0;
		for (int i=0;i<m;i++)
		{
			infile>>a[2*i].id>>a[2*i+1].id>>a[2*i].data;
			a[2*i+1].data=a[2*i].data;
			ans=ans+((n+n-a[2*i+1].id+a[2*i].id+1)*(a[2*i+1].id-a[2*i].id)/2)%p*a[2*i].data%p;
			ans=ans %p;
			a[2*i].f=true;
			a[2*i+1].f=false;
		}
		m*=2;
		sort(a,a+m,cmp);
		t=0;
		for (int i=0;i<m;i++)
		{
			if (a[i].f)
			{
				t+=a[i].data;
				v[i]=t;
			}
			else
			{
				t-=a[i].data;
				v[i]=t;
			}
		}
		int j,min,k;
		for (int i=0;i<m;i++)
			if (a[i].f)
			{
				while (v[i]>0)
				{
					j=i+1;
					min=v[i];
					while (v[j]>0) 
					{
						if (v[j]<min)
						{
							min=v[j];
							k=j;
						}
						j++;
					}
					ans=ans-((n+n-a[j].id+a[i].id+1)*(a[j].id-a[i].id)/2)%p*min%p;
					for (k=i;k<j;k++) v[k]-=min;
				}
			}
		ans=(ans+p)%p;
		oufile<<"Case #"<<loop<<": "<<ans<<endl;
	}
}
