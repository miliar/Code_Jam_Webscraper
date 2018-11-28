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

/*
struct state{
	int cnt;
	int prevPos;
	string val;	
	vector<string> hist;
	vector<int> posHist;
	state(){}
	state(int cnt,string val,int prevPos):cnt(cnt),val(val),prevPos(prevPos){}
};

int minCost;

void Cha(int kt, string val){
	minCost=(1<<20);
	queue<state> q;
	state st=state(0,val,-1);
	state fin;
	q.push(st);
	set<string> hist;
	hist.insert(st.val);
	while(!q.empty()){
		state cur=q.front();
		//cout<<cur.cnt<<" "<<cur.val<<endl;
		q.pop();
		if(cur.val.find("-")!=string::npos && cur.cnt < minCost){
			FOD(i,cur.val.size()-1,0){
				if(cur.prevPos!=i){
					string nseq=cur.val;
					reverse(nseq.begin(),nseq.begin()+i+1);
					FOE(j,0,i){
						if(nseq.at(j)=='+'){
							nseq.at(j)='-';
						}else{
							nseq.at(j)='+';
						}
					}					
					if(hist.find(nseq)==hist.end()){
						state ns=state(cur.cnt+1,nseq,i);
						ns.hist=cur.hist;
						ns.hist.pb(cur.val);
						ns.posHist=cur.posHist;
						ns.posHist.pb(i);
						hist.insert(nseq);
						q.push(ns);
					}
				}
			}			
		}else{	
			if(minCost>cur.cnt){
				minCost=cur.cnt;
				fin=cur;
			}
		}
	}
	//cout<<minCost<<endl;
	printf("Case #%d: %d\n",kt,minCost);
	//set<string>::iterator it;
	//for(it=fin.hist.begin();it!=fin.hist.end();it++){
	//	cout<<*it<<endl;
	//}
	//FORVEC(i,fin.hist){
		//cout<<fin.hist[i]<<" "<<fin.posHist[i]<<endl;
	//}
}*/


/*
int maxDepth=10;

void dfs(int d,string val){
	if(d>=maxDepth){		
		cout<<val<<endl;
		return;
	}else{
		dfs(d+1,val+"+");
		dfs(d+1,val+"-");
	}
}

void Prepare(){
	printf("%d\n",(int)pow(2,maxDepth));
	dfs(0,"");
}
*/

void solve(int kt, string val){
	int sz=val.size();
	char prev=val.at(sz-1);
	int ret=prev=='+'?0:1;
	FOD(i,sz-2,0){
		if(val.at(i)!=prev){
			ret++;
		}
		prev=val.at(i);
	}
	printf("Case #%d: %d\n",kt,ret);
}

int main(int argc, char **argv){
	//ios_base::sync_with_stdio(false);
	//const clock_t begin_time = clock();
	int kt=0;
	string val;
	cin >> kt;
	FOE(i,1,kt){
		cin >> val;
		solve(i,val);
	}
	//std::cout <<endl<< float( clock () - begin_time ) /  CLOCKS_PER_SEC;
	return 0;
}