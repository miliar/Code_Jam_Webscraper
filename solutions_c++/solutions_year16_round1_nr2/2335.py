#include <iostream>
#include <string>
#include <algorithm>


using namespace std;

int ss[55][55];
int ans;
int mmp[3000];

void solve(int n){
	
	int i,J,k;
	for(i=0;i<3000;i++) mmp[i]=0;
	
	k=n*2-1;
	for(i=0;i<k;i++)
		for(J=0;J<n;J++)
			mmp[ss[i][J]]++;
			
	for(i=0;i<2501;i++)
		if(mmp[i]>0&&mmp[i]%2) 
			cout  <<" " << i;
	cout<<endl;
}


int main() {
	int t, n, m;
	
	
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
      cin >> n;
      int cnt=n*2-1;
      for(int J=0;J<cnt;J++){
      	
      	for(int m=0;m<n;m++)
      		cin >> ss[J][m];
	  }
      
      
    cout << "Case #" << i << ":";
    solve(n);
    
    //cout<<"cnt "<<cnt;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }

}
