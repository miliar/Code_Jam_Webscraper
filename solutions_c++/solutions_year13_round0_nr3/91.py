#include<cstdio>
#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstdlib>
#include<climits>
#include<cstring>
using namespace std;

#define CLR(a,x) memset(a,x,sizeof(a))
#define PB push_back
#define INF 1000000000
#define MOD 1000000007
#define MP make_pair
#define tr(container , it) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define REP(i,a) FOR(i,0,a)
#define LL long long
#define VI vector < int >
#define PII pair < int , int >

#define Bits 26
#define MaxLen 52

vector < pair < int , string > > nums;
void check(string str)
{
	int j,k,sum,len=str.size(),count=0;
	string res;
	for(j=0;j<len;j++)
	{
		count+=str[j]=='1';
		sum=0;
		for(k=0;k<=j;k++)
			sum+=(str[k]-'0')*(str[j-k]-'0');
		if(sum>9)
			return;
		res+='0'+sum;
	}
	for(j=0;j<len-1;j++)
		res+=res[len-j-2];
	nums.PB(MP(2*len-1,res));
//	cout<<str<<" "<<res<<" "<<count<<endl;
}

void precompute(void)
{
	int i,mask,j,len,count;
	string str,strr;
	for(i=1;i<(1<<Bits);i+=2)
	{
		mask=i;
		str="";
		count=0;
		while(mask)
		{
			str+='0'+(mask&1);
			count+=mask&1;
			mask>>=1;
		}
		if(count>4)
			continue;
		strr=str;
		reverse(strr.begin(),strr.end());
		len=str.size();
		for(j=len;2*j<=MaxLen;j++)
		{
			check(strr+str);
			check(strr+"0"+str);
			check(strr+"1"+str);
			check(strr+"2"+str);
			str="0"+str;
			strr+='0';
		}
	}
	str="2";
	for(j=1;2*j<=MaxLen;j++)
	{
		strr=str;
		reverse(strr.begin(),strr.end());
		check(str+strr);
		check(str+"0"+strr);
		check(str+"1"+strr);
		str+='0';
	}
}

int main()
{
	long long t,ans,kase;
	string strA,strB;
	pair < int , string > A,B;
	precompute();
	nums.PB(MP(1,"1"));
	nums.PB(MP(1,"4"));
	nums.PB(MP(1,"9"));
	sort(nums.begin(),nums.end());
	while(scanf("%lld",&t)!=EOF)
	{
		kase=1;
		while(t--)
		{
			cin>>strA>>strB;
			A=MP(strA.size(),strA);
			B=MP(strB.size(),strB);
			ans=upper_bound(nums.begin(),nums.end(),B)-lower_bound(nums.begin(),nums.end(),A);
			printf("Case #%lld: %lld\n",kase,ans);
			kase++;
		}
	}
	return 0;
}

