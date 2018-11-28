#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <deque>

#define REP(i,n) for(int i=0;i<(n);i++)
#define REPA(i,a,n) for(int i=(a);i<((a)+(n));i++)
#define INITW(var,value,width) for(int whslkfje=0;whslkfje<(width);whslkfje++) var[whslkfje]=(value)
#define INITHW(var,value,height,width) for(int hwesaft=0;hwesaft<(height);hwesaft++) \
		 for(int whslkfje=0;whslkfje<(width);whslkfje++) var[hwesaft][whslkfje]=(value)

typedef long long lint;
using namespace std;
void solve();
void init();

int main(){
	init();

	int T;
	cin>>T;
	string str;
	getline(cin, str);
	
	for(int t=1;t<=T;t++){
		cout<<"Case #"<<t<<":";
		solve();
		cout<<"\n";
	}
}

void init(){
	
}

int K,N;
int keys[201];
int c2k[21][201];
int type[21];
deque<int> qu;
bool found;
bool triedthis[2<<21];

bool wastried(){
	int sum=0;
	for (deque<int>::iterator it = qu.begin(); it != qu.end(); ++it){
		int var = *it;
		sum += (2<<var);
	}
	return triedthis[sum];
}
void settried(){
	int sum=0;
	for (deque<int>::iterator it = qu.begin(); it != qu.end(); ++it){
		int var = *it;
		sum += (2<<var);
	}
	triedthis[sum]=true;
}

void trie(int i){
	if(found)return;
	if((int)qu.size()==N){
		found=true;
		return;
	}
	if(find(qu.begin(), qu.end(), i) != qu.end()) return;
	int neededtype = type[i];
	if(!keys[neededtype])return;
	
	qu.push_back(i);
	if(wastried()){
		qu.pop_back();
		return;
	}
	keys[neededtype]--;
	REPA(k,1,201)keys[k]+=c2k[i][k];
	
	REPA(ii,1,N)trie(ii);
	if(found)return;
	
	settried();
	qu.pop_back();
	keys[neededtype]++;
	REPA(k,1,201)keys[k]-=c2k[i][k];
}

void solve(){
	cin>>K>>N;
	INITW(triedthis,false,2<<21);
	INITW(keys,0,201);
	INITW(type,0,21);
	INITHW(c2k,0,21,201);
	REP(i,K){
		int tk;
		cin>>tk;
		keys[tk]++;
	}
	REPA(n,1,N){
		cin>>type[n];
		int ki;
		cin>>ki;
		REP(i,ki){
			int ti;
			cin>>ti;
			c2k[n][ti]++;
		}
	}
	qu.clear();
	found=false;
	REPA(i,1,N)trie(i);
	
	if(!found)cout<<" IMPOSSIBLE";
	else{
		for (deque<int>::iterator it = qu.begin(); it != qu.end(); ++it){
			cout <<" "<< *it;
		}
	}
}
