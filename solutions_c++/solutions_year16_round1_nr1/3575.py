#include <bits/stdc++.h>
using namespace std;

string s,dau,cuoi;
vector<int> a[30];

int main() {
	freopen("input.inp","r",stdin);
	freopen("output.out","w",stdout);
	int test;
	scanf("%i\n",&test);
	for(int dem=1;dem<=test;dem++) {
		printf("Case #%i: ",dem);
		getline(cin,s);
		dau="";
		cuoi="";
		for(int ch=0;ch<=26;ch++) a[ch].clear();
		for(int i=0;i<s.length();i++) 
			a[s[i]-'A'].push_back(i);
		int ht=s.length()-1;
		for(char ch='Z';ch>='A';ch--) 
			while (!a[ch-'A'].empty()) {
				if (a[ch-'A'].back()<=ht) {
					while (ht>a[ch-'A'].back()) {
						cuoi=s[ht]+cuoi;
						ht--;
					}
					dau=dau+s[a[ch-'A'].back()];
					ht=a[ch-'A'].back()-1;
					//cout<<ht<<" ";
				}
				a[ch-'A'].pop_back();
			}
		cout<<dau<<cuoi<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}