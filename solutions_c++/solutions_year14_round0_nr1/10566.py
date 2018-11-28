#include<iostream>

using namespace std;

int main()
{

  int T;
  cin>>T;
  int i,r,j;
  int r1,r2;
  int arr1[4][4],arr2[4][4];

  if(T<0||T>100)
    { cout<<"limits crossed as T should be less 100 and more than 0"<<endl;
    }
  else
    {

  for(i=0;i<T;i++)
    {
       int count=0;
       int col=0;
       int index;
      cin>>r1;
      for(r=0;r<4;r++)
	{
	  for(j=0;j<4;j++)
	    {
	      cin>>arr1[r][j];
	    }
	  cout<<endl;

	}
      cin>>r2;

      for(r=0;r<4;r++)
	{
	  for(j=0;j<4;j++)
	    {
	      cin>>arr2[r][j];
	    }
	  cout<<endl;

	}

 
      while(col<4)
	{
	  
      for(j=0;j<4;j++)
	 {
	   if(arr1[r1-1][col]==arr2[r2-1][j])
	     {
	       count+=1;
	       index=col;

	      }
	   
	  }
	   col+=1;
	 }
	

    
      //Answer

      if(count==1)
	{
	  cout<<"Case #"<<i+1<<": "<<arr1[r1-1][index];
	  
	}
      else if(count==0)
	{
	  cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!";
	}
      else
	{
	  cout<<"Case #"<<i+1<<": "<<"Bad magician!";
	  
	}
    }
    }
      return 0;

}
