#include<iostream>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("myfile.txt","w",stdout);
	long long t,l,q,i,j;
	string si;
 	cin>>t;
 	int aa=1;
 	for(j=0;j<t;j++)
 	{
 		int q=0;
 		cin>>si;
 		l=si.length();
 		for(i=0;i<l-1;i++)
 		{
 			if(si[i]!=si[i+1])
 			q++;
 		}
 		if(si[l-1]=='+')
 		cout<<"Case "<<"#"<<aa<<": "<<q<<endl;
 		else
 		cout<<"Case "<<"#"<<aa<<": "<<q+1<<endl;
 		aa++;
 	}




}

