#include<iostream>
#include<vector>
using namespace std;

int main(int argc, char *argv[]) {
	int caseNo=1, i, t;
	cin>>t;
	while(t--) {
        string s;
        vector<char> cakes;
        int ans;
        cin>>s;
        for(i=s.size()-1; i>=0; i--)
            if(s[i] == '-') break;
        if(i==-1) ans = 0;
        else {
            for(; i>=0; i--)
                cakes.insert(cakes.begin(), s[i]);
            //cakes.reverse();
            ans=1;
            for(i=1; i<cakes.size(); i++) {
                if(cakes[i] == cakes[i-1]);
                else ans++;
            }
        }
        cout<<"Case #"<<caseNo++<<": "<<ans<<'\n';
    }
    return 0;
}
