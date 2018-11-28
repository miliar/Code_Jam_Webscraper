#include<iostream>
void main()
{ 
	using namespace std;
	int t,i,d,j;
	int M,count,n,copy;
	/*unsigned __int64 n,copy;*/
	cin >> t;
	for(i=1;i<=t;i++)
	{
		cin >> n;
		int a[]={0,1,2,3,4,5,6,7,8,9};
		M=1;count=0;copy=n; 
		if(n==0) {cout <<"Case #"<< i <<": INSOMNIA \n" ; continue;} 
		else 
		{
		do
		{
		for(;n!=0;n=n/10)
		{
			d=n%10;
			for(j=0;j<10;j++)
			{
				if(a[j]==d) {count++;a[j]=14;}
			}
		}
		M++;
		n=copy*M;
		}
		while(count<10);
		
		if(count==10) 
		{
			cout <<"Case #" << i << ": " << (M-1)*copy << "\n";
			continue;
		}
		}
	}
}

