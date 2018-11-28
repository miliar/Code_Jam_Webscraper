#include <iostream>
 using namespace std;
 
int main()
 {int T,a[4][4],b[4][4],i1,i2,count,num,i,j,k;
	 cin>>T;
	 
	 for(i=1;i<(T+1);i++)
	 {count=0;
	  cin>>i1;
		 for(j=0;j<4;j++)
		  for(k=0;k<4;k++)
		  cin>>a[j][k];
	  cin>>i2;
		 for(j=0;j<4;j++)
		  for(k=0;k<4;k++)
		  cin>>b[j][k]; 
		
	  for(j=0;j<4;j++)
	    for(k=0;k<4;k++)
	    {if(a[(i1-1)][j]==b[(i2-1)][k]){count++;num=a[(i1-1)][j];}
			}
			cout<<"Case #"<<i<<": ";
		if(count > 1){cout<<"Bad magician!"<<endl;}
		else if(count == 1){cout<<num<<endl;}
		else {cout<<"Volunteer cheated!"<<endl;}	
	
	
	}
	 return 0;
	 }
