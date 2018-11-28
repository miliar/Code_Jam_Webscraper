#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
	    char a[100];
	    cin>>a;
	    int count=0;
	    for(int j=strlen(a)-1;j>0;j--)
	    {
	        if(a[j]!=a[j-1])
	        count++;
	    }
	    if(a[strlen(a)-1]=='-')
	    count++;
	    cout<<"Case #"<<i<<": "<<count<<"\n";
	}
	return 0;
}

