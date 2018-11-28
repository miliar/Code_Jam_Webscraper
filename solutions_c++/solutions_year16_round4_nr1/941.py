#include <stdio.h>
#include <vector>
#include <iostream>
#include <string.h>
#include <assert.h>
#include <algorithm>
#include <time.h>
#define forn(i, n) for(int i = 0; i < (int)n; i++)
using namespace std;
int d[13][4097][4097];
int p[13][4097][4097];
int din(int n, int r, int p, int s){
	assert(r + s + p == (1 << n));
	if(n == 0){
		if(r == 1)return 1;
		if(s == 1)return 2;
		
		return 4;
	}
	if(d[n][r][s] != -1)return d[n][r][s];
	int & q = d[n][r][s];
	q = 0;
	for(int x = 0; x <= r; x++){
		int y = r - x;
		int z = p - y;
		//printf("\n\t!!!%d %d %d", x, y, z);
		if(y < 0 || z < 0)continue;
		if(z + x  != s)continue;
		//printf("!");
		(q |= din(n - 1, x, y, z));
			//q = 1;
			//printf("!");
			//return 1;
		
		
	}
	return q;
}
string ans, tmp;
void f(int n, int r, int p, int s, int t){
	assert(r + s + p == (1 << n));
	if(n == 0){
		if(r == 1) ans = "R";
		if(s == 1) ans = "S";
		if(p == 1) ans = "P";

		return ;
	}
	//if(d[n][r][s] != -1)return d[n][r][s];
	//int & q = d[n][r][s];
	//q = 0;
	//for(int t = 1; t < 5; t++)if(t != 3)
	for(int x = 0; x <= r; x++){
		int y = r - x;
		int z = p - y;
		if(y < 0 || z < 0)continue;
		if(z + x  != s)continue;
		if(din(n - 1, x, y, z) & t){
			f(n - 1, x, y, z, t);
			tmp=string();
			tmp.resize(2*ans.size());
			forn(j, ans.size()){
				if(ans[j] == 'R')
					tmp[2*j] = 'R', tmp[2*j + 1] = 'S';
				if(ans[j] == 'P')
					tmp[2*j] = 'P', tmp[2*j + 1] = 'R';
				if(ans[j] == 'S')
					tmp[2*j] = 'P', tmp[2*j + 1] = 'S';
				
			}
			swap(ans, tmp);
			return;
			//q = 1;
			//return 1;
		}
	}
	//	return q;


}
int ln;
string* ss;
bool cmp(int i, int j){
	for(int k = 0; k < ln; k++){
		if((*ss)[i + k] != (*ss)[j + k]){
			return (*ss)[i + k] < (*ss)[j + k];
		}
	}
	return 0;
}
void minsert(string &s, string::iterator b,string::iterator e){
	for(string::iterator it = b; it != e; it++)
		s.push_back(*it);
}
void srt(string &s){
	ss = &s;
	for(ln = 1; ln < (int)s.size() ; ln *= 2){
		tmp.clear();
		for(int i = 0; i < (int)s.size(); i += 2*ln){
			if(cmp(i, i + ln)){
				minsert(tmp, s.begin() + i, s.begin() + i + ln); 
				minsert(tmp, s.begin() + i + ln, s.begin() + i + ln + ln); 
			
			}
			else{
				minsert(tmp, s.begin() + i + ln, s.begin() + i + ln + ln); 
				minsert(tmp, s.begin() + i, s.begin() + i + ln); 
				
			}
		}
		swap(tmp, s);
	}
}
void solve(){
	//memset(d, -1,sizeof d);
	int n, r, p, s;
	cin >> n >> r >> p >> s;
	int msk;
	if(!(msk = din(n, r, p, s))){
		printf("IMPOSSIBLE");
		return;
	}
	string nl;
	nl.resize((1 << n), 'Z');
	vector<string> v(3,nl);
	
	if(msk & 1){f(n, r, p, s, 1);
		v[0] = ans;
		srt(v[0]);
	}
	if(msk & 2){
		f(n, r, p, s, 2);
		v[1] = ans;
		srt(v[1]);
	}
	if(msk & 4){
		f(n, r, p, s, 4);
		v[2] = ans;
		srt(v[2]);
	}
	ans = min(v[0], min(v[1], v[2]));
	cout << ans;
}
int main(){
	memset(d, -1, sizeof d);
	int t;
	cin >> t;
	forn(i, t){
		printf("Case #%d: ", i + 1);
		solve();
		puts("");
	}
	cerr << clock() << endl;
	return 0;
}
