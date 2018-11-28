#include<bits/stdc++.h>
using namespace std;
int modulo[66000][11][33];
int N=32;
int counter=0;
const int MAXN = 65800;
vector<int> v[555];
string ans[555];
bool check(int num, int base, string &X) {
	string to="";
	while(num!=0) {
		int val=num%base;
		to+=val+48;
		num/=base;
	}
	reverse(to.begin(),to.end());
	for(int i=0;i<(int)to.size();i++) {
		if(to[i]!=X[i]) return false;
	}
	if((int)to.size()!=(int)X.size()) return false;
	return true;
}
void go(int idx, string st) {
	if(counter>=500) return;
	if(idx==1 or idx==N) return go(idx+1,st+'1');
	if(idx==N+1) {
		bool z=true;
		for(int i=2;i<=10;i++) {
			bool f=false;
			for(int j=2;!f and j<MAXN;j++) {
				int sum=0;
				for(int k=N-1;k>=0;k--) if(st[k]=='1') sum+=modulo[j][i][N-k-1];
				sum%=j;
				if(sum==0) {
					v[counter].push_back(j);
					if(check(j,i,st)) break;
					f=true;
					break;
				}
			}
			if(!f) {
				z=false;
				break;
			}				
		}
		if(z) ans[counter]=st,counter++;
		else v[counter].clear();
		return;
	}
	go(idx+1,st+'0');
	go(idx+1,st+'1');
}
int main() {
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cout<<"Case #1:"<<endl;
	for(int i=2;i<=10;i++) for(int j=0;j<=0;j++) for(int k=2;k<MAXN;k++) modulo[k][i][j]=1;
	for(int i=2;i<=10;i++) for(int j=1;j<32;j++) for(int k=2;k<MAXN;k++) modulo[k][i][j]=(modulo[k][i][j-1]*i)%k;
	string st="";
	go(1,st);
	for(int i=0;i<500;i++) {
		cout<<ans[i]<<" ";
		for(int j=0;j<(int)v[i].size();j++) {
			if(j!=0) cout<<" ";
			cout<<v[i][j];
		}
		cout<<endl;
	}
	return 0;
}
