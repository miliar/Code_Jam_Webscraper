#include<iostream>
#include <cstdio>
#include <iomanip> 
using namespace std;

double f,c,x;
int n;
int main()
	{freopen("output.txt","w",stdout);
	 std::cout << std::fixed;
	 cin>>n;
	 for(int i=1;i<=n;++i)
		{cin>>c>>f>>x;
		 double f1=0,f2=0,t=0,r=2.0;
		 if(c<x)
			{while(1)
				{f1=x/r;
		 	 	 f2=c/r + x/(r+f);
				 if(f1<=f2)
					break;
				 t=t+c/r;
				 r=r+f;
				}
			 t=t+x/r;
			}
		 else
			{t=x/r;
			}
		 cout<<"Case #"<<i<<": ";
		 std::cout << std::setprecision(7) << t << '\n';
		}
  return 0;
}

