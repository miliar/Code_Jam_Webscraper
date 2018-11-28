#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <memory.h>
#include <ctime>
 
using namespace std;
 
#define ABS(a) ((a>0)?a:-(a))
#define MIN(a,b) ((a<b)?(a):(b))
#define MAX(a,b) ((a<b)?(b):(a))
#define FOR(i,a,n) for (int i=(a);i<(n);++i)
#define FI(i,n) for (int i=0; i<(n); ++i)
#define pnt pair <int, int>
#define mp make_pair
#define PI 3.14159265358979
#define MEMS(a,b) memset(a,b,sizeof(a))
#define LL long long
#define U unsigned
int cnt1=0,cnt2=0;
inline bool ispal(LL num)
{
	stringstream tmp;
	tmp<<num;
	string s1,s2;
	tmp>>s1;
	s2=s1;
	reverse(s2.begin(),s2.end());
	return (s1==s2);
}

inline vector<int> tovec(string s)
{
	vector<int> res;
	for (int i=(int)s.length(); i>0; i-=9)
	if (i<9)
		res.push_back(atoi(s.substr (0, i).c_str()));
	else
		res.push_back(atoi(s.substr(i-9, 9).c_str()));
	return res;
}
inline string mul(string s1)
{
	vector<int> a=tovec(s1);
	int base=1000000000;
	vector<int> res;
	res.resize(a.size()+a.size());
	FOR(i,0,a.size())
	{
		int p=0;
		for (int j=0; j<a.size() || p; ++j)
		{
			int v=0;
			if (j<a.size())
				v=a[j];
			LL k=a[i]*1ll*v+p+res[i+j];
			res[i+j]=k%base;
			p=k/base;
		}
	}
	while ((res.back()==0) && (res.size()>1))
		res.pop_back();
	string ans="";
	stringstream tmp;
	tmp<<res.back();
	tmp>>ans;
	for (int i=(int)res.size()-2; i>=0; --i)
	{
		char s2[15];
		sprintf(s2,"%09d",res[i]);
		ans+=(string)s2;
	}
	return ans;
}
inline bool check1(string s, string A)
{
	if (s.size()>A.size())
		return true;
	if (s.size()<A.size())
		return false;
	return (s>=A);
}
inline bool check2(string s, string A)
{
	if (s.size()<A.size())
		return true;
	if (s.size()>A.size())
		return false;
	return (s<=A);
}
inline bool ispal1(string s)
{
	int n=s.size();
	FOR(i,0,s.size()/2)
		if (s[i]!=s[n-i-1])
			return false;
	return true;
}
string A,B;
vector<string> Arr1;
vector<string> Arr2;
inline void go(string s)
{
	if (s.size()>51)
		return;
	Arr1.push_back(mul(s));
	s+=" ";
	int m=s.size()/2;
	for (int i=(int)s.size()-1; i>=0; --i)
	{
		if (i==m)
		{
			s[i]='0';
			break;
		}
		s[i]=s[i-1];
	}
	int res=1;
	FOR(i,0,3)
	{
		s[m]=i+'0';
		string s4=mul(s);
		if (ispal1(s4))
		{
			cnt2++;
			Arr1.push_back(s4);
		}
	}
	s+=' ';
	for (int i=(int)s.size()-1; i>=0; --i)
	{
		if (i==m)
		{
			s[i]='0';
			break;
		}
		s[i]=s[i-1];
	}
	FOR(i,0,3)
	{
		s[m]=s[m+1]=i+'0';
		string s4=mul(s);
		if (ispal1(s4))
		{
			//Arr1.push_back(s4);
			go(s);
		}
	}
}

int main()
{
#ifdef Fcdkbear
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    double beg=clock();
#else
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif

	int t;
	scanf("%d",&t);
	Arr1.push_back("1");
	Arr1.push_back("4");
	Arr1.push_back("9");
	go("11");
	go("22");
	FOR(it,0,t)
	{
		printf("Case #%d: ",it+1);
		cin>>A>>B;
		int res=0;
		FOR(i,0,Arr1.size())
		{
			if ((check1(Arr1[i],A)) && (check2(Arr1[i],B)))
				res++;
		}
		printf("%d\n",res);
		fprintf(stderr,"Case #%d solved\n",it+1);
	}
#ifdef Fcdkbear
    double end=clock();
    fprintf(stderr,"*** Total time = %.3lf ***\n",(end-beg)/CLOCKS_PER_SEC);
#endif
    return 0;
}