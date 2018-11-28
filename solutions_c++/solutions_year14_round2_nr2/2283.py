//#pragma comment(linker, "/STACK:512000000")
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <stdlib.h>

using namespace std;

bool IsEq(string s1, string s2) {
	if (s1.size()!=s2.size()) return 0;
	for (int p=0;p<s1.size();++p)
		if (s1[p]!=s2[p]) return 0;
	return 1;
}

int main() {
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);

	int i,j,n,m,c,t,a,b,k;
	string st;
	vector<string> v,ans;
	bool f;

	cin>>t;

	j=0;
	while (j<t) {
		cin>>a>>b>>k;
		
		c=0;
		for (i=0;i<a;++i)
			for (m=0;m<b;++m)
				if ((i&m)<k) c++;

		cout<<"Case #"<<j+1<<": "<<c<<endl;
		j++;
	}

    return 0;
}