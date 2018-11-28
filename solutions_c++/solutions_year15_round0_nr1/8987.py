#include <iostream>
#include <string>
using namespace std;

int main(){
	int t;
	cin>>t;
	for (int i=1; i<= t; i++){
		int smax; 
		string shy;
		cin>>smax>>shy;
		int ans = 0;
		int count = 0;
		for (int j = 0; j< smax+1; j++){
			int curr_num = shy[j] - '0';
			
			if (count < j){
				int new_friends = j - count;
				ans += new_friends;
				count += new_friends;
			}
			count+= curr_num;
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
}