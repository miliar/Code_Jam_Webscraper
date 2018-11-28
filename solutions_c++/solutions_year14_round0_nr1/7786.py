#include<stdio.h>
#include<iostream>
#include<vector>
#include<stack>
#include<algorithm>
using namespace std;
int main()
{
	int t,p=1;
	cin>>t;
	while(t--)
	{
		int ans1,ans2,one[4][4],two[4][4];
		cin>>ans1;
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		cin>>one[i][j];
		cin>>ans2;
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		cin>>two[i][j];
	    int count=0,element=0;
	    for(int i=0;i<4;i++)
	    for(int j=0;j<4;j++)
		{
	    	    if(one[ans1-1][i]==two[ans2-1][j])
	    		{
	    		element=one[ans1-1][i];
	    		count++;
	    	    }
	    }
	    if(count==1)
	    cout<<"Case #"<<p<<":"<<" "<<element<<"\n";
		else if(count==0)
		cout<<"Case #"<<p<<":"<<" "<<"Volunteer cheated!\n"; 
	    else
	    cout<<"Case #"<<p<<":"<<" "<<"Bad magician!\n";
		p++;	
	}
return 0;
}
