#include<bits/stdc++.h>
#define in(x) scanf("%d",&x)
#define in2(x,y) scanf("%d%d",&x,&y)
#define in3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define inll(x) scanf("%lld",&x)
#define inll2(x,y) scanf("%lld%lld%lld",&x,&y)
#define inll3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z)
#define inc(x) scanf("%c",&x)
#define ins(x) scanf("%s",x)
#define out(x) printf("%d",x)
#define outll(x) printf("%lld",x)
#define outc(x) printf("%c",x)
#define outs(x) printf("%s",x)
#define F(x,y,z) for(int x=y;x<z;x++)
#define F2(x,y,z) for(int x=y-1;x>=z;x--)
#define F3(x,y,z) for(int x=y;x<z;x=x+2)
#define NL printf("\n")
#define _ printf(" ")
#define ln strlen
#define PB push_back
#define MP make_pair
#define pqueue priority_queue
#define X first
#define Y second
#define MAX 1001
#define MOD 1000000007
#define INF 99999999

using namespace std;

typedef long long int LL;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii > vii;

int main()
{
	 int t;in(t);
	 F(i,1,t+1){
	 	int l;in(l);
	 	char s[MAX];ins(s);
	 	int sum=0,count=0;
	 	int len=ln(s);
	 	F(j,1,len){
	 		sum+=s[j-1]-'0';
	 		if(sum<j){
	 			count+=j-sum;
	 			sum=j;
	 		}
	 	}
	 	printf("Case #%d: ",i);
	 	out(count);NL;
	 }
	 return 0;
}

