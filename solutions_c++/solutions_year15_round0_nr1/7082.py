#include <iostream>
#include <cstring>

using namespace std;

main(){
	int t;
	cin>>t;
	for(int j=1;j<=t;j++){
		int s;
		char shy[1003];
		cin>>s>>shy;
		int total=shy[0]-48,req=0;
		for(int i=1;i<=s;i++){
			if(total<i && shy[i]!='0'){
				req+=(i-total);
				total+=(i-total);
			}
			total+=shy[i]-48;
		}
		cout<<"Case #"<<j<<": "<<req<<endl;
	}
	
}