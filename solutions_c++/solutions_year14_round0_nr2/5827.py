/*-->>Light Cavalry<<--*/

//Imp header files
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <sstream>
#include <map>
#include <list>
#include <deque>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <sstream>
#include <ctime>
#include <cassert>
#include <climits>
#include <fstream>
using namespace std;

//defined I/O
#define si(n) scanf("%d",&n)
#define sli(n) scanf("%ld",&n)
#define slli(n) scanf("%lld",&n)
#define sf(n) scanf("%lf",&n)
#define GetLine(n) getline(cin,n);
#define ss(n) scanf("%s",n)
#define pi(n) printf("%d",n)
#define pli(n) printf("%ld",n)
#define plli(n) printf("%lld",n)
#define pf(n) printf("%lf",n)
#define ps(n) printf("%s",n)
#define newLine printf("\n")
#define space printf(" ")
#define SWAP(a,b,t) t=a,a=b,b=t
#define Loop(i,a,n) for(__typeof(n) i(a); i<n; i++)
#define ULL unsigned long long int
#define LL long long int 

#define MOD 1000000007
//Imp functions
int gcd(int a, int b){if(b == 0)return a;else return gcd(b,a % b);}

#define get getchar_unlocked
inline int scan()
{
	int n=0,s=1;
	char p=get();
	if(p=='-') s=-1;
	while((p<'0'||p>'9')&&p!=EOF&&p!='-') p=get();
	if(p=='-') s=-1,p=get();
	while(p>='0'&&p<='9') { n = (n<< 3) + (n<< 1) + (p - '0'); p=get(); }
	return n*s;
}



int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.in","w",stdout);
	
	int t;
	t=scan();
	
	int c=0;
	while(t--)
	{
		c++;
		int ans1;
		ans1=scan();
		
		int a[17],b[17];
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		
		int x;
		
		Loop(i,0,4)
		{
			
			Loop(j,0,4)
			{
				x=scan();
				
				if(i==ans1-1)
				{
					a[x]=1;
				}
				
			}
			
		}
		
		int ans2;
		ans2=scan();
		
		Loop(i,0,4)
		{
			
			Loop(j,0,4)
			{
				x=scan();
				
				if(i==ans2-1)
				{
					b[x]=1;
				}
				
			}
			
		}
		
		int flag=0;
		
		int ans=0;
		Loop(i,1,17)
		{
			if(a[i]==1 && b[i]==1){
			flag++;
			ans=i;
			}
			
		}
		
		if(flag==1)
		cout<<"Case #"<<c<<": "<<ans<<endl;
		else if(flag==0)
		cout<<"Case #"<<c<<": Volunteer cheated!"<<endl;
		else
		cout<<"Case #"<<c<<": Bad magician!"<<endl;
		
	}
	
	return 0;
}





