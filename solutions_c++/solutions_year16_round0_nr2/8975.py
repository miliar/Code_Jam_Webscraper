#include <iostream>
using namespace std;

int t,sze,res;
string arr;
int it,cnt;
int main(){

	cin>>t;
	for(int zz=1;zz<=t;zz++){
		cin>>arr;
		sze = arr.size();
		it = cnt = 0;
		
		if(arr[it] == '+'){
			while(it < sze){
				while(arr[it] == '+' && it < sze) it++;
				if(it == sze)	cout<<"Case #"<<zz<<": "<<cnt<<endl;
				else{
					cnt+=2;
					while(arr[it] == '-' && it < sze) it++;
					if(it == sze){
						cout<<"Case #"<<zz<<": "<<cnt<<endl;
					}
				}
			}
		}else{
			while(it<sze){
				while(arr[it] == '-' && it < sze) it++;
				while(arr[it] == '+' && it < sze) it++;
				if(it == sze)	cout<<"Case #"<<zz<<": "<<cnt+1<<endl;
				else cnt += 2;
			}
		}
	}
	return 0;
}