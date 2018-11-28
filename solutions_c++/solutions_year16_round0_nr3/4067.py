#include <bits/stdc++.h>
using namespace std;

int n,sl;
string s;

long long doi(int k) {
	long long res=0, ht=1;
	for(int i=7;i>=0;i--) {
		if (s[i]=='1') res+=ht;
		ht*=k;
	}
	return res;
}

void cal(int k) {
	if (sl==0) return;
	if (k==7) {
		cout<<s<<s<<" ";
		for(int i=2;i<=10;i++) cout<<doi(i)<<" ";
		cout<<"\n";
		--sl;
		return;
	}
	s[k]='0';
	cal(k+1);
	s[k]='1';
	cal(k+1);
}

int main() {
	freopen("input.inp","r",stdin);
	freopen("output.out","w",stdout);
	int test;
	scanf("%i\n",&test);
	for(int dem=1;dem<=test;dem++) {
		printf("Case #%i:\n",dem);
		cin>>n>>sl;
		s.resize(8,'0');
		s[0]='1';
		s[7]='1';
		cal(1);
	}
	fclose(stdin);
	fclose(stdout);
}