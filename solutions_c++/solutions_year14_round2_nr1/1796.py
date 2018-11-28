#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <sstream>
using namespace std;

#define FOR(i,x,n) for(int i=x;i<n;++i)
#define RFOR(i,x,n) for(int i=x;i>=n;--i)
#define ST 0.000000001
#define MOD 1000000007
#define pb(a) push_back(a)
#define b() begin()
#define e() end()
#define CLR(a,x) memset(a,x,sizeof(a))
#define sz(x) (int)x.size()
#define MP make_pair
#define tr(container , it) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)
#define LL long long
#define VI vector < int >
#define VUI vector < unsigned int >
#define VLL vector < long long >
#define VD vector < double >
#define PII pair < int , int >
#define INF 2147483647
#define LLINF 9223372036854775807
#define si(a) scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define sd(a) scanf("%lf",&a)

string reducer(string s){
	string s1="";
	s1+=s[0];
	FOR(i,1,s.size()){
		if(s[i]!=s[i-1])
			s1+=s[i];
	}
	return s1;
}

int finddiff(string s1,string s2){
	if(s1.size()>s2.size()){
		string tmp=s1;
		s1=s2;
		s2=tmp;
	}
	int p1=0,p2=0,score=0;
	string res=reducer(s1);
	FOR(i,0,res.size()){
		int c1=0,c2=0;
		while(s1[p1]==res[i] && p1<s1.size()){
			c1++;
			p1++;
		}
		while(s2[p2]==res[i] && p2<s2.size()){
			c2++;
			p2++;
		}
		score+=abs(c1-c2);
		//cout<<"--"<<abs(c1-c2)<<endl;
	}
	return score;
}
int N;
string s[105],s2[100];
int main()
{
	int T;
	cin>>T;
	FOR(t,1,T+1){
		cin>>N;
		int fail=0, score=0;
		FOR(i,0,N){
			cin>>s[i];
			s2[i] = reducer(s[i]);
		}
		FOR(i,1,N){
			if(s2[i]!=s2[i-1]){
				fail=1;
				break;
			}
		}
		if(fail){
			cout<<"Case #"<<t<<": Fegla Won"<<endl;
			continue;
		}
		score+=finddiff(s[0],s[1]);
		cout<<"Case #"<<t<<": "<<score<<endl;
	}
	return 0;
}

