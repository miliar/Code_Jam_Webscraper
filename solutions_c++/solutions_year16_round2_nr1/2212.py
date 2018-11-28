#include<iostream>
#include<cstdio>
#include<vector>
#include<cstring>
#include<algorithm>
#include<bitset>
#include<cmath>
#include<string>
#include<climits>
#include<queue>
#include<cstdlib>
#include<iomanip>
#include<fstream>
#define rep(i,n) for(int i=0;i<n;i++)
#define repup(i,a,b) for(int i=a;i<=b;i++)
#define repdn(i,a,b) for(int i=b;i>=b;i--)
#define scd(n) scanf("%d",&n);
#define scl(n) scanf("%lld",&n);
#define scs(str) scanf("%s",str);
#define prdl(n) printf("%d\n",n);
#define prll(n) printf("%lld\n",n);
#define prd(n) printf("%d",n);
#define prl(n) printf("%lld",n);
#define pb push_back;
#define mp make_pair;
#define vi vector<int>;
#define vp vector< pair<int ,int> >;
typedef long long ll;
using namespace std;
ll mod=1e9+7;
int main()
{
	int t;
 	ofstream myfile;
  	myfile.open ("example.txt");
	scanf("%d",&t);
	repup(p,1,t)
	{
		string s;
		cin>>s;
		int cz=0,cw=0,cx=0,cg=0,cs=0,cf=0,cv=0,cr=0,ci=0,co=0;
		int i=0;
		while(i<s.length())
		{
			if(s[i]=='Z')
				cz++;
			else if(s[i]=='W')
				cw++;
			else if(s[i]=='X')
				cx++;
			else if(s[i]=='G')
				cg++;
			else if(s[i]=='S')
				cs++;
			else if(s[i]=='F')
				cf++;
			else if(s[i]=='V')
				cv++;
			else if(s[i]=='R')
				cr++;
			else if(s[i]=='I')
				ci++;
			else if(s[i]=='O')
				co++;
			i++;	
		}
//		cout<<cz<<endl;
		int A[10]={0};
		A[0]=cz;
		A[2]=cw;
		A[6]=cx;
		A[8]=cg;
		A[7]=cs-A[6];
		A[5]=cv-A[7];
		A[4]=cf-A[5];
		A[3]=cr-(A[4]+A[0]);
		A[1]=co-(A[2]+A[4]+A[0]);
		A[9]=ci-(A[5]+A[6]+A[8]);
		int j=0;
		myfile<<"Case #"<<p<<": ";
		while(j<10)
		{
			if(A[j]>0)
			{
			
			while(A[j]>0)
				{
					myfile<<j;
					A[j]--;
				}
			}
			j++;
		}
		myfile<<endl;
	}
	myfile.close();
	return 0;
}
