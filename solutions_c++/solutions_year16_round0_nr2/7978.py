#include <iostream>
#include <string>
using namespace std;

int main() {
	long long t, le, ans, i, j;
	string s;
	cin>>t;
	for(int i =1; i<=t; i++){
	    cin>>s;
	    ans=0;
	    le = s.size();
	    if(le>1)
	    for(j=1; j<le; j++){
	        if(s[j]!=s[j-1])
	            ans++;
	    }
	    if(s[le-1]=='-')
	        ans++;
	    cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}

