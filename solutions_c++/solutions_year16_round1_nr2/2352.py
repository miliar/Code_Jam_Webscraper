#include<iostream>
using namespace std;
int main()
{ long int t,j;
cin>>t;
 for(j=1;j<=t;j++)
  {  long int n,a[2501]={0},k,i,x,b[51]={0};
    cin>>n;
    for(i=0;i<2*n-1;i++)
      for(k=0;k<n;k++) 
       { cin>>x;
        a[x]++; }
     k=0;
	for(i=1;i<=2500;i++)
	  if(a[i]%2)
	   b[k++]=i;
	cout<<"Case #"<<j<<": "; 
	for(i=0;i<n;i++)
	 cout<<b[i]<<" ";
	 cout<<endl;       
}
}