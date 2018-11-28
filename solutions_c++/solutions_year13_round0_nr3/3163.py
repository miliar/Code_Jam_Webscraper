#include <iostream>
#include<iomanip>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <deque>
//#define SET(p) memset(p,-1,sizeof(p))
//#define CLR(p) memset(p,0,sizeof(p))
#define LL long long int
#define ULL unsigned long long int
#define S(n) scanf("%d",&n)
#define Sl(n) scanf("%lld",&n)
#define Sf(n) scanf("%lf",&n)
#define Ss(n) scanf("%s",n)
using namespace std;
int kmod=1000000007;

bool IsPalindrome(char *s)
{
	int n=strlen(s);
	int i=0;
	int j=n-1;
	while(i<j)
	{
		if(s[i]!=s[j])
			return false;
		i++;
		j--;
	}
	return true;

}
void fun(int k)
{
	long long int a,b;
	Sl(a);
	Sl(b);
	long long int l=sqrt(a);
	if(l*l!=a)
		l++;
	long long int h=sqrt(b);

	//cout<<l<<" "<<h<<endl;
	int count=0;
	char buffer[20];
	while(l<=h)
	{

		sprintf(buffer,"%lld",l);
		//cout<<buffer[0]<<endl;
		if(buffer[0]>'3')
		{
			l++;
			continue;
		}
		bool p=IsPalindrome(buffer);
		//cout<<p<<endl;
		if(p==true)
		{
			long long int y=l*l;
			sprintf(buffer,"%lld",y);
			//cout<<buffer[0]<<endl;
			bool q=IsPalindrome(buffer);
			if(q==true)
				count++;
		}
		l++;
	}
	printf("Case #%d: %d\n",k,count);
}

int main()
{
	int t;
	S(t);
	for(int k=1;k<=t;k++)
	{
		fun(k);
		//cin>>s;
	}
	return 0;
}

