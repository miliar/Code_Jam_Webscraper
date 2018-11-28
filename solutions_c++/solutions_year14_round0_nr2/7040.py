#include <iostream>
#include <iomanip>
using namespace std;

int main() {
        
     double double x,f,c,t;
     cin>>t;
     for(int i=1;i<=t;i++)
     {double double time1=0.0,time2=0.0,time3=0.0,crate=2.0;
      cin>>c>>f>>x;
     	for(int j=0;;j++)
     	{  
     		time1=x/crate;
     		time2=c/crate+(x/(crate+f));
     		if(time2<time1)
     		{ time3=time3+(c/crate);
     		 crate=crate+f;
     	     }
     	     else
     	     {time3=time3+(x/crate);
     	     break;
     	     }
     	
     	
     	}
     	cout<<"Case #"<<i<<": "<<fixed;
     	cout<<setprecision(7)<<time3<<endl;
     }
	return 0;
}