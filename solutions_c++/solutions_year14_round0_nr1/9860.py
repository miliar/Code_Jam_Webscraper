#include<iostream>
#include<map>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int kk=1;kk<=t;kk++)
	{cout<<"Case #"<<kk<<": ";
		int g1,a[4][4],b[4][4],g2,co=0,flag=0,num;
		map<int,int>m;
		cin>>g1;
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
		cin>>a[i][j];
		if(i==g1-1)
		{
			m.insert (pair<char,int>(a[i][j],1));
		}
		}
		cin>>g2;
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++){
		
		
		cin>>b[i][j];
	    if(i==g2-1)
	    {
	    	
	    	if(m[b[i][j]]==1){co++;num=b[i][j];}
	
		}}
		if(co==1)
		cout<<num<<endl;
		else if(co==0)
		cout<<"Volunteer cheated!\n";
		else if(co>1)
		cout<<"Bad magician!\n";
	
}}
