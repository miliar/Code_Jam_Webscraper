#include <bits/stdc++.h>
using namespace std;

const int MAXW = (1<<21);

bool mark[MAXW];
int C,D,V;
int last[MAXW];

void add (int x){
	for (int i=0; i<x; i++)
		last[i] = 0;
	for (int i=x; i<MAXW; i++) 
		if (mark[i]==false && mark[i-x]==true && last[i-x]+1 <= C){
			last[i] = last[i-x] + 1;
			mark[i] = true;
		}else
			last[i] = 0;
}

void main2(){
	cin >> C >> D >> V;
	memset(mark,0,sizeof mark);
	mark[0] = true;
	for (int o=0; o<D; o++){
		int x; cin >> x; add(x);
	}
	int ans = 0;
	long long i = 0;
	for (i=1; i<MAXW; i++) if (!mark[i]){
		if (V < i){
			cout << ans << endl;
			return;
		}
		ans++;
		add(i);
	}
	cout << ans << endl;
}

int main(){
	int t; cin >> t;
	for (int o=1; o<=t; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
