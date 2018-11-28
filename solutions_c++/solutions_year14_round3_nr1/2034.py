#include<iostream>
#include<math.h>
using namespace std;

int main()
{int T,P,Q,i,p,q;
char input[30];
	cin>>T;
	for(int co=0;co<T;co++)
	{cin>>input;i=P=Q=0;p=0;
		for(i=0;input[i]!='/';i++)
		{P=P*10+((int)input[i]-48);
			}
			i++;
		for(;input[i]!='\0';i++)
		{Q=Q*10+((int)input[i]-48);
			}
		
		cout<<"Case #"<<(co+1)<<": ";
		
		for(i=0;pow(2,i) <= Q;i++)
		{if(Q% (int)pow(2,i)!=0){cout<<"impossible"<<endl;p=1;break;}
			}
		if(p==0)
		{i=0;
		while(P<Q)
		{P*=2;i++;
			}
		cout<<i<<endl;}
		
		}
	
	return 0;}
