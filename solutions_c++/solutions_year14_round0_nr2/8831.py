#include <iostream>
#include <iomanip>

using namespace std;

int  main()
{
            int t=0;
            double n=2;
            double c=0,f=0,x=0;
            double tt[100];
            
            cin>>t;
            
            for(int i=1;i<=t;i++)
			{
				tt[i]=0;
				cin>>c;
				cin>>f;
				cin>>x;
                n=2;
                
				while((c/n)+(x/(n+f))<=(x/n))
				{
					tt[i]=tt[i]+(c/n);
                    n=n+f;
                }
                
				tt[i]=tt[i]+(x/n);
                
			}
            
            for(int i=1;i<=t;i++)
    		{
			    printf("Case #%d: %0.7f\n",i,tt[i]);
                //cout<<"Case #"<<i<<": "<<setprecision(10)<<tt[i]<<endl;
             }
return 0;
}