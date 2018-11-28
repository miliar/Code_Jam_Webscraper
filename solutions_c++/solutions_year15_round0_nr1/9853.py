#include<iostream>
using namespace std;
int main(){
	int t,j=0;
	cin>>t;
	int r[t];
	while(j<t){
		int i,max,result=0,sum=0;
		cin>>max;
		char s[max+1];
		cin>>s;
		for(i=0;s[i]!='\0';i++){
			if(s[i]!='0'){
				if(i > sum){
					result += i-sum;
					sum +=result;
				}
				sum += s[i]-'0';
			}
		}
		r[j]=result;
		j++;
	}
	for(j=0;j<t;j++){
		cout<<"Case #"<<j+1<<": "<<r[j]<<endl;
	}
	return 0;
}
