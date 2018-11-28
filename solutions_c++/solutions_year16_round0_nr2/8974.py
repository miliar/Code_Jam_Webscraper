#include <iostream>
#include <string>
using namespace std;
void flip(string &s,int c2){
	for (int i = 0; i < c2; ++i)
	{
		if(s[i]=='+')
			s[i]='-';
		else if(s[i]=='-')
			s[i]='+';
		/* code */
	}
}
bool check(string s,int len){
	for (long int i = 0; i < len; ++i)
	{
		/* code */
		if(s[i]=='-')
			return true;
	}
	return false;
}
int main(){
	long int  t,c1=0,c2=0,i,j,k,len;
	string s;
	long int count=0;
	cin>>t;
	for(int l=1;l<=t;l++){
		count=0;
		cin>>s;
		len=s.size();
		while(check(s,len)){
			for ( i = 0; i < len; ++i)
			{
					if (s[i]=='-')
					{
						k=i;
						while(s[k]!='+'&&k<len){
							k++;
						}
						flip(s,k);
						count++;
					}
			}
		}
		cout<<"Case #"<<l<<": "<<count<<endl;
	}
}
