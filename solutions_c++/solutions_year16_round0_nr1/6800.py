#include<iostream>
using namespace std;
int N,T,A[11];
void check(long long int N)
{
	//cout << "value " << N;
	while(N>0)
	{
		A[N%10]=1;
		N=N/10;
	}
}
int main()
{
	int t=1,f=0,i,j;
	long long int p;
	cin >> T;
	while(T--)
	{
		cin >> N;
		for(i=0;i<=9;i++)
		A[i]=0;
		f=0;
		for(i=1;i<100002;i++)
		{	
			p=N*i;
			f=0;
			check(p);
			for(j=0;j<=9;j++){
				if(A[j]!=1)
					{
						f=1;
						break;	
					}
			}
			if(f==0)
			{	
				cout << "Case #" << t << ": " << p << endl;
				break;
			}
		}
		if(f==1)
		cout << "Case #" << t << ": INSOMNIA" << endl;
		t++;
		
		
	}



return 0;
}
