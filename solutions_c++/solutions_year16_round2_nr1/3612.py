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
int a[26];
string s;
vector<int> v;
string m[10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

void adj(int x){
	int len=m[x].length();
	FOR(i,0,len){
		a[m[x][i]-'A']--;
	}
}

int main(int argc, char **argv){
	//ios_base::sync_with_stdio(false);
	//const clock_t begin_time = clock();
	cin >> nt;
	FOE(k,1,nt){
		cin >> s;		
		CLR(a,0);		
		int len=s.length();
		FOR(i,0,len){
			a[s[i]-'A']++;
			switch(s[i]){				
				case 'Z':v.pb(0);adj(0);break;
				case 'X':v.pb(6);adj(6);break;
				case 'G':v.pb(8);adj(8);break;
				case 'W':v.pb(2);adj(2);break;
				case 'U':v.pb(4);adj(4);break;
				default: break;
			}
		}
		FOR(i,0,26){
			if(a['O'-'A']>0){
				v.pb(1);
				adj(1);
			}else if (a['H'-'A']>0){
				v.pb(3);
				adj(3);
			}else if(a['F'-'A']>0){
				v.pb(5);
				adj(5);
			}else if(a['S'-'A']>0){
				v.pb(7);
				adj(7);
			}else if(a['I'-'A']>0){
				v.pb(9);
				adj(9);
			}
		}
		sort(v.begin(),v.end());
		int sz=v.size();		
		printf("Case #%d: ",k);
		FOR(i,0,sz){
			printf("%d",v[i]);
		}
		puts("");
		v.clear();
	}	
	//std::cout <<endl<< float( clock () - begin_time ) /  CLOCKS_PER_SEC;
	return 0;
}