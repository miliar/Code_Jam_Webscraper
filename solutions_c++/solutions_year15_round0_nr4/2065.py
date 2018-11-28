#include<bits/stdc++.h>
using namespace std;
typedef long long int LL;
#define sd(x) scanf("%d", &x)
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define ft first
#define sc second
#define INF 1000000000
#define MOD 10000007
int main()
{
	freopen("inp.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int t, cse;
	cin>>t;
	for (cse = 1; cse <= t; cse ++) {
		int x, r, c;
		cin>>x>>r>>c;
		if(r>c) swap(r,c);
		cout<<"Case #"<<cse<<": ";
		if (x==1) {
			cout<<"GABRIEL"<<endl;
		} else if (x==2) {
			if ((r*c)%2 == 0) {
				cout<<"GABRIEL"<<endl;
			} else {
				cout<<"RICHARD"<<endl;
			}
		} else if (x==3) {
			if ((r==3 || c==3) && (r!=1 && c!=1)) {
				cout<<"GABRIEL"<<endl;
			} else {
				cout<<"RICHARD"<<endl;
			}
		}
		else {
			if (c==4 &&(r==3||r==4))
				cout<<"GABRIEL"<<endl;
			else 
				cout<<"RICHARD"<<endl;
		}
	}
	return 0;
}
