#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for(int i=0; i<(n); i++)
#define rrep(i, n) for(int i=n; i>=0; i--)
#define pb push_back
#define gline(s) getline(cin, s)
int find(int *a, int no){
	int max=-1, pos=-1;
	rep(i, no){
		if(a[i] > max){
			max=a[i];
			pos=i;
		}
	}
	if(max==0){
		return -1;
	}
	else
	return pos;
}
bool  calt(int *a, int no, int sum){
	rep(i, no){
		if(a[i]/(double)sum >= 0.50){
			return false;
		}
	}
	return true;
}
void solve(){
	int no;
	cin >> no;
	int a[no];
	int sum=0;
	rep(i, no){
		cin >> a[i];
		sum+=a[i];
	}
	int max=find(a, no);
	string line="";
	while(max !=-1){
		a[max]--;
		sum--;
		line+= char(max+'A');
		if(calt(a, no, sum)|| line.size()==2 || sum==2){
			cout << line << " "; 
			line="";
		}
		max=find(a, no);
	}
	cout << endl;
}
main(){
	freopen("A.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	rep(i, t){
		cout << "Case #" << i+1 << ": " ;
		solve();
	}
}
