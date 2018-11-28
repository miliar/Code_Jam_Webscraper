#include <bits/stdc++.h>

using namespace std;

int main()
{
  freopen("in.in","r",stdin);
  freopen("out.out","w",stdout);
  int tc;
  cin>>tc;
  for(int t=1;t<=tc;t++)
  {
	  double c,f,x;
	  cin>>c>>f>>x;
	  double co=0;
	  double r=2.00;
	  double time=0;
	  while(co<=x)
	  {
		  //cout<<"time "<<time<<endl;
		  if(co>=x) break;
		  double t1 = (x-co)/r;
		  double t2 = (x-co+c)/(f+r);
		  if (co<c)
		  {
			  co=min(x,c);
			  time+=min(x,c)/r;
			  
		  }
		  else if(t1<=t2)
		  {
			 // cout<<"ere"<<"co "<<co<<endl;
			  
			  time+=(x-co)/r;
			  co+=x-co;
		  }
		  else
		  {
			  co-=c;
			  r+=f;
		  }
		//  cout<<"time after"<<time<<endl;
	  }
	  cout<<"Case #"<<t<<": ";
	  printf("%0.7lf\n",time);
	  
	  
  }	
  return 0;
}
