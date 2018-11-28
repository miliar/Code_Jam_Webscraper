#include<iostream>
using namespace std;

int main()
{
  int cse=0;
  cin>>cse;
  for(int c=1;c<cse+1;c++)
    {
      int num;
      cin>>num;
      //each digit react differently
      //for small case we can do 
      int array[10]={0,0,0,0,0,0,0,0,0,0};
      //denote whether anything is counted
      int *numse=new int[8];
      int *numuse=new int[8];
      //if 0, cout
      if (num==0)
	{
	  cout<<"Case #"<<c<<": "<<"INSOMNIA"<<endl;
	  continue;
	}
      //get digit;
      int num1=num;
      int dig=0;
      while (num1!=0)
	{
	  num1=num1/10;
	  dig++;
	}
      num1=num;
      for (int i=0;i<dig;i++)
	{
	  numse[i]=num1%10;
	  numuse[i]=numse[i];
	  num1=num1/10;
	}

      //denote how many time did it count
      for (int count=1;;count++)
	{
	  //1. check current state, make 1;
	  for(int i=0;i<dig;i++)
	    array[numuse[i]]=1;

	  //check if all array became 1;
	  bool flag=true;
	  for(int i=0;i<10;i++)
	    {
	      if(array[i]!=1)
		flag=false;
	    }
	  //if all became 1, we accept;
	  if (flag==true)
	    {
	      cout<<"Case #"<<c<<": ";
	      for(int i=0;i<dig;i++)
		cout<<numuse[dig-i-1];
	      cout<<endl;
	      break;
	    }
	  else
	    {
	      //2. do addition
	      int carry=0;
	      for(int i=0;i<dig;i++)
		{
		  if(numse[i]+numuse[i]+carry>9)
		    {
		      numuse[i]=(numse[i]+numuse[i]+carry)%10;
		      if(i==dig-1)
			{
			  dig++;
			  numse[i+1]=0;
			  numuse[i+1]=0;
			}
		      carry=1;
		    }
		  else 
		    {
		      numuse[i]=(numse[i]+numuse[i]+carry)%10;
		      carry=0;
		    }
		  
		}	  
	    }  
	    }
	  
	}

  return 0;
}
