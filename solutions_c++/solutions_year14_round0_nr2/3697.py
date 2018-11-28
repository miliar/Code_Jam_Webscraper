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
ll n,m,a[4000],b[4000],k,n25,n50,n100;

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
    //#ifdef WRITE_IN_FILE
    freopen("B-large.in","r",stdin);
    freopen("largeB.txt","w",stdout);
   // #endif

	double c,f,x;
	int t;

	while(cin>>t)
	{
		for(int i=0;i<t;i++)
		{
			cin>>c>>f>>x;
			double speed = 2.00000000;

			double ck = 0.000000000;

			double tm = 0.000000000;
			double res = 0.000000000;

			res = x/speed;

			while(1)
			{
				if( res > (tm + (c/speed) + x/(speed+f)))
				{
					res = tm + c/speed+ x/(speed+f);
					tm += c/speed;
					speed += f;
				}
				else
				{
					break;
				}
			}

				printf("Case #%ld: %.10lf\n",i+1,res);
				/*if(((x-ck)/speed)<((x+c)/(speed+f)))
				{
					tm+=((x-ck)/speed);
					break;
				}
				else
				{
					tm+=((c-ck)/speed);
					speed+=f;
					ck=0;
				}*/

			
		}
	}
	
	return 0;
}
