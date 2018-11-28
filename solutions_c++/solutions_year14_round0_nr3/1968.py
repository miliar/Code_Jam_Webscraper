#include <iostream>
using namespace std;

const int mx[] = { 0, 1,1,1,0,-1,-1,-1};
const int my[] = {-1,-1,0,1,1, 1, 0,-1};

int r,c,m;
int p[25];

int q(int i, int j){
	if(i>=r || j>=c || i<0 || j<0) return 0;
	if(p[i*c+j]) return 0;
	
	p[i*c+j] = 2;
	
	for(int x = 0; x < 8; x++) if(i+my[x]>=0 && i+my[x]<r && j+mx[x]>=0 && j+mx[x]<c && p[(i+my[x])*c + j+mx[x]] == 1) return 1;
	
	int ans = 1;
	for(int x = 0; x < 8; x++) ans += q(i+my[x], j+mx[x]);
	
	return ans;
}
bool check(){
	int a = q(0,0);
	return a == r*c-m;
}
bool go(int v, int np){
	if(np > m) return false;
	if(np < m && v >= r*c) return false;
	if(np == m){
		if(check()){
			cout << 'c';
			for(int i=0; i<r; i++){
				for(int j=0; j<c; j++) if(j+i>0){
					if(p[i*c+j] == 1) cout << '*'; else cout << '.';
				}
				if(i<r-1)cout << endl;
			}
			return true;
		}
		
		for(int i=0; i<r*c; i++) if(p[i]==2) p[i]=0;
		return false;
	}
	p[v] = 0; if(go(v+1, np)) return true;
	p[v] = 1; if(go(v+1, np+1)) return true;
	p[v] = 0; return false;
}

int main(){
	int t; cin >> t;
	for(int ca = 1; ca <= t; ca++){
		
		cin >> r >> c >> m;
		for(int i=0; i<r*c; i++) p[i] = 0;
		
		cout << "Case #" << ca << ": ";
		cout << endl;
		
		if(!go(1,0)) cout << "Impossible";
		
		cout << endl;
	}
	return 0;
}
