#include<iostream>
#include<string.h>
#include<cstdio>
#include<map>
#include<vector>
#include<list>
#include<math.h>
using namespace std;
int main(){

	int kp,ans=0,counti=0;
	string str;
	cin>>kp;
	for(int t=1;t<=kp;t++){
		ans=0,counti=0;
		cin>>str;
		int i=str.length()-1,j=0;
		int p=0,q=0;
		while(str[i]!='/'){
			q+=(str[i]-'0')*pow(10,j);
			i--;j++;
		}
		i--;j=0;
		while(i>=0){
			p+=(str[i]-'0')*pow(10,j);
			j++;i--;
		}
		//cout<<p<<" "<<q<<endl;
		if(q%2==1 && q!=1)
			ans=1;
		while(p<q){
			q/=2;
			counti++;
			if(q%2==1 && q!=1)
				ans=1;
		}
		if(ans==0)
			cout<<"Case #"<<t<<": "<<counti<<endl;
		else
			cout<<"Case #"<<t<<": impossible"<<endl;
		
	}
	








	return 0;
}

