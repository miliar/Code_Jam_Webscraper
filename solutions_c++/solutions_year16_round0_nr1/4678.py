#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
string solveSheep(int n){
int left = 10;	
int tn=n;
int f[11];
int numb;
for(int i=0;i<10;i++) f[i]=0;


	while(1&&n!=0){
		int tmp=tn;
		while(tmp>0){
			numb=tmp%10;
                        if(f[numb]==0){

				f[numb]=1;
				left--;

                        }	
		        tmp/=10;
		}
		
		if(left==0) break;
		tn+=n;
	}

	

	string ans="INSOMNIA";
	if(left==0){
		ans="";
		while(tn>0){
			ans+=(tn%10+'0');
			tn/=10;
		}
		
		reverse(ans.begin(),ans.end());
	}

	return ans;

}


int main() {
	int t, n, m;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
      cin >> n;

    cout << "Case #" << i << ": " <<  solveSheep(n) << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }

}
