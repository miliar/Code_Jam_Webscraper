#include<stdio.h>
#include<iostream>

using namespace std;
int main(){
  int T,t,row,row1,i,j,a[4][4],b[4][4],c[4],length=0;

  cin>>T;
  for(t=0;t<T;t++)
    {
length=0;
      cin>>row;
      row--;
      for(i=0;i<4;i++)
	{
	  for(j=0;j<4;j++)
	    cin>>a[i][j];
        }
      cin>>row1;
      row1--;
      for(i=0;i<4;i++)
	{
	  for(j=0;j<4;j++)
	    cin>>b[i][j];
        }
      for(i=0;i<4;i++)
	{
          for(j=0;j<4;j++)
	    {
	      if(a[row][i]==b[row1][j]){
		c[length]=a[row][i];
		length++;
	      }
	    }
	}
      cout << "Case #"<<t+1<<": ";
      if(length==1)
	{
	  cout<<c[length-1]<<endl;
	}
      if(length>1)
	{
	  cout<<"Bad magician!\n";
	}
      if(length==0)
	{
	  cout<<"Volunteer cheated!"<<endl;

	}
    }
  return 0;
}
