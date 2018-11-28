#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int solveCake(string s){
	
	int ans=0,i;
	
	int d0[110],d1[110];
	
	if(s.at(0)=='-'){
		d0[0]=0;
		d1[0]=1;
	}
	else{
		d0[0]=1;
		d1[0]=0;
	}
	for(i=1;i<s.length();i++){
		
		if(s.at(i)=='-'){
			d0[i]=min(d0[i-1],(d1[i-1]+1));	
			d1[i]=d0[i]+1;
		}else
		{
			
			d1[i]=min((d0[i-1]+1),d1[i-1]);
		    d0[i]=d1[i]+1;
		}		
		
	}
	
	return d1[s.length()-1];

}

int main() {
	int t, n, m;
	string ss;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
      cin >> ss;
    cout << "Case #" << i << ": " <<  solveCake(ss) << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }

}
