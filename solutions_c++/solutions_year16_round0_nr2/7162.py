#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("codejam2.txt","r",stdin);
	freopen("codejam2out.txt","w",stdout);
	int t;
	cin >> t;
	for(int tst = 1; tst <= t;tst++){
		printf("Case #%d: ",tst);
		string s;
		cin >> s;
		int cnt = 0;
		int neg = 0,pos = 0;
		int n = s.length();
		for(int i = 0; i < n; i++){
			if(s[i] == '+'){
				if(neg > 0){
					cnt++;
					neg = 0;
				}
				pos++;
				
			}
			else{
				if(pos > 0){
					cnt++;
					pos = 0;
				}
				neg++;
			}
		}
		if(neg > 0) cnt++;
		cout << cnt << endl;
	}
	return 0;
}

