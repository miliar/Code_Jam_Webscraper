#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        int n,row,column;
        string str;
        cin>>n>>row>>column;
        row>column?row=row+column-(column=row):row=row;
	if(n==1)
	{
		str="GABRIEL\n";
	}
	else if(n==2)
	{
		if((row==1&&(column==1||column==3))||(column==3&&row==3))
			str="RICHARD\n";
		else str="GABRIEL\n";
	}
	else if(n==3)
	{
		if((row==2&&column==3)||(row==3&&(column==3||column==4)))
			str="GABRIEL\n";
		else str="RICHARD\n";
	}
	else if(n==4)
	{
		if(column==4&&(row==3||row==4))
			str="GABRIEL\n";
		else str="RICHARD\n";
	}
    	cout<<"Case #"<<j<<": "<<str;
    }
    return 0;
}
