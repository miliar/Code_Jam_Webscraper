#include<iostream>
#include<string.h>
using namespace std;
int main(){
	int smax,t,count,sum;
	string s;
	cin>>t;
	for(int i1=0;i1<t;i1++){
		cin>>smax;
		count=0;
		sum = 0;
		cin>>s;
		int *arr;
		arr = new int[smax+1];
		for(int i=0;i<smax+1;i++){
			arr[i] = int(s[i])-48;
			if((sum-i) < 0){
				count = count + i-sum;
				sum = arr[i] + i;
			}
			else{
				sum = sum + arr[i];
			
			}
		
		}
		
		cout<<"Case #"<<i1+1<<": "<<count<<endl;
	}
	
}
