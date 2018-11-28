#include<iostream>
#include<cstring>

using namespace std;


int main(){
	int t,sum;
	char *s;
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	cin>>t;
	for(int i=0;i<t;i++)
	{
		sum=0;
		scanf(" %s ",s);
		for(int j=1;j<strlen(s);j++)
			if(s[j]=='-' && s[j-1]=='+')
				sum+=2;
		if(s[0]=='-')
			sum++; 
		cout<<"Case #"<<(i+1)<<": "<<sum<<endl;
	}
	
	return 0;
}