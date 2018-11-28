#include<iostream>

using namespace std;

int main()
{
	int cases;
	cin>>cases;
	long long int r, t;
	for(int q=0 ; q<cases ; q++)
	{
		cin >> r >> t;
		long long int sum = 0, count =1;
		long long int j = 0;
		for(long long int i = r; sum <= t; i+=2)
		{
			sum += (2*i + 1);
			j++;
		}
		cout<<"Case #"<<q+1<<": "<<j-1<<"\n";
	}
	return 0;
}
