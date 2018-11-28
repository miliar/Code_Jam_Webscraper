//B
//Code Jam 2016
#include <bits/stdc++.h>
using namespace std;
int rec(string s,int depth){
	int i;
	//cout<<s<<endl;
	//getchar();
	for (i = (int)s.size()-1; i>=0 ; i--)
	{
		if(s[i]=='-')break;
	}
	if(i==-1){
		return depth;
	}
	int j;
	char p = (s[0]=='+'?'-':'+');
	for (j = 0; j <= i; j++)
	{
		if(s[j]==p){
			break;
		}
	}
	for (int k = 0; k < j; k++)
	{
		s[k]=p;
	}
	return rec(s,depth+1);
}
int main(){
	int t,t1;
	cin>>t;
	t1=t;
	getchar();
	while(t--){
		cout<<"Case #"<<t1-t<<": ";
		string s;
		cin>>s;
		cout<<rec(s,0);
		cout<<endl;
	}
	return 0;
}
