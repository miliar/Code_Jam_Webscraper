#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
   int t;
   cin>>t;   
   int cases=1;
  
   while(t--)
   {
      double c,f,x;
	  cin>>c>>f>>x;
	  double new_f=2.0;
	  double time,time1,old_time=0;
	  time = x/2.0;
	  while(1)
	  {
		//cout<<old_time<<" "<<time<<endl;
		old_time = old_time + (c/new_f);
		 new_f= new_f +f;
		 time1=old_time + (x/new_f);
         if(time1<time)
			time=time1;
			else
				break;
	  
	   
	  }
		 
	  printf("Case #%d: %.7lf\n",cases++,time);
	}
	return 0;
}
	
