#include <bits/stdc++.h>
using namespace std;
string p;
char f(char p){return p == '+' ? '-' : '+';}
void rev(string &p, int j){
	reverse(p.begin(), p.begin()+j);
	for(int i = 0; i<j; i++) p[i] = f(p[i]); 
}
bool g(string &p){
	for(int i = 0; i<p.size(); i++){
		if(p[i] == '-') return true;
	}
	return false;
}
int main(){
	int t;cin >>t;
	for(int y = 1;y<=t;y++){	
			cin >> p;
			int N = p.size();
			int i = 0,j = N-1,res = 0;
			res+=(N == 1 && p[0] == '-');
			while(g(p)&&j>0){
				while(p[j] == '+') j--;
				int k = 0;
				for( ;p[k] == '+';k++) ;
				rev(p,k);
				res+=(k != 0);
				int h = k;
				for( ; p[k] == '-'; k++) ;
				rev(p,k);
				res+=(h != k);
			}
			printf("Case #%d: %d\n",y,res);
		}
}