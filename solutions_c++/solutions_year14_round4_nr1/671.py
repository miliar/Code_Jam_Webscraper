#include <iostream>
#include <queue>
#include <string>
#include <map>
#include <set>
#include <iomanip> 
#include <vector>
#include <list>
#include <utility> 
#include <iterator> 
#include <math.h> 
#include <algorithm> 
#include <stdio.h> 
using namespace std;


#define REP(i,T) for(int i=0;i<T;++i)
#define MP make_pair
#define PII pair<int,int>
#define BG begin
#define ND end
#define VI vector<int>
#define VB vector<bool>
#define ALL(i) i.BG(),i.ND()
#define FORI(i,a,b) for(int i=a;i<b;++i)
#define OUT(i) while(!i.empty())
#define GP(a,b) a[b.first][b.second]
#define EX(a,b) (a.find(b)!=a.end())


long long gcd(long long a,long long b){
	long long tmp;
	while(b!=0){
		tmp=b;
		b=a%b;
		a=tmp;
	}
	return a;
}
void judge(){
	int n,x;
	cin>>n>>x;
	vector<int> s(n);
	vector<bool> av(n,true);
	REP(i,n){
		cin>>s[i];
	}
	sort(ALL(s));
	int ans=0;
	vector<int> stack;
	for(int i=n-1;i>=0;--i){
		if(!stack.empty()&&s[i]+stack.back()<=x){
			stack.pop_back();
			ans++;
		}
		else{
			stack.push_back(s[i]);
		}
	}
	ans+=stack.size();
	cout<<ans;
	return;


}
int main(){
	int t;
	scanf("%d",&t);
	REP(tt,t){
		cerr<<tt<<endl;
		printf("Case #%d: ",tt+1);
		judge();
		
		printf("\n");
	}
	return 1;
}