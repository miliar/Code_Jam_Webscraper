#include<iostream>
using namespace std;
int main()
{
  int k,q,j,i,cases,remainder,flag,list1[10];
  long long int n,z;
  cin>>cases;
  for(q=1;q<=cases;q++)
    {
      cin>>n;
      if (n == 0)
	{
	  cout<<"Case #"<<q<<": INSOMNIA"<<endl;
	  continue;
	}
      j=1;
      flag = 1;
      for(i=0;i<10;i++)
	     list1[i]=0;
      while (flag != 0)
	 {
	  z=j*n;
	  k=z;
	  j++;
	  while (z != 0)
	    {
	      remainder = z % 10;
	      list1[remainder] = 1;
              z = z/10;
	    }

          flag = 0;     
	  for(i=0;i<10;i++)
	    {
              if (list1[i] == 0) 
                {
                  flag = 1; 
		  break;
                }  
            }	

          if (flag == 0)
              break;

	  }
      cout<<"Case #"<<q<<": "<<k<<endl;
    }
  return 0;
}
