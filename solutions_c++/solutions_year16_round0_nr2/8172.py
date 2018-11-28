#include<cstdio>
#include<iostream>
#include<utility>
#include<cstring>

using namespace std;

int func1(int);
int func2(int);

char str[200];

int func1(int loc){
	if(loc==1){
		if(str[loc]=='+')
			return 0;
		else
			return 1;
	}
	if(str[loc]=='+')
		return func1(loc-1);
	else
		return 1+func2(loc-1);
}

int func2(int loc)
{
	if(loc==1){
		if(str[loc]=='-')
			return 0;
		else
			return 1;
	}
	if(str[loc]=='-')
		return func2(loc-1);
	else
		return 1+func1(loc-1);
}

int main()
{
	int T;
	freopen("IN.in","r",stdin);
	freopen("Output.txt","w",stdout);

	cin>>T;
	for(int t=1;t<=T;t++){
		cin>>(str+1);
		cout<<"Case #"<<t<<": "<<func1(strlen((str+1)))<<endl;
	}
	return 0;
}