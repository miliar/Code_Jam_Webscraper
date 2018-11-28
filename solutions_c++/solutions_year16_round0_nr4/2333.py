#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<map>
#include<algorithm>
#include<vector>
#include<queue>
#include<ctime>
using namespace std;
typedef long long ll;
bool used[10000000];
ll pri[10000000];
int n_pri;
void deal() {
	ll k,c,s;
	cin>>k>>c>>s;
	for(int i=1;i<=k;++i)
		cout<<" "<<i;
	cout<<endl;
}
void openFile() {
	freopen("D-small-attempt0.out","w", stdout);
	freopen("D-small-attempt0.in","r",stdin);
}
int main() {
	int t;
	openFile(); 
	cin>>t;
	for(int i=0;i<t;++i) {
		cout<<"Case #"<<i+1<<":";
		deal();
	}
}