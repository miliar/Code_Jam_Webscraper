#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>

#define pb push_back
#define ll long long
#define REP(a,b) for(int(a)=0;(a)<(b); (a)++)
using namespace std;

vector<int> rozl;
int n;
int sum;

void dva(){
	int mmx = 0;
	REP(a,rozl.size()){
		mmx = max(rozl[a],mmx);
	}
	vector<int> nejv;
	REP(a,rozl.size()){
		if(rozl[a] == mmx) nejv.pb(a);
	}
	if(nejv.size() == 2){
		cout<<" "<<(char)('A'+nejv[0])<<(char)('A'+nejv[1]);
		rozl[nejv[0]]--;
		rozl[nejv[1]]--;
		sum-=2;
		return;
	}
	rozl[nejv[0]]--;
	cout<<" "<<(char)('A'+nejv[0]);
	sum--;

}

void solve(int test){
	rozl.clear();
	sum = 0;
	scanf("%i",&n);

	REP(a,n){
		int pr;
		scanf("%i",&pr);
		rozl.pb(pr);
		sum+=pr;
	}
	printf("Case #%i:",test);
	while(sum > 0) dva();
	printf("\n");


}



int main(){
	int t;
	scanf("%i",&t);
	REP(a,t) solve(a+1);
	
	return 0;
}
