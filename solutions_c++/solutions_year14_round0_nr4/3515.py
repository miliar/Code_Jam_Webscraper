#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <bitset>
#include <ctime>
#include <cmath>
#include <cassert>
#include <algorithm>
using namespace std;


#define pb(p) push_back(p)
#define fr(i,a,b) for(int i=a;i<b;i++)
#define frd(i,a,b) for(int i=a; i>=b i--)
#define PI 2*acos(0.0)
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()

int MIN (int a, int b) {
  int x= (b>a)?a:b;
  return x;
}

int MAX(int a, int b) {
  int x= (b<a)?a:b;
  return x;
}

#define maxn 10000000

/*vector<int>prime;
__int64 count[maxn+10];
bool visit[maxn+10];

void make_prime(){
    int i,j;
    int pos1=sqrt((double)maxn)+1;
	visit[1]=true;
	visit[4]=true;
	visit[6]=true;
	visit[8]=true;
    for(i=3;i<=pos1;i++)
	{
		if(visit[i]==false)
		{
			for(j=i*i;j<=maxn;j=j+i+i)
			visit[j]=true;
		}
	}
    prime.push_back(2);
    for(j=3;j<=maxn;j+=2)
        if( visit[j]==false )prime.push_back(j);
}
*/
typedef long long ll;
const int size = 1000007;
const ll modulo = 1000000007;
const ll inf = 1e18;
const double eps = 1e-6;
ll n,m,k,n25,n50,n100;

double a[4000],b[4000];
/*long LCMANDGCD()
{
	c=a*b;
	while(a!=b)
	{
		if(a>b)
		a=a-b;
		else
		b=b-a;
	}
	cout<< "HCF = " << a<<endl;
	cout<< "LCM = " << c/a<<endl;

}*/

int main()
{
   // #ifdef WRITE_IN_FILE
    freopen("D-large.in","r",stdin);
    freopen("largeRD.txt","w",stdout);
   // #endif
	int t;
	while(cin>>t)
	{
		for(int i=0;i<t;i++)
		{
			cin>>n;
			memset(a,0,sizeof(a));
			memset(b,0,sizeof(b));

			double temp[1010];
			double t1[1010];

			for(int j=0;j<n;j++)
			{
				cin>>a[j];
				t1[j] = a[j];
			}
			for(int j=0;j<n;j++)
			{
				cin>>b[j];
				temp[j] = b[j];
			}

			//normal game res

			sort(a,a+n);
			sort(b,b+n);

			int x = 0;
			int y = 0;
			int sz = n;

			for(int j=0;j<n;j++)
			{
				if(a[j]>b[sz-1])
				{
					x++;
					for(k=0;k<sz-1;k++)
					{
						b[k]=b[k+1];
					}
					sz--;
				}
				else
				{
					for(k=0;k<sz;k++)
					{
						if(a[j]<b[k])
						{
							//sz;
							for(int mm = k;mm<sz-1;mm++)
							{
								b[mm]=b[mm+1];
							}
							sz--;
							break;
						}
					}
				}


			}//end of normal game


			//unfair game starts

			int zz = 0;
			sz=n;

			sort(temp,temp+n);
			sort(t1,t1+n);

			for(int j=n-1;j>=0;j--)
			{
				if(temp[j]>t1[sz-1])
				{
					for(k=0;k<sz-1;k++)
					{
						t1[k]=t1[k+1];
					}
					sz--;
				}
				else
				{
					for(k=0;k<sz;k++)
					{
						if(temp[j]<t1[k])
						{

							zz++;
							//sz;
							for(int mm = k;mm<sz-1;mm++)
							{
								t1[mm]=t1[mm+1];
							}
							sz--;
							break;
						}
					}
				}


			}


			printf("Case #%ld: %ld %ld\n",i+1,zz,x);

			for(int j=0;j<n;j++)
			{
				temp[j]=0.0;
				t1[j]=0.0;
			}
	}

	}

	return 0;
}
