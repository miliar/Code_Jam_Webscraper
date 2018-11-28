#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define F first
#define S second
typedef long long LL;


int ntest;
string R[20],P[20],S[20];
int n,p,r,s;

string update(string s){
	string r;
	for(int i=0; s[i]; i++){
		if(s[i]== 'R') r+= "RS";
		if(s[i]== 'S') r+= "PS";
		if(s[i]== 'P') r+= "PR";
	}
	return r;
}

void init(){
	R[0] = "R"; 
	P[0] = "P"; 
	S[0] = "S"; 
	for(int i=1; i<13; i++){
		R[i] = update(R[i-1]);
		S[i] = update(S[i-1]);
		P[i] = update(P[i-1]);		
	}
}

string f(string s, int n){
	if(n==1) return s;
	string t1 = s.substr(0,s.length()/2);
	string t2 = s.substr(s.length()/2,s.length()/2);
	string r1 = f(t1,n-1);
	string r2 = f(t2,n-1);
	if(r1<r2) return r1+r2;
	else return r2+r1;
}

void solve(int test){
	printf("Case #%d: ",test+1);
	scanf("%d %d %d %d",&n,&r,&p,&s);
	//Check R
	int cr=0,cp=0,cs = 0;
	for(int i=0; R[n][i]; i++){
		if(R[n][i] == 'R') cr++;
		if(R[n][i] == 'P') cp++;
		if(R[n][i] == 'S') cs++;
	}
	if(r==cr && s == cs &&  p == cp){
		cout << f(R[n], n) << endl; return;
	}
	//Check S
	cr=0,cp=0,cs = 0;
	for(int i=0; S[n][i]; i++){
		if(S[n][i] == 'R') cr++;
		if(S[n][i] == 'P') cp++;
		if(S[n][i] == 'S') cs++;
	}
	if(r==cr && s == cs &&  p == cp){
		cout << f(S[n], n) << endl; return;
	}
	//Check P
	cr=0,cp=0,cs = 0;
	for(int i=0; P[n][i]; i++){
		if(P[n][i] == 'R') cr++;
		if(P[n][i] == 'P') cp++;
		if(P[n][i] == 'S') cs++;
	}
	if(r==cr && s == cs &&  p == cp){
		cout << f(P[n], n) << endl; return;
	}
	cout << "IMPOSSIBLE" << endl;
}

int main(){
	freopen("A-large.in","r",stdin);
  	freopen("test.out","w",stdout);
  	init();
  	scanf("%d",&ntest);
  	for(int test=0; test<ntest; test++){
  		solve(test);
	}
  	return 0;
}


