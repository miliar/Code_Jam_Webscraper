#include <iostream>
#include <string>
#include <algorithm>


using namespace std;



string solve(string ss){
	
	string ans="";
	
	int a[1005],i,dp[1005],J,len;
	
	len=ss.length();
	for(i=0;i<len;i++) a[i]=ss[i]-'A';
	
	dp[0]=a[0];
	for(i=1;i<len;i++){
		
		if(a[i]>=dp[0]){
		
			for(J=i;J>0;J--)
				dp[J]=dp[J-1];
			dp[0]=a[i];
		}
		else
			dp[i]=a[i];
		
	}
	
	for(i=0;i<len;i++)
		ans+=(dp[i]+'A');
	
	return ans;
	
}


int main() {
	int t, n, m;
	string ss;
	
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
      cin >> ss;
    cout << "Case #" << i << ": "<<solve(ss)<<endl;
    
    //cout<<"cnt "<<cnt;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }

}
