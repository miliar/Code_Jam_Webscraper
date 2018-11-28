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

int T, N;
string s[105], perm;
vector <string> plist;

void swap (char *x, char *y)
{
    char temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

void permute(char * a, int i, int n) 
{
   int j; 
   if (i == n){
     string x = (string)a;
     plist.pb(x);
   }
   else
   {
        for (j = i; j <= n; j++)
       {
          swap((a+i), (a+j));
          permute(a, i+1, n);
          swap((a+i), (a+j)); 
       }
   }
} 

bool check(string order){
	string str="";
	FOR(i,0,order.size()){
		str+=s[order[i]-'0'];
	}
	bool chk[28];
	FOR(i,0,26)
		chk[i]=false;
	bool valid = true;
	chk[str[0]-'a']=true;
	FOR(i,1,str.size()){
		if(str[i]!=str[i-1]){
			if(chk[str[i]-'a']==false)
				chk[str[i]-'a']=true;
			else{
				valid=false;
				break;
			}
		}
	}
	return valid;
}

int main()
{
	cin>>T;
	
	FOR(t,1,T+1){
		cin>>N;
		plist.clear();
		perm = "";
		FOR(i,0,N)
			cin>>s[i];
		FOR(i,0,N)
			perm+=(char)('0'+i);
		//cout<<perm<<endl;
		//plist.pb(perm);
		char tmp[1000];
		strcpy(tmp,perm.c_str());
		permute(tmp, 0, perm.size()-1);
		/*FOR(i,0,plist.size())
			cout<<plist[i]<<" ";
		cout<<endl;*/
		LL ans = 0;
		FOR(i,0,plist.size())
			if(check(plist[i]))
				++ans;
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}
