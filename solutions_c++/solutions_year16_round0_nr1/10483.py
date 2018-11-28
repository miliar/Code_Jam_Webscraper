#include <bits/stdc++.h>
using namespace std;
#define llp unsigned long long
#define ll long long

int main() {
	// your code goes here
	llp t, num, c = 1, i, a[10];
	cin>>t;
	while(t--){
	    for(i=0; i<10; i++)             //to store 10 values from 0 to 9 to false
	        a[i] = 0;
	    cin>>num;
	    if(num==0)
	        cout<<"Case #"<<c++<<": INSOMNIA\n";
	    else{
	        llp count = 0, r, temp, x, ans;
	        for(i=1; count<10; i++){    // loop to traverse form num*1 to num*... till we traverse from 0to9 in a[]
	            temp = i*num;           
	            x = temp;
	            while(temp>0){          // loop to traverse all digits
	                r = temp%10;
	                if(a[r]==0){        //condition to compare digits with a[]
	                    a[r] = 1;
	                    count++;
	                    if(count==10) ans = x;
	                }
	                temp = temp/10;
	            }
	        }
	        cout<<"Case #"<<c++<<": "<<ans<<endl;
	    }
	}
	return 0;
}