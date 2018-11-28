#include <bits/stdc++.h>
using namespace std;

#define R(i,a,b) for(int i=a;i<b;i++)
#define RE(i,a,b) for(int i=a;i<=b;i++)
#define RR(i,a,b) for(int i=a;i>b;i--)
#define RRE(i,a,b) for(int i=a;i>=b;i--)
#define F(i,n) for(int i=0;i<n;i++)
#define FE(i,n) for(int i=0;i<=n;i++)
#define FR(i,n) for(int i=n;i>0;i--)
#define FRE(i,n) for(int i=n;i>=0;i--)
#define mp(a,b) make_pair(a,b)
#define pii pair <int, int>
#define pb push_back
#define ft first
#define sd second
#define LL long long
#define gc getchar_unlocked
#define pc putchar_unlocked

inline void get(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

int a[30];
pii part[30];

bool cmp(pii a, pii b)
{
	return a.ft > b.ft;
}

int main()
{
	int T;
	get(T);
	for (int __rep = 1; __rep <=T; __rep++)
	{
		int n;
		get(n);

		int sum = 0;

		F(i,n)
		{
			get(a[i]);
			part[i] = mp(a[i],i);
		}

		cout << "Case #" << __rep << ": ";	
		if (n == 2)
		{
			for (int i=0; i<a[0]; i++)
			{
				cout << "AB ";
			}
			cout << endl;
		}
		else
		{
			sort(part, part+n, cmp);
			while (part[0].ft != 1)
			{
				for (int i=0; i<n; i++)
				{
					if (i!=0 && part[i].ft <= part[i-1].ft)
					{
						i=-1;
						continue;
					}
					if (i == 0 && part[i].ft == 1)
						break;
					cout << char('A'+part[i].sd) << " ";
					part[i].ft -= 1;
				}
			}
			
			if (n%2)
			{
				cout << "A "; 
				for (int i=1; i<n; i+=2)
				{
					cout << char('A'+i) << char('A'+i+1) << " ";
				}
			}
			else
			{
				for (int i=0; i<n; i+=2)
				{
					cout << char('A'+i) << char('A'+i+1) << " ";
				}	
			}
			cout << endl;
		}


	}
	return 0;
}