#include <iostream>
#include <cstring>
#include <cmath>



using namespace std;




int main(){

	int tc;
	int k,c,s;
	cin>>tc;
	for(int i = 0; i < tc; i++){
		cin>>k>>c>>s;
		cout<<"Case #" + to_string(i+1)<<": ";
		if(k == s){

			for(int j = 1; j <= k; j++){
				cout<<j<<" ";
			}
			cout<<endl;
		}
		else{
			cout<<"IMPOSSIBLE"<<endl;
		}

		
    }

}

