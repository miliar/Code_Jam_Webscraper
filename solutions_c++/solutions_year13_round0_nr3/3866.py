#include <iostream>
#include <set>
#include <vector>
#include <math.h>


using namespace std;

#define LEN 100
int D[LEN];

typedef long long ll;

set<ll> ans;

void anal(ll x){
	ll xx=(ll)sqrt(1.0*x);
	if(xx*xx != x) return;
	
	vector<int> v;
	while(xx>0){
		v.push_back(xx%10);
		xx/=10;
	}
	
	int l=(int)v.size();
	for(int i=0,j=l-1; i<j; i++,j--){
		if(v[i]!=v[j])return;
	}
	
	ans.insert(x);
}

void go(int pos, int len){
	if(2*pos>=len){
		ll z = 0;
		for (int i=0;i<len;i++){
			z=10ll*z+D[i];
		}
		
		anal(z);
		return;
	}
	int start=pos==0?1:0;
	
	for(int i=start;i<10;i++){
		D[pos]=D[len-1-pos]=i;
		go(pos+1,len);
	}
}

int main(){
	for (int i=1;i<=14;i++)go(0,i);
	int t;
	
	cin>>t;
	for(int tt=1;tt<=t;tt++){
		int a,b;
		cin>>a>>b;
		
		int cnt=0;
		for (set<ll>::iterator it=ans.begin(); it!=ans.end(); it++){
			if(a<=*it && *it<=b){
				cnt++;
			}
		}
		
		printf("Case #%d: %d\n",tt,cnt);
	}
	return 0;
}