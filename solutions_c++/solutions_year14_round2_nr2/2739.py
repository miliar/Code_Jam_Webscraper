#include<iostream>
#include <algorithm> 
#include <fstream>
#include <iomanip>
using namespace std;
int main()
{
	ifstream cin;
    ofstream cout;
    cin.open ("B-small-attempt1.in");
    cout.open("output.txt");
    int a,b,k,t,n,l,i,j;
	long long count;
	cin>>t;
	for(i=1;i<=t;i++)
	{		
	    cin>>a>>b>>l;
	    count=0;
	    for(j=0;j<a;j++)
	    {
	    	for(k=0;k<b;k++)
	    	{
	    		 if((j&k)<l)
	    		 {
	    		 	count++;
	    		 }
	    	}
	    }
	   cout<<"Case #"<<i<<": "<<count<<endl;
	}
}
