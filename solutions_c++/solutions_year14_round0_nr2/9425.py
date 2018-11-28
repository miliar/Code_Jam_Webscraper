#include<iostream>
#include<stdlib.h>
#include <iomanip>  

using namespace std;
int main()
{
	int t=0,farms=0;
	cin >> t;
	long double c[t],f[t],x[t],time2000[10000],time500[10000],total[t],rate=2.0000000000000000;
	for(int i=1;i<=t;i++)
	    {
            c[i-1]=0.0000000000000;
            f[i-1]=0.0000000000000;
            x[i-1]=0.0000000000000;
            total[i-1]=0.0000000000;
	    }
    for(int i=1;i<10000;i++)
        {
            time2000[i-1]=0.0000000000000;
            time500[i-1]=0.0000000000000;
        }
            
	for(int i=1;i<=t;i++)
	    {   cin >> fixed;
	    	cin >> c[i-1];
	    	cin >> f[i-1];
	    	cin >> x[i-1];
	    }



      /* for(int i=0;i<t;i++)
        {   cout << fixed;
            cout << c[i]<<endl;
            cout << f[i]<<endl;
            cout << x[i]<<endl;
        }*/      




    for (int l = 0; l < t; l++)
    {       total[l]=0.00000000000;
    		for(int k=1;k<=10000;k++)
    		{
    		 rate=2+(k-1)*f[l];
    	     time500[k-1]=c[l]/rate;
    	     time2000[k-1]=x[l]/rate;
            }

            for(int k=0;k<=10000;k++)
            {
            	if(time2000[k]<=time2000[k+1]+time500[k])
            	{
                    for (int i = 0; i < k ; i++)
                    {
                        total[l] += time500[i];
                    }
                    total[l] += time2000[k];
                    break;
            	}
            }
            cout<<fixed;
            cout <<"Case #"<<l+1<<": "<<setprecision(7)<<total[l]<<endl;   	
        }


     }

