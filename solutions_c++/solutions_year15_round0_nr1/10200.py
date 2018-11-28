#include <iostream>
#include <string>
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	int t,smax,x,min,temp,j=1;
	string s;
	cin>>t;
	while(t--){
		min=0;
		cin>>smax>>s;
		temp=0;
		for(int i=0;i<smax;i++){
			temp+=int(s[i])-48;
			if(temp<i+1 && int(s[i+1])!=48){
				min=min+(i+1)-temp;
				temp=temp+min;
			}
		}
		cout<<"Case #"<<j<<": "<<min<<endl;
		j++;
	}
}