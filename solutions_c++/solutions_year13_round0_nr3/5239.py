#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int t,a,b,l=1,p=0,i;
	int c[5]={1,4,9,121,484};
freopen("input1.txt","r",stdin);
		freopen("output1.txt","w",stdout);
          std:cin>>t;
	      while(l<=t)
	      {
		      p=0;
		      cin>>a>>b;
		      cout<<"Case #"<<l<<":";
		      for(i=0;i<5;i++)
		      {
			      if(c[i]>=a&&c[i]<=b)
				      p++;
		      }
		      cout<<" "<<p<<"\n";
		      ++l;
	      }
	      return 0;
}
