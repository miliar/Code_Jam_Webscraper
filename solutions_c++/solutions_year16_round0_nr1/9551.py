#include<iostream>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("a_large.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
	int array_digits[10];
	int T;
	cin>>T;
	int N,Ni;
	int i=1,k,j;
	int digit;
	int count = 0;
	for(i=1;i<=T;i++)
	{
		cin>>N;
		Ni=N;
		k=1,count = 0;
		for(j=0;j<10;j++)
		{
			array_digits[j] = 0;
		}
		if(N==0)
		{
			cout<<"Case #"<<i<<": INSOMNIA\n";
		}
		else
		{
			while(count!=10)
			{
				Ni= N*k;
				k++;
					while(Ni>0 && count!=10)
					{
						digit = Ni%10;
						if(array_digits[digit]==0)
						{
							array_digits[digit] = 1;
							count++;
						}
						Ni=Ni/10;
					}

			}
			k--;
			cout<<"Case #"<<i<<": "<<N*k<<endl;
		}
	}
	return 0;
}



