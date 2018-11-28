#include <algorithm>
#include <vector>
#include <iostream>
#include <string>

using namespace std;

int main(){
	int t;
	cin>>t;
	for(int h=0;h<t;h++){
		int x,r,c;
		cin>>x>>r>>c;
		string ans= "GABRIEL";
		int area = r*c;
		if(x==2){
			if(area%2==1){
				ans= "RICHARD";
			}
		}
		else if(x==3){
			if(((r%2==0)&&(c%2==0))||(r==1||c==1)) {
				ans= "RICHARD";
			}
		}
		else if(x==4){
			if(!((r>=3 && c>=3) && area%2==0)){
				ans= "RICHARD";	
			}
		}
		cout<<"Case #"<<(h+1)<<": "<<ans<<endl;
	}
}
