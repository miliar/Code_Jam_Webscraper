#include <bits/stdc++.h>

using namespace std ;

int a[1000005];

int main()
{
   int t,n,v,i,j,balance,res,sum;

     freopen("abcd.txt","r",stdin);
    freopen("out2.txt","w",stdout);

	scanf("%d",&t);

	for(v=1;v<=t;v++)
    {
		scanf("%d",&n);

		for(i=0;i<n;i++)
		 scanf("%d",&a[i]);

		balance=a[0];

		i=1;

		while(i<n)
        {
			if(a[i]>balance)
                balance=a[i];

			i++;
		}
        res=balance;
		for(i=1;i<balance+1;i++)
        {
			sum=i;
			for(j=0;j<n;j++)
			{
				if(a[j]>i)
				{
					if(a[j]%i==0)
						sum+=((a[j]/i)-1);
					else
						sum+=a[j]/i;
				}

			}
			res=min(res,sum);
		}
		cout<<"Case #"<<v<<": "<<res<<endl;
	}
	return 0;
}
