#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for(int p=0;p<t;p++){
        string s,ans="";
        cin >> s;
        int len=s.length();
        ans+=s[0];
        char first=s[0],last=s[0];
        for(int i=1;i<len;i++){
            if(s[i]>first && s[i]>last){
                ans=s[i]+ans;
                first=s[i];
            }
            else if(s[i]<first && s[i]<last){
                ans=ans+s[i];
                last=s[i];
            }
            else if(s[i]==first){
                ans=s[i]+ans;
                first=s[i];
            }
            else if(s[i]==last){
                ans=ans+s[i];
                last=s[i];
            }
            else{
                ans=ans+s[i];
                last=s[i];
            }
        }
        cout << "Case #" << p+1 << ": " << ans << endl;
    }

	// your code goes here
	return 0;
}
