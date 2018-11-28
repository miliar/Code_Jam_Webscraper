#include<bits/stdc++.h>

using namespace std;

string s;

int main() {
  int T, caso = 0;
  scanf("%d",&T);
  while (T--) {
	cin>>s;
	int n = s.size(); 
	char c = s[0];
	int ans = 0;
	for(int i=0; i<n-1; ++i) {
	  if (s[i+1] != c) {
		c = s[i+1];
		++ans;
	  }
	}
	if (c == '-')++ans;
	printf("Case #%d: %d\n", ++caso, ans);
  }
}