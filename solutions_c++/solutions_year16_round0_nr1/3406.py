		/*masterwayne*/
#include<bits/stdc++.h>
using namespace std;
#define sc(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d %d",&x,&y)
#define sc3(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define pf(x) printf("%d",x)
#define pf2(x,y) printf("%d %d",x,y)
#define pf3(x,y,z) printf("%d %d %d",x,y,z)
#define fr(i,x,n) for(int i=x;i<n;i++)
#define fre(i,x,n) for(int i=x;i<=n;i++)
#define fb(i,x,n) for(int i=n-1;i>=x;i--)
#define fbe(i,x,n) for(int i=n;i>=x;i--)
#define pfn() printf("\n")
#define pfs() printf(" ")
#define pb push_back
int main()
{
	//freopen("inp22.in","r",stdin);
	//freopen("out2.txt","w",stdout);
	int t;
	sc(t);
	for(int i=1;i<=t;i++)
	{
		int n;
		sc(n);
		if(n==0)
		{
          cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
		}
		else
		{
		int arr[10]={0};
		int count=0;
		long long int m=n;
		while(1)
		{
           long long num=m;
           while(num!=0)
           {
           	  int rem=num%10;
           	  num=num/10;
           	  if(arr[rem]==0)
           	  {
           	  	count++;
           	  	arr[rem]=1;
           	  }
           }
           if(count==10)
           	break;
           m+=n;
		}
		cout<<"Case #"<<i<<": "<<m<<endl;
	    }
	}
	return 0;
}