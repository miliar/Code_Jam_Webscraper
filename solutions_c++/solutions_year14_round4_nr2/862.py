#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define fr(a,b,c) for(int a = b; a < c; a++)
#define rep(a,b) fr(a,0,b)
#define pb push_back
#define db if(1)
#define ln puts("")

int n;

int r[1111];

bool read(){
	scanf("%d", &n);
	
	rep(i,n){
		scanf("%d", &r[i]);
	}
	
	return true;
}

int cn = 1;

int ind[1111][1111];

void process(){
	printf("Case #%d: ", cn++);

	vector<int> temp;
	
	rep(i,n){
		temp.pb(r[i]);
	}
	
	sort(temp.begin(), temp.end());
	
	rep(i,n){
		rep(j,n){
			if(r[j] == temp[i]) {
				//printf("%d became %d\n", r[j], i);
				r[j] = i;				
			}
		}
	}
	
	temp.clear();
	
	rep(i,n){
		//printf("%d ", r[i]);
		temp.pb(r[i]);
	}
	//ln;
	
	int res = 0;
	
	for(int i = n; i >= 1; i--){
		int lo = 0;
		
		//ln;
		rep(j,i){
			if(temp[j] < temp[lo]) lo = j;
			//ind[i][temp[j]] = j;
			//printf("%d ", temp[j]);
		}
		//ln;
		
		//printf("%d %d for %d\n", lo, (int)(temp.size()-lo-1), temp[lo]);
		
		res += min(lo, (int)(temp.size()-lo-1));
		
		temp.erase(temp.begin()+lo);
	}
	
	printf("%d\n", res);
	
}

int main(){
	int t;
	scanf("%d", &t);
	
	while(t-- && read()) process();
	
	return 0;
}


