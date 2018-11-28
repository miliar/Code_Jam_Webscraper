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
	int n;
	cin>>n;
	int ans=0;
	vector<int> d(n);
	REP(i,n){
		cin>>d[i];
	}
	REP(i,n){
		int l=0,r=0;;
		for(int j=0;j<i;++j){
			if(d[j]>d[i])l++;
		}
		for(int j=i+1;j<n;++j){
			if(d[j]>d[i])r++;
		}
		ans+=l>r?r:l;
	}
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