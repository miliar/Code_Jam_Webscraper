# include <iostream>
# include <sstream>
using namespace std;

int main()
{   freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n_cases;cin>>n_cases;
	for(int case_id=0;case_id<n_cases;case_id++)
	{	double C,F,X;cin>>C>>F>>X;
		double prev1=X/2.0;double prev2=0.0;int n_farms=0;
		
		while(1)
		{   double new1=X/(2.0+((n_farms+1.0)*F));
		    double new2=prev2+(C/(2.0+(n_farms*F)));
		    
		    double dec=prev1-new1;
		    double inc=new2-prev2;

		    if(dec<=inc)
			{   
			    printf("Case #%d: %.7lf\n",case_id+1,prev1+prev2);
			    break;
			}
			n_farms++;
			prev1=new1;prev2=new2;
		}
	}

}
			
	

	    
	
