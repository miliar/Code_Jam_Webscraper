#include <iostream>
#include<string.h>
using namespace std;
int a[1001]={'0'};

int main(void) {
 freopen("A-large (1).in","r",stdin);
  freopen("outputgcj.out","w",stdout);
	int t,n,flag,count,max,sum;
	cin>>t;
	int x=1;
	while(x<=t)
	{  	sum=0;
		cin>>n;
		max=1;
		for(int i=1;i<=n;i++)
		{cin>>a[i];if(a[i]>a[max])
		max=i;sum+=a[i];
	    }
	    cout<<"Case #"<<x<<": ";

	    if(n==2)
          {for(int i=1;i<=a[1];i++)
		  cout<<"AB ";
            cout<<endl;}		
		else if(n!=2) 
		{
			while(sum!=2)
		 { max=1;
		  for(int i=1;i<=n;i++)
		{if(a[i]>a[max])
		max=i;
	    }
		  cout<<(char)(max+64)<<" "; sum--;a[max]--;
     }
     for(int i=1;i<=n;i++)
     if(a[i]==1)
     cout<<(char)(i+64);
     cout<<endl;
    }
	x++;
	}
	
}

