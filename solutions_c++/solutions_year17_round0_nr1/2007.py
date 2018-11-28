/*ckpeteryu Code Jam 2017 QR - Problem A Oversized Pancake Flipper*/
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
#define LL long long unsigned int

struct state{
	string s;
	int dist;
	state(){}
	state(string s):s(s){dist=0;}
};

int solve(string s,int p){
	set<string> lookup;
	set<string>::iterator it;
	int len=s.length();
	queue<state> q;
	bool found=false;
	state fin;
	q.push(state(s));
	while(!q.empty()){
		state cur=q.front();
		q.pop();
		if(cur.s.find_first_of("-")==string::npos){
			found=true;
			fin=cur;
			break;
		}
		FOR(i,0,len-p+1){			
			state ns=cur;
			FOR(j,0,p)
				ns.s[i+j]=(ns.s[i+j]=='+'?'-':'+');
			//cout<<"ori: "<<cur.s<<" new: "<<ns.s<<endl;
			if(lookup.find(ns.s)==lookup.end()){
				ns.dist+=1;
				q.push(ns);
				lookup.insert(ns.s);
			}
		}
	}
	if(found)
		return fin.dist;
	else
		return -1;
}

int solve2(string s,int p){
	int len=s.length();
	int ret=0;
	while(1){
		int pos=-1;
		FOR(i,0,len){
			if(s[i]=='-'){
				pos=i;
				break;
			}
		}
		//cout<<s<<endl;
		if(pos!=-1){
			ret++;
			int rem=p;
			FOR(i,pos,min(pos+p,len)){
				s[i]=s[i]=='+'?'-':'+';
				rem--;
			}
			if(rem>0){
				ret=-1;
				break;
			}
		}else
			break;
	}
	return ret;
}

int nt,p;
string s;
char c[1005];

int main(int argc, char **argv){
	//ios_base::sync_with_stdio(false);
	//const clock_t begin_time = clock();
	scanf("%d",&nt);
	stringstream ss;
	FOE(k,1,nt){
		scanf("%s %d",c,&p);
		//int ret=solve(string(c),p);
		int ret=solve2(string(c),p);
		ss<<ret;
		printf("Case #%d: %s\n",k,ret!=-1?ss.str().c_str():"IMPOSSIBLE");
		ss.str(string());
	}
	//std::cout <<endl<< float( clock () - begin_time ) /  CLOCKS_PER_SEC;
	return 0;
}