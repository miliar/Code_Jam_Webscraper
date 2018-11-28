#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<set>
#include<map>
#include<queue>
#include<cstring>
#include<stack>
#include<fstream>
using namespace std;
int main(){
	ifstream cin;
	ofstream cout;
	cin.open("C:\\Users\\hp\\Downloads\\7.in");
	cout.open("C:\\Users\\hp\\Downloads\\out.txt");
	int t,i,q=1;
	cin>>t;
	while(t--){
	int x,r,c;
	cin>>x>>r>>c;
	if(x==1)
	cout<<"Case #"<<q<<": "<<"GABRIEL"<<endl;
	else if(x==2&&(r*c/x)>=1){
	if(r*c%x==0)	
	cout<<"Case #"<<q<<": "<<"GABRIEL"<<endl;
	else
	cout<<"Case #"<<q<<": "<<"RICHARD"<<endl;
	}
	else if(x==3&&(r*c/x)>=2)
	{
	if(r*c%x==0)	
	cout<<"Case #"<<q<<": "<<"GABRIEL"<<endl;
	else
	cout<<"Case #"<<q<<": "<<"RICHARD"<<endl;
	}
	else if(x==4&&(r*c/x)>=3)
	{
	if(r*c%x==0)	
	cout<<"Case #"<<q<<": "<<"GABRIEL"<<endl;
	else
	cout<<"Case #"<<q<<": "<<"RICHARD"<<endl;
	}
	else
	cout<<"Case #"<<q<<": "<<"RICHARD"<<endl;
	q++;
	}
	return 0;
}