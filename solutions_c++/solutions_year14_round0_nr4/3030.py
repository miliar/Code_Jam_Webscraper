# include <iostream>
# include <sstream>
# include <algorithm>
using namespace std;
double a[1111],b[1111];

int main()
{   freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n_cases;cin>>n_cases;
	for(int id=0;id<n_cases;id++)
	{   int length;cin>>length;
	    for(int i=0;i<length;i++)
			cin>>a[i];
		for(int i=0;i<length;i++)
		    cin>>b[i];
		sort(&a[0],&a[length]);
		sort(&b[0],&b[length]);
		
		int p=0,q=0;
		while(p<length && q<length)
		{   if(a[p]<b[q])
		    {   p++;
			}
			else
			{   p++;
			    q++;
			}
		}
		cout <<"Case #"<<id+1<<": "<<q<<" ";
		p=0;q=0;
		while(p<length && q<length)
		{   if(b[q]<a[p])
		    {	q++;
			}
			else
			{   q++;
			    p++;
			}
		}
		cout <<length-p<<endl;
	}
}
		    
		




		
		
		
		
		
		
		

