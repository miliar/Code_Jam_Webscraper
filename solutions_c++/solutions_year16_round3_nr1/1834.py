#include<bits/stdc++.h>
using namespace std;
#define endl "\n"
typedef long long int LL;

int main()
{

	 ios_base:: sync_with_stdio(false); cin.tie(0);
	  
	 freopen("input.in","r",stdin);
     freopen("output.in","w",stdout);

	 int t;cin>>t;for(int d=1;d<=t;d++)
	 {
	 	cout<<"Case #"<<d<<": ";
	 	 int x=65;
	 	 int n,sum=0;
	 	 cin>>n;
	 	 int a[n];
	 	 for(int i=0;i<n;i++)
	 	 	{
	 	 		cin>>a[i];
	 	 		sum+=a[i];
	 	 	}
         while(sum>0)
         {
         	 int mx=0;
               for(int i=0;i<n;i++)
               {
                    if(a[i]>a[mx])
                    	mx=i;
               }
               int fir=mx;
               sum--;a[mx]--;
                mx=0;
               for(int i=0;i<n;i++)
               {
                    if(a[i]>a[mx])
                    	mx=i;
               }
              if(a[mx]>sum/2)
              {
              	sum--;int sec=mx;a[mx]--;
              	char pp=x+fir;char cc=x+sec;
              	cout<<pp<<cc<<" ";
              }
              else
              {
              	  char pp=x+fir;
                  cout<<pp<<" ";
              }
         }
        
     cout<<endl;
	 }
        
        

	 return 0;
}