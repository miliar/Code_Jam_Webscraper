/*ckpeteryu*/
#include<iostream>
#include<iomanip>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<climits>
#include<cmath>
#include<bitset>
#include<string>
#include<ctime>
#include<typeinfo>
#include<functional>
#include<map>
#include<set>
#include<vector>
#include<stack>
#include<queue>
//#include<regex>
#include<algorithm>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define FOD(i,s,e) for(int i=(s);i>=(int)(e);i--)
#define FORVEC(i,a) for(int i=0;i<(int)((a).size());i++)
#define pb push_back
#define mp make_pair
#define CLR(s,x) memset(s,x,sizeof(s))
#define LL long long int

int nt;
string s;

int main(int argc, char **argv){
	//ios_base::sync_with_stdio(false);
	//const clock_t begin_time = clock();	
	//scanf("%d",&nt);
	cin >> nt;
	FOE(k,1,nt){
		cin>>s;
		int len=s.size();
		char c=s[0];
		string ret="";
		ret.pb(s[0]);
		FOR(i,1,len){
			if(s[i]>=c){
				ret=s[i]+ret;
				c=s[i];
			}else{
				ret+=s[i];
			}			
		}
		printf("Case #%d: %s\n",k,ret.c_str());
	}
	//std::cout <<endl<< float( clock () - begin_time ) /  CLOCKS_PER_SEC;
	return 0;
}