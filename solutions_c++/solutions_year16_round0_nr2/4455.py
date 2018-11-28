#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for(int p=0;p<t;p++){
        string s;
        cin >> s;
        int ans=0;
        int len=s.length();
        int plus=0;
        for(int i=0;i<len;i++){
            int flag=0;
            if(s[i]=='+'){
                plus++;
            }
            while(i<len && s[i]=='-'){
                i++;
                flag=1;
            }
            if(flag==1 && plus==0){
                ans++;
                plus++;
            }
            else if(flag==1 && plus!=0){
                ans+=2;
                plus++;
            }
        }
        cout << "Case #" << p+1 << ": " << ans << endl;
    }
	// your code goes here
	return 0;
}
