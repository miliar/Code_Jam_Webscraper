/*input
4
OZONETOWER
WEIGHFOXTOURIST
OURNEONFOE
FOURTHREETWOTWOEIGHTNINE
*/
#include <bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%d",&x);
#define slld(x) scanf("%lld",&x);
#define ss(x) scanf("%s",x);
#define sc(x) scanf("%c",&x);
#define LL long long
#define LD long double
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define bit(x,i) (x&(1<<i))  //select the bit of position i of x
#define lowbit(x) ((x)&((x)^((x)-1))) //get the lowest bit of x
#define pc1(x) cout<<x<<" "<<endl;
#define pc2(x,y) cout<<x<<" "<<y<<" "<<endl;
#define pc3(x,y,z) cout<<x<<" "<<y<<" "<<z<<" "<<endl;
#define pc4(w,x,y,z) cout<<w<<" "<<x<<" "<<y<<" "<<z<<" "<<endl;
#define pce(x) cout<<x<<endl;
#define ps0() cout<<endl;
#define ps1(x) cout<<#x<<" ";
#define ps2(x,y) cout<<#x<<" "<<y<<" "<<endl;
#define ps3(x,y,z) cout<<#x<<" "<<y<<" "<<z<<" "<<endl;
#define ps4(w,x,y,z) cout<<#w<<" "<<x<<" "#y<<" "<<z<<" "<<endl;
#define pse(x) cout<<#x<<endl;
#define GET_MACRO(_0, _1, _2, _3, _4, NAME, ...) NAME
#define GET_MACRO1(_1, _2, _3, _4, NAME, ...) NAME
#define ps(...) \
		do{if (DEBUG) GET_MACRO(_0, ##__VA_ARGS__, ps4, ps3, ps2, ps1, ps0)(__VA_ARGS__)} while(0);
#define pc(...) \
 		do{if (DEBUG) GET_MACRO1(__VA_ARGS__, pc4, pc3, pc2, pc1)(__VA_ARGS__)} while(0);
#define READ(filename)  freopen(filename, "r", stdin);
#define WRITE(filename)  freopen(filename, "w", stdout);

typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI; 

#define DEBUG 0

int main()
{
	READ("A-large.in")
	WRITE("A_large_out.txt")
	int T;
	int a[26],p[10];
	string s;
	sd(T)
	for(int t=1;t<=T;t++)
	{
		for(int i=0;i<26;i++)
		{
			a[i]=0;
		}
		printf("Case #%d: ",t);
		cin>>s;
		for(int i=0;i<s.length();i++)
		{
			// pc(s[i]-'A')
			a[s[i]-'A']++;
		}
		for(int i=0;i<26;i++)
		{
			pc((char)(i+'A'),a[i])
		}
		p[0]=a['Z'-'A'];
		p[2]=a['W'-'A'];
		p[6]=a['X'-'A'];
		p[8]=a['G'-'A'];
		p[3]=a['T'-'A']-p[2]-p[8];
		p[7]=a['S'-'A']-p[6];
		p[5]=a['V'-'A']-p[7];
		p[4]=a['F'-'A']-p[5];
		p[1]=a['O'-'A']-p[0]-p[2]-p[4];
		p[9]=a['I'-'A']-p[5]-p[6]-p[8];
		for(int i=0;i<10;i++)
		{
			pc(i,p[i])
		}
		for(int i=0;i<10;i++)
		{
			for(int j=0;j<p[i];j++)
			{
				printf("%d",i);
			}
		}
		printf("\n");
	}	
}
