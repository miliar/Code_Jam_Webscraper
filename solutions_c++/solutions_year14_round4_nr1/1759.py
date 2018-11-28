#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <algorithm>
#define modu 9999991
using namespace std;
int M,N,K;
int ans;
int S[100001];
int main(void)
{
   int i,t0,T,X,ans,j,flag;

   cin>>T;

   for(t0=1;t0<=T;t0++)
   {
       ans=0;
	   cin>>N>>X;
	   for(i=0;i<N;i++)
	   {
		   cin>>S[i];
	   }
	 sort(S,S+N);
	 for(i=0;i<N;i++)
	 {flag=0;
		 if(S[i]==-1)
			 continue;
		for(j=N-1;j>i;j--)
		{
			//cout<<S[i]<<S[j]<<endl;
			if(S[j]==-1||S[j]+S[i]>X)
				continue;
			else
			{

                S[j]=-1;
                S[i]=-1;
               // cout<<"a:"<<S[i]<<S[j]<<endl;
                ans++;
                flag=1;
                break;
			}

		}

		if(flag==0)
		{S[i]=-1;
		ans++;
		}
	 }
	 cout<<"Case #"<<t0<<": "<<ans<<endl;
   }
   return 0;
}

