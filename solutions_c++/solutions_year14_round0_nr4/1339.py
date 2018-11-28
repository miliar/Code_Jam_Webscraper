#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define fr(a,b,c) for(int a = b; a < c; a++)
#define rep(a,b) fr(a,0,b)
#define pb push_back
#define db if(1)
#define ln puts("")

int n;
double a[1111];
double b[1111];
bool read(){
	scanf("%d", &n);
	
	rep(i,n) scanf("%lf", &a[i]);
	rep(i,n) scanf("%lf", &b[i]);
	
	return true;
}

int regular(){
	sort(a, a+n);
	sort(b, b+n);
	
	int curk = 0;
	int res = 0;
	rep(i,n){
		while(curk < n && b[curk] < a[i]) curk++;
		if(curk >= n) res++;
		//else printf("ken used %lf against %lf\n", b[curk-1], a[i]);
		curk++;
	}
	
	return res;
}

int deceit(){
	sort(a, a+n);
	sort(b, b+n);
	//reverse(b, b+n);
	
	int res = 0;
	
	int j = 0;
	
	rep(i,n){
		//printf("%lf %lf\n", a[i], b[i]);
		if(a[i] > b[j]){
			res++;
			j++;
		}		
	}
	
	return res;
}

int complete(){
	sort(a, a+n);
	int res = 0;
	do{
		bool used[11];
		memset(used, false, sizeof used);
		int res2 = 0;
		vector<int> p;
		double eps = 1e-5;
		
		rep(i,n){
			int hi = -1;
			int lo = -1;
			
			double old = a[i];
			
			double big = a[i];
			rep(j,n) if(used[j] == false) big = max(big, b[j]);
			a[i] = big-eps;
			
			rep(j,n){
				if(used[j] == false){
					if(lo == -1){
						lo = j;
					} 
					if(hi == -1 && b[j] > a[i]) {
						hi = j;
					}
					if(lo != -1 && b[j] < b[lo]) lo = j;
					if(hi != -1 && b[j] > a[i] && b[j] < b[hi]) hi = j;					
				}
			}
			
			a[i] = old;
			
			if(hi != -1){
				p.pb(hi);
				used[hi] = true;
			}
			else{
				used[lo] = true;
				res2++;
				p.pb(lo);
			}		
		}
		
		res = max(res, res2);
			
		if(res2 == 8){
			rep(i,n){
				printf(">%lf %lf\n", a[i], b[p[i]]);
			}
			break;
		}
	} while(next_permutation(a, a+n));
	
	return res;
}
int cn = 1;

void process(){
	printf("Case #%d: %d %d\n", cn++, deceit(), regular());	
}

int main(){
	int t;
	scanf("%d", &t);
	
	while(t-- && read()) process();
	
	return 0;
}


