#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
     double x,f,c;
     int t;
     cin>>t;
     for(int i=1;i<=t;i++)
     {
         double time1=0.0,time2=0.0,time3=0.0,cook=2.0;
        cin>>c>>f>>x;
     	for(int j=0;;j++)
     	{
     		time1=x/cook;
     		time2=c/cook+(x/(cook+f));
     		if(time2<time1)
     		{
     		    time3=time3+(c/cook);
                cook=cook+f;
     	     }
     	     else
     	     {
     	         time3=time3+(x/cook);
                break;
     	     }
     	}
     	cout<<"Case #"<<i<<": "<<fixed;
     	cout<<setprecision(7)<<time3<<endl;
     }
	return 0;
}
