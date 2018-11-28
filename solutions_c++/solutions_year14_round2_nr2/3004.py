# include <iostream>
using namespace std;

int f(int a,int b)
{
	int i=1,sum = 0;int sum1 = 0;
	int rem,rem1,rem2,div1,div2;
	do
    {
        rem=a%2;
        sum=sum + (i*rem);
        a=a/2;
        i=i*10;
    }while(a>0);
	i = 1;
	do
    {
        rem=b%2;
        sum1=sum1 + (i*rem);
        b=b/2;
        i=i*10;
    }while(b>0);
	int var = 0;int j = 1;
	do
	{
	rem1 = sum%10;
	
	rem2 = sum1%10;
	
	if (rem1 == rem2) 
		var = var+j*rem1;
	sum = sum/10;
	sum1 = sum1/10;
	j = j*10;
	}while (sum > 0 && sum1 > 0);
	int x = 0;int k = 1;
	do
	{
		rem = var%10;
		x = x+k*rem;
		var = var/10;
		k = k*2;
	}while (var > 0);
	return x;
}

int main()
{
	int i,j,k,n,a,b,c;
	cin >> n;
	int flag[n];
		
	for (i=1;i<=n;i++)
	{
		flag[i] = 0;	
		cin >> a >> b >> c;
		for (j=0;j<a;j++)
	 	{
			for (k=0;k<b;k++)
			{
				if (f(j,k) < c)
					flag[i]++;
			}
		}
	}
	for (i=1;i<=n;i++)
		cout << "Case #"<<i<<": "<< flag[i] << endl;
}
					
