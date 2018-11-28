#include<iostream>
#include<cmath>
#include<string>
#include<vector>
#include<Algorithm>
#include <fstream> // You should include this library
using namespace std;
int main()
{
     freopen("Input.txt","r",stdin); // For reading input
	  freopen("Output file path","w",stdout); // for writing output
     
     // Use normal cin and cout for reading from files after adding these lines.
	 int t,n,m,d,x;
	 int a[4][4],b[4][4];
	 cin>>t;
	 for(x=1;x<=t;x++)
	 {
	 cin>>n;
	 for(int i=0;i<4;i++)
	 { 
	  for(int j=0;j<4;j++)
	  {
	    cin>>a[i][j];
	  
	  }
	 }
	 int z=0;
	 cin>>m;
	 for(int i=0;i<4;i++)
	 { 
	  for(int j=0;j<4;j++)
	  {
	    cin>>b[i][j];
	  
	  }
	 }
	 for(int i=0;i<4;i++)
	 {
		 for(int j=0;j<4;j++)
	  { if(a[n-1][i]==b[m-1][j])
	   {
	     z++;
		 d=a[n-1][i];
	   }
	 
		 }}
	
	 if(z==0)
	 {
	 cout<< "Case #"<<x<<": Volunteer cheated!";
	 cout<<endl;
	 
	 }
	 else if(z==1)
	 {
	  cout<<"Case #"<<x<<": "<<d;
	   cout<<endl;
	  
	 }
	 else
	 {
	   cout<< "Case #"<<x<<": Bad magician!";
	    cout<<endl;
	 
	 }
	 }

}
