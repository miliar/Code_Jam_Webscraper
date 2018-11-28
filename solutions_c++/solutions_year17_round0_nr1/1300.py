#include <iostream>
#include <string>
#include <set>
using namespace std;
string s;
int n,k,t;
int main() {
	cin>>t;
	for(int T = 1; T<=t; T++){
	    int ans = 0;
		cin>>s>>k;
		n = s.size();
		set<int> flips;
		for(int i = 0; i<n; i++){
		    set<int> nflips;
		    for(int j : flips){
		        if(j<k) nflips.insert(j+1);
		    }
		    flips = nflips;
		    if(s[i]=='-'){
		        //odd
		        if(flips.size()%2==0){
		            ans++;
		            flips.insert(1);
		        }
		    }
		    else{
		        //even
		        if(flips.size()%2==1){
		            ans++;
		            flips.insert(1);
		        }
		    }
		}
		set<int> nflips;
	    for(int j : flips){
	        if(j<k) nflips.insert(j+1);
	    }
	    flips = nflips;
	    if(flips.size()){
	        cout<<"Case #"<<T<<": "<<"IMPOSSIBLE"<<endl;
	    }
	    else{
		    cout<<"Case #"<<T<<": "<<ans<<endl;
	    }
	}
	return 0;
}