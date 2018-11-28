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

int nt,N;
vector<string> v;

struct compgt{
	bool operator()(pair<char,int> p1, pair<char,int> p2)const{
		return p2.second>p1.second;
	}
};

typedef priority_queue< pair<char,int>, vector< pair<char,int> >, compgt> MaxHeap;

MaxHeap h;

int main(int argc, char **argv){
	//ios_base::sync_with_stdio(false);
	//const clock_t begin_time = clock();	
	cin>>nt;
	FOE(k,1,nt){
		cin>>N;
		int t;
		int sum=0;
		FOR(i,0,N){
			cin>>t;
			sum+=t;	
			h.push(mp(i+'A',t));			
		}
		string x="";
		if(sum%2==1){
			pair<char,int> cur = h.top();
			h.pop();
			x.pb(cur.first);			
			v.pb(x);
			cur.second--;
			if(cur.second>0){
				h.push(cur);
			}
			x="";
		}
		int f=0;
		while(!h.empty()){
			pair<char,int> cur = h.top();
			h.pop();
			x.pb(cur.first);
			cur.second--;
			f++;
			if(cur.second>0){
				h.push(cur);
			}
			if(f>=2){
				v.pb(x);
				x="";
				f=0;				
			}
		}
		int sz=v.size();
		printf("Case #%d:",k);
		FOR(i,0,sz){
			printf(" %s",v[i].c_str());
		}
		puts("");		
		v.clear();
	}
	//std::cout <<endl<< float( clock () - begin_time ) /  CLOCKS_PER_SEC;
	return 0;
}