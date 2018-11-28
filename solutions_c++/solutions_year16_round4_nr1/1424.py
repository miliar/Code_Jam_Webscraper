#include <bits/stdc++.h>
#define pii pair<int,int>
#define mp make_pair
using namespace std;
#define rock 2
#define scissor 3
#define paper 1

int uu;


int check (int x, int y, int z){
	if (x>y+z or y>z+x or z>x+y) return 0;
	if (x+y+z==2){
		if (z==2 or y==2 or x==2) return 0;
		return 1;
	}
	if (!x or !y or !z) return 0;
	int n= x+y+z;
	return check(n/2-y, n/2-z, n/2-x);
}

int id[4], tmp[4];

bool cmp (int i, int j){
	return (id[i]<id[j]);
}

bool cmp2 (pair <pii, int> x, pair <pii, int> y){
	if (id[x.first.first]!=id[y.first.first]) return (id[x.first.first]<id[y.first.first]);
	if (id[x.first.second!=id[y.first.second]]) return (id[x.first.second]<id[y.first.second]);
	return (x.second<y.second);
}


pair <pii,int> t[4];

int find (int n){
	for (int i=1; i<=3; i++) if (id[i]==n) return i;
}

void gnt (){
	t[1]= mp(mp(id[1], id[3]), 1);
	t[2]= mp(mp(id[2], id[1]), 2);
	t[3]= mp(mp(id[2], id[3]), 3);
	sort(t+1, t+4, cmp2);
	for (int i=1; i<=3; i++){
		if (t[i].first.first>t[i].first.second){
			int tp= t[i].first.first;
			t[i].first.first= t[i].first.second;
			t[i].first.second= tp;

		}
	}
	sort(t+1, t+4);
	for (int i=1; i<=3; i++) id[t[i].second]= i;
}



char itc (int n){
	if (n==1) return 'R';
	if (n==2) return 'P';
	if (n==3) return 'S';
}


pii get (int n){
	pii pp;
	if (n==1) pp= mp(1, 3);
	else if (n==2) pp= mp(1, 2);
	else pp= mp(2, 3);
	if (id[pp.first]>id[pp.second]){
		int tmp= pp.first;
		pp.first= pp.second;
		pp.second= tmp;
	}
	return pp;
}

vector <int> cons (vector <int> v){
	int x, y, z;
	x= v[0];
	y= v[1];
	z= v[2];
	int n= x+y+z;
	int t[4]= {0, 1, 2, 3};
	sort(t+1, t+4, cmp);

	int q;
	if (n==2){
		vector <int> res;
		for (int i=1; i<=3; i++){
			q= t[i];
			for (int j=0; j<v[q-1]; j++) res.push_back(q);
		}
		return res;
	}
	vector <int> p;
	p.push_back(n/2-y);
	p.push_back(n/2-z);
	p.push_back(n/2-x);
	int pp[4];
	for (int i=1; i<=3; i++) pp[i]= id[i];
	gnt();
	vector <int> res= cons(p);
	for (int i=1; i<=3; i++) id[i]= pp[i];
	vector <int> pres;
	for (int i=0; i<res.size(); i++){
		pii t= get(res[i]);
		pres.push_back(t.first);
		pres.push_back(t.second);
	}
	return pres;

}



void solve(){
	int m, r, s, p, n;
	cin>>m>>r>>p>>s;
	n= (1<<m);
	if (n==2){
		if (r==2 or p==2 or s==2){
			cout<<"Case #"<<uu<<": IMPOSSIBLE"<<endl;
			return;
		}
		cout<<"Case #"<<uu<<": ";
		for (int i=0; i<p; i++) cout<<"P";
		for (int i=0; i<r; i++) cout<<"R";
		for (int i=0; i<s; i++) cout<<"S";
		cout<<endl;
		return;
	}
	if (!check(r, p, s)){
		cout<<"Case #"<<uu<<": IMPOSSIBLE"<<endl;
		return;
	}
	vector <int> t;
	t.push_back(r);
	t.push_back(p);
	t.push_back(s);
	vector <int> res= cons(t);
	cout<<"Case #"<<uu<<": ";
	for (int i=0; i<res.size(); i++) cout<<itc(res[i]);
	cout<<endl;


}

int main() {
	// your code goes here
	int t;
	cin>>t;
	for (uu=1; uu<=t; uu++){
		id[1]= 2;
		id[2]= 1;
		id[3]= 3;
		solve();
	}
	return 0;
}
