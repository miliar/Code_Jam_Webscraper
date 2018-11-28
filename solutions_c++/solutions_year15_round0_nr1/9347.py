#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

int main(){

ios::sync_with_stdio(false);

 long int test,smax,value;
 string sv;

cin>>test;

for(int j=0;j<test;j++){
	
	cin>>smax;
	cin>>sv;
	
	long int arr[(smax+1)],count=0,sum=0;
	
	for(int i=0;i<sv.length();i++){
		
			arr[i]=sv[i]-'0';
	}

	for(long int i=0;i<=smax;i++){
		
		if(i==0){
			
			if(arr[i]==0) count++;
		}
		else{
			
			sum+=arr[i-1];
			
			if(count+sum<i)	count+=i-(sum+count);
		}
	}
	
	cout<<"Case #"<<j+1<<": "<<count<<"\n";
	
}

return 0;
}

