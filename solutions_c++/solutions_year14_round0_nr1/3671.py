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

int a[4000][4000],b[4000][4000];
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
    freopen("A-small-attempt0.in","r",stdin);
    freopen("outputCJA.txt","w",stdout);

	long t;

	while(cin>>t)
	{
		for(int i=0;i<t;i++)
		{
			cin>>m;

			int temp[5];

			for(int j=1;j<=4;j++)
				for(k=1;k<=4;k++)
				{
					cin>>a[j][k];
					if(j==m) temp[k]=a[j][k];
				}
			
			/*for(int j=1;j<=4;j++)
			{
				cout<<temp[j]<<endl;
			}*/

				int z;
				cin>>z;

				int temp1[5];

				for(int j=1;j<=4;j++)
				{
					for(k=1;k<=4;k++)
					{
						cin>>b[j][k];
						if(j==z) temp1[k]=b[j][k];
					}
				}

				bool bf = false;
				int cnt = 0;
				int savepos=0;

				/*for(int j=z;j<=z;j++)
				{
					for(k=1;k<=4;k++)
					{
						for(int v=1;v<=4;v++)
						{
							if(b[j][k]==temp[v])
							{
								cnt++;
								savepos = v;
								break;
							}
						}
					}
					}
				*/


				for(int j=1;j<=4;j++)
				{
					for(k=1;k<=4;k++)
					{
						if(temp1[j]==temp[k])
						{
							cnt++;
							savepos=k;
						}
					}
				}
				if(cnt==1)
				{
					printf("Case #%ld: %ld\n",i+1,temp[savepos]);
				}
				else if(cnt>1)
				{
					printf("Case #%ld: Bad magician!\n",i+1);
				}
				else if (cnt==0)
				{
					printf("Case #%ld: Volunteer cheated!\n",i+1);
				}

		}
	}
	
	return 0;
}
