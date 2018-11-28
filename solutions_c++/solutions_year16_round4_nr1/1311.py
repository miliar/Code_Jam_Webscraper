#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>

#define pb push_back
#define ll long long
#define REP(a,b) for(int(a)=0;(a)<(b); (a)++)
using namespace std;

string zkus(string co, int kol){
	if (kol == 0) return co;
	else if(co == "P"){
		return zkus("P",kol-1) + zkus("R",kol-1); 
	}else if(co == "S"){
		return zkus("P",kol-1) + zkus("S",kol-1); 
	}else{
		return zkus("R",kol-1) + zkus("S",kol-1); 
	}
}

bool jde(int p,int r, int s, string& vys){
	REP(a,vys.size()){
		if(vys[a] == 'P') p--;
		if(vys[a] == 'R') r--;
		if(vys[a] == 'S') s--;
	}
	if(p != 0) return false;
	if(s != 0) return false;
	if(r != 0) return false;
	return true;
}

bool jemen(string men, string vet){
	REP(a,men.size()){
		if(men[a] < vet[a]) return true;
		if(men[a] > vet[a]) return false;
	}
	return true;
}

string usporadej(string je){
	if(je.size() == 1) return je;
	string pr = usporadej(je.substr(0,je.size()/2));
	string dr = usporadej(je.substr(je.size()/2));
	if(jemen(pr,dr)) return pr+dr;
	else return dr+pr;
}

void solve(int test){
	int n,p,r,s;
	cin>>n>>r>>p>>s;
	string pp = usporadej(zkus("P",n));
	string rr = usporadej(zkus("R",n));
	string ss = usporadej(zkus("S",n));
	vector<string> vse;
	if(jde(p,r,s,pp)) vse.pb(pp);
	if(jde(p,r,s,ss)) vse.pb(ss);
	if(jde(p,r,s,rr)) vse.pb(rr);
	if(vse.size() == 0){
		printf("Case #%i: IMPOSSIBLE\n",test);
		return;
	}
	string ii = vse[0];
	REP(a,vse.size()){
		if(jemen(vse[a],ii)){
			ii = vse[a];
		}
	}
	cout<<"Case #"<<test<<": "<<ii<<endl;



}


int main(){
	int t;
	cin>>t;
	REP(a,t) solve(a+1);
	
	return 0;
}
