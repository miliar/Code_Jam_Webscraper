#include <bits/stdc++.h>

using namespace std;

#define LL long long
#define INF 1000000000
#define pii pair<int,int>
#define vi vector<int>
#define mp make_pair
#define fi first
#define se second
#define pb push_back
#define pu push
#define MAX_N 100010

void r_win(){
	cout<<"RICHARD"<<endl;
}

void g_win(){
	cout<<"GABRIEL"<<endl;
}
	
int main(){
	int tc,x,r,c;
	cin>>tc;
	for(int zz = 1; zz <= tc; zz++){
		cin>>x>>r>>c;
		cout<<"Case #"<<zz<<": ";
		if(x == 1){
			g_win();
			continue;
		}
		if(x == 2){
			if(r % 2 == 0 || c % 2 == 0){
				g_win();
			}
			else{
				r_win();
			}
			continue;
		}
		if(x == 3){
			if((r % 3 == 0 || c % 3 == 0) && (r >= 2 && c >= 2)){
				g_win();
			}
			else{
				r_win();
			}
			continue;
		}
		if(x == 4){
			if(r*c % 4 != 0){
				r_win();
			}
			else if((r == 4 && c == 3) || (r == 3 && c == 4)){
				g_win();
			}
			else if(r < 4 || c < 4){
				r_win();
			}
			else{
				g_win();
			}
			continue;
		}
	}

}