#include<iostream>
#include<cmath>
using namespace std;

int main()
{
  int i,n_case,cases,k,c,s;
  cin>>cases;
  cin.ignore();
  for(n_case=1;n_case<=cases;n_case++)
  {
	  cin>>k>>c>>s;
	  cout<<"Case #"<<n_case<<":";
	  for (i=1;i<=k;i++)
	  {
		  cout<<" "<<i;
	  }
	  cout<<endl;
  } 

  
  return 0;
} 
  
