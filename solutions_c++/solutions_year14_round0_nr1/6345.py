#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include<queue>
#define pii pair<int,int>
#define mk make_pair
#define pb push_back 
#define ll  long long
#define LB(v,x) lower_bound(v.begin(),v.end(),x)-v.begin()
#define UB(v,x) upper_bound(v.begin(),v.end(),x)-v.begin()
#define fi first
#define se second
using namespace std;

int caso=1;

void doit(){
	int a,b,x;
	cin>>a;
	vector<int>A,B;
	for(int i=1;i<=4;++i){
		for(int j=1;j<=4;++j){
			cin>>x;
			if(i==a)A.pb(x);	
		}
	}
	cin>>b;
	for(int i=1;i<=4;++i){
		for(int j=1;j<=4;++j){
			cin>>x;
			if(i==b)B.pb(x);	
		}
	}
	int ct=0,res=-1;
	for(int i=0;i<4;++i){
		for(int j=0;j<4;++j){
			if(A[i]==B[j]){
				ct++;
				res=A[i];
				break;
			}
		}
	}
	printf("Case #%d: ",caso++);
	if(ct==0){
		puts("Volunteer cheated!");
		return ;
	}
	if(ct==1)cout<<res<<endl;
	else	puts("Bad magician!");
	
}

int main(){
	int t;
	cin>>t;
	while(t--)doit();
}
