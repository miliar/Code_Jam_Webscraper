#include<iostream>
using namespace std;
int main(){
	int l,j=0;
	cin>>l;
	int r[l];
	while(j<l){
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
	for(j=0;j<l;j++){
		cout<<"Case #"<<j+1<<": "<<r[j]<<endl;
	}
	return 0;
}
