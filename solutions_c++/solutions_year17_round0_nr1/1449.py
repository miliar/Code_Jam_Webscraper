#include <bits/stdc++.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	long long T, cas, K, i, ans, j;
	string s;
	cin >> T;
	for(cas=1;cas<=T;cas++){
	    cout << "Case #"<< cas << ": ";
        cin >> s >> K;
        ans = 0;
        for(i=0;i<=s.size()-K;i++){
            if(s[i]=='-'){
                for(j=0;j<K;j++){
                    if(s[i+j]=='+') s[i+j] = '-';
                    else s[i+j] = '+';
                }
                ans++;
            }
        }
        for(i=s.size()-K+1;i<s.size();i++){
            if(s[i]=='-') break;
        }
        if(i<s.size()) cout << "IMPOSSIBLE\n";
        else cout << ans << '\n';
	}
	return 0;
}
