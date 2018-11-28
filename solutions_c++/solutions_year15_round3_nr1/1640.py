#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <cmath>

using namespace std;


int main(){
	int t;
	cin>>t;
	for(int h=0;h<t;h++){
		long long r,c,w,ans;		
		cin>>r>>c>>w;
		if(w==1){
			ans = r*c;
		}
		else if(w==c){
			ans = r + (w-1);
		}
		else{
			ans = w-1;
			ans += r*ceil((c*1.0)/(w));
		}	
		cout<<"Case #"<<(h+1)<<": "<<ans<<endl;
	}
}
