#include <bits/stdc++.h>

using namespace std;

int main(){
	int i,_case,test,need,len,total,temp;
	string people;
	cin>>test;
	//i = shyness level and index
	//people[i] = number of people
	_case = test;
	while(test--){
		cin>>len>>people;
		if(len==0){
			cout<<"Case #"<<(_case-test)<<": 0"<<endl;
		}
		else{
			i=1;total=0;need=0;temp=0;
			while(i<=len){
				total+=(people[i-1]-'0');
				temp=need;
				if(total<i)need+=(i-total);
				total+=(need-temp);
				i++;
			}
			cout<<"Case #"<<(_case-test)<<": "<<need<<endl;
		}
		need=0;total=0;
	}
}