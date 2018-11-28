#include <iostream>
using namespace std;

int main() {
	// your code goes here
    long long int t,k,c,i,j,s;
    cin>>t;
    int r=1;
    while(r<=t)
    {
    	cin>>k>>c>>s;
    	long long int a[c][k];
    	for(i=0;i<k;i++)
    	{
    		a[0][i]=i+1;
    	}
    	for(i=1;i<c;i++)
    	{
    		for(j=0;j<k;j++)
    		{
    			a[i][j]=a[i-1][k-1]*j+a[i-1][j];
    			//cout<<a[i][j]<<" ";
    		}
    		//cout<<"\n";
    	}
    	cout<<"Case #"<<r<<": ";
    	for(i=0;i<k;i++)
    	  {cout<<a[c-1][i]<<" ";}
    	  cout<<"\n";
    	r++;
    }
	return 0;
}