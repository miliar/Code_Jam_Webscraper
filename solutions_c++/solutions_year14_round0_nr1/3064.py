#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int main() {
  int t,x,y,i,j,count,n;
  int in;
  int card1[17],card2[17],card3[17];
  cin>>t;
  n=t;
  while(t--)
  {
	  count=0;
	  for(i=1;i<=16;i++)
		  card3[i]=0;
	  cin>>x;
	  for(i=1;i<=16;i++)
	  {
		  cin>>card1[i];
	  }
	  cin>>y;
	  for(i=1;i<=16;i++)
	  {
		  cin>>card2[i];
	  }
	  for(i=4*(x-1)+1;i<=4*x;i++)
	  {
		  for(j=4*(y-1)+1;j<=4*y;j++)
		  {
			  if(card1[i]==card2[j])
			  {
				  card3[card1[i]]++;
				  count++;
			  }
		  }
	  }
	  cout<<"Case #"<<n-t<<": ";
	  if(count==0)
	  {
		  cout<<"Volunteer cheated!"<<endl;
	  }
	  else if(count>1)
	  {
		  cout<<"Bad magician!"<<endl;
	  }
	  else
	  {
		  for(i=1;i<=16;i++)
		  {
			  if(card3[i])
			  {
				  in=i;
			  }

		  }
		  cout<<in<<endl;
	  }
  }
  return 0;

}
