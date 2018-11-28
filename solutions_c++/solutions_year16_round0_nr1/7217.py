#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t,n,i,j,b[10],k,e;
	scanf ("%d",&t);
	e=1;
	while (t--)
	{
		scanf ("%d",&n);
		for (i=0;i<10;i++)
		  b[i]=0;
		j=1000;
	for (j=1;j<=1000;j++)
		{
		    i=j*n;
		    while (i)
		    {
		    	b[i%10]=1;
		    	i/=10;
		    }
		    for (i=0;i<10;i++)
		    if (!b[i])
		    break;
		    if (i>=10)
		    break;
		}
		cout<<"Case #"<<e++<<": ";
		if (j>1000)
			cout<<"INSOMNIA"<<endl;
		else
		  cout<<j*n<<endl;
	}
	return 0;
}
			