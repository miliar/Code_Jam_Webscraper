#include <iostream>
using namespace std;
int test_for_all(int *arr)
{
	int t = 0,i;
	for(i=0;i<10;i++)
	{
		if(arr[i] == 1)
			t++;
	}
	if(t == 10)
		return 0;
	else 
		return 1;
}
int main()
{
	int t,x = 1;
	int test[10];
	long long int n,i,tmp,num;
	cin >> t;
	while(t--)
	{
		cin >> n;
		if(n == 0)
		{
			cout << "Case #" << x << ": " << "INSOMNIA\n";
			x++;
			continue;
		}
		for(i=0;i<10;i++)
			test[i] = 0;
		i = 1;
		while(test_for_all(test) && i <= 1000000)
		{
			tmp = n*i;
			num = tmp;
			while(tmp)
			{
				test[tmp%10] = 1;
				tmp /= 10;
			}
			i++;
		}
		cout << "Case #" << x << ": " <<  num << "\n";
		x++;
	}
	return 0;
}
