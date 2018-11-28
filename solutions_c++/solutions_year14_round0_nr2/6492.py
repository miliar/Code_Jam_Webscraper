#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
  //c = cost of farm
  //x = final dest
  //f = extra by farm

  int t;
  int casenum = 0;
  
  cin>>t;  

  while(t--)
    {      
      double c,f,x;
      double currate= 2.0;
      double curcookies = 0;
      double tt = 0;
      cin>>c;
      cin>>f;
      cin>>x;

      casenum++;

      if(x<c)
	{
	  tt = x/currate;
	}
      else
	{
	  while(curcookies<x)
	    {
	      tt += (c/currate);
	      curcookies = c;
	  
	      if( ((x - curcookies)/currate) > ((x)/(currate + f)) )
		{
		  currate += f;
		  curcookies = 0;	      
		}
	      else
		{
		  tt+=(x-curcookies)/currate;
		  break;
		}	  
	    }
	}

      cout.setf(ios::fixed, ios::floatfield);      
      cout<<"Case #"<<casenum<<": "<<setprecision(7)<<fixed<<tt<<endl;     
    }

  return 0;
}
