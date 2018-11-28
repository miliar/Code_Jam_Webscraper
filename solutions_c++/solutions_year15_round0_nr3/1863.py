#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>

using namespace std;
int ntest;
int L,t;
string s,r;
int f[105000], l[105000];

int mul(int x, int y){
	int res=1;
	if(x<0) res*=-1;
	if(y<0) res*=-1;
	
	if( abs(x)==1 && abs(y) == 1 ) return res;
	if( abs(x) == abs(y) ) return -1*res;
	if(abs(x)==1) return res*y;
	if(abs(y)==1) return res*x;
	
	if(abs(x) == 2){
		if( abs(y) == 3 ) return res*4;
		if( abs(y) == 4 ) return res*-3;
	}
	
	if(abs(x) == 3){
		if( abs(y) == 2 ) return res*-4;
		if( abs(y) == 4 ) return res*2;		
	}
	
	if(abs(x) == 4){
		if( abs(y) == 2 ) return res*3;
		if( abs(y) == 3 ) return res*-2;		
	}
}

int convert(char c){
	if(c=='i') return 2;
	if(c=='j') return 3;
	if(c=='k') return 4;
}

bool check(int x, int y){
	
		
	if( f[x] != 2 ) return false;
	
	if( f[ r.length()-1 ] != -1 ) return false;
	
	if(f[y-1] != 4  ) return false;
	
	
	return true;
}

void solve(int test){
	printf("Case #%d: ",test+1);
	scanf("%d %d\n",&L,&t);
	
	getline(cin,s);
	
	if(L*t < 3) { printf("NO\n"); return;}
	
	r="";
	
	for(int i=0; i<t; i++) 	r = r+s;
	
	f[0] = convert( s[0] );
	for(int i=1; r[i]; i++){
		f[i] = mul( f[i-1],convert(r[i]) );	
	}
		
	bool flag= false;
	for(int i=0; r[i]; i++)
		for(int j=i+2; r[j]; j++){
			if(check(i,j)) { flag= true; break; }
		}
		
		
	if(flag) printf("YES\n");
	else printf("NO\n");
}

int main(){
	freopen("C-small.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&ntest);
	for(int t=0; t<ntest; t++){
		solve(t);
	}
	return 0;
}
