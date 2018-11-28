#include <bits/stdc++.h>
using namespace std;

int n;
string s;

int main() {
	freopen("input.inp","r",stdin);
	freopen("output.out","w",stdout);
	int test;
	scanf("%i\n",&test);
	for(int dem=1;dem<=test;dem++) {
		printf("Case #%i: ",dem);
		getline(cin,s);
		n=s.length();
		int res=0;
		if (s[0]=='-') res=1;
		for(int i=1;i<n;i++) 
			if (s[i]=='-' && s[i-1]=='+') res+=2;
		cout<<res<<"\n";
	}
	fclose(stdin);
	fclose(stdout);
}