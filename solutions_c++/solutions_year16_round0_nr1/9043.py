#include<iostream>

using namespace std;

int main(){
	long long int n,m,r,i;
	int j;
	int t;
	cin >> t;
	for(int k=1; k <= t; ++k)
	{
		int a[10]={-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
		j=0;
		i=1;
		cin >> n;
		m=n;
		r=n;
		while(1)
		{
		//	cout << n << " ";
			if(n==0)
			{
				cout << "Case #" << k << ": "<<  "INSOMNIA" << endl;
				break;
			}
			if(r>0)
			{	
				while(r!=0)
				{
					a[r%10]=r%10;
					r=r/10;
				}
				while(a[j]!=-1 && j<10)
				j++;
				if(j==10) 
				{
					cout << "Case #" << k << ": " << n << endl;
					break;
				}
			}
			if(j==10) break;
			i++;
			r=n=m*i;
		}
	}
	return 0;
}