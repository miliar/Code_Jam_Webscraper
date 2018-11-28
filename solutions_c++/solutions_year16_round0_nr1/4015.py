#include <bits/stdc++.h>
using namespace std;
int d[10];
int check(int n)
{
	int i,f;
	while(n!=0)
	{
		d[n%10]=1;
		n/=10;
	}
	for(i=0;i<10;++i)
	{
		if(d[i]==1)
		f=1;
		else
		{
			f=0;
			break;
		}
	}
	return f;
}
int main() 
{
	ifstream input;
    ofstream output;
    input.open("A-large.in");
    output.open("output.txt");
	int t,j=1;
	input>>t;
	while(t--)
	{
		long long int n,k=2,i;
		input>>n;
		for(i=0;i<10;++i)
		d[i]=0;
		output<<"Case #"<<j<<":";
		j++;
		if(n==0)
		output<<" INSOMNIA\n";
		else
		{
			while(1)
			{
				if(check(n))
				break;
				else
				n=(n/(k-1))*k,k++;
			}
			output<<" "<<n<<endl;
		}
	}
	output.close();
	input.close();
	//sakshamsinghnsit
	return 0;
}
