#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

__int128 pov(__int128 a, int p)
{
	if(p==0) return 1;
	if(p==1) return a;
	if(p&1) return a*pov(a, p-1);
	__int128 t=pov(a, p>>1);
	return t*t;
}

__int128 conv(__int128 a, int base)
{
	__int128 res=0;
	int tmp=0;
	while(a>0)
	{
		res+=(a%10)*pov(base, tmp);
		a/=10;
		tmp++;
	}
	return res;
}

__int128 gen(int n)
{
	__int128 a=1;
	n--;
	while(n--)
		a*=10;
	return a+1;
}

__int128 next(__int128 b)
{
	vector<bool> bn;
	while(b>0)
		bn.push_back(b%10), b/=10;

	bool s=0;
	for(int i=1;i<(int)bn.size();i++)
		if(!s)
		{
			if(bn[i])
				bn[i]=0, s=1;
			else
			{
				bn[i]=1;
				break;
			}
		}
		else
		{
			if(!bn[i])
			{
				bn[i]=1;
				break;
			}
			else
				bn[i]=0;
		}	
	__int128 a=0;
	for(int i=(int)bn.size()-1;i>=0;i--)
		a=a*10+bn[i];
	return a;
}
void out(__int128 a)
{
	vector<int> ab;
	while(a>0)
		ab.push_back(a%10), a/=10;
	for(int i=(int)ab.size()-1;i>=0;i--)
		printf("%d", ab[i]);
}

void stderrout(__int128 a)
{
	vector<int> ab;
	while(a>0)
		ab.push_back(a%10), a/=10;
	for(int i=(int)ab.size()-1;i>=0;i--)
		fprintf(stderr,"%d", ab[i]);
		fprintf(stderr,"\n");
}

int main()
{
	__int128 a,b;
	int t;
	scanf("%d", &t);
	int n,j;
	for(int tc=1;tc<=t;tc++)
	{
		scanf("%d %d", &n, &j);
		a=gen(n);
		printf("Case #%d:\n", tc);
		while(j)
		{
			bool f=1;
			vector<int> ans;
			for(int i=2;i<=10;i++)
			{
				bool fc=1;
				int d;
				b=(__int128)conv(a, i);
				stderrout(a);
				cerr<<"conv to "<<i<<" :";
				stderrout(b);
				for(d=2;d<10000;d++)
				{
					if(b%d==0)
					{
						cerr<<(int)b<<"%"<<d<<"=0\n";
						fc=0;
						break;
					}
				}
				if(fc)
				{
					f=0;
					break;
				}
				else
				{
					cerr<<"push "<<d<<"\n";
					ans.push_back(d);
					cerr<<"pushed "<<ans[ans.size()-1]<<"\n";
				}

			}

			if(f&&ans.size()==9)
			{
				j--;
				out(a);
				for(int i=0;i<9;i++)
					printf(" %d", ans[i]);
				printf("\n");
			}
			a=next(a);
		}
		
		printf("\n");
	}
	return 0;
}