#include<bits/stdc++.h>
using namespace std;
int main() {
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int t,cases=0;
	cin >> t;
	string s;
	while(t--) {
		cin >> s;
		bool flag=false;
		int l=0;
		long cnt=0;
		int r=s.length()-1;
		while(l<=r) {
			if(l==r) {
				if((flag && s[l]=='+')||(!flag && s[l]=='-'))
					cnt++;
				break;
			}
			if(!flag) {
				if(s[r]=='-') {
					flag=true;
					cnt++;
					if(s[l]=='+')
					{
						cnt=cnt+1;
						while(l<r && s[l]=='+')
							l++;
					}
				}
				else {
					r--;
				}
			}
			else {
				if(s[l]=='+') {
					flag=false;
					cnt++;
					if(s[r]=='-') {
						cnt=cnt+1;
						while(r>l && s[r]=='-') {
							r=r-1;
						}
					} 
				}
				else {
					l++;
				}
			}
		}
		cout << "Case #" << ++cases << ": " << cnt << endl;
	}
	//fclose(stdout);
	return 0;
}	
