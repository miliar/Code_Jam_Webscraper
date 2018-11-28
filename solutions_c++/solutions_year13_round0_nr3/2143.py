#include<iostream>
#include<cmath>
using namespace std;

bool check(int n)
{
	int arr[105];
	memset(arr, 0, sizeof(arr));
	bool f = true;
	int idx = 0;
	while(n)
	{
		arr[idx] = n%10;
		n/=10;
		idx++;
	}
	for(int i = 0; i < idx/2; ++i)
	{
		if(arr[i] != arr[idx-1-i])
		{
			f = false;
			break;
		}
	}
	return f;
}

int main()
{
	freopen("F:\\download\\3_1.txt", "r", stdin);
	freopen("F:\\download\\3_1out.txt", "w", stdout);
	int T,A,B;
	int id = 1;
	cin>>T;
	while(T--)
	{
		cin>>A>>B;
		int ans = 0;
		double s1 = sqrt((double)A);
		double s2 = sqrt((double)B);
		for(int i = (int) s1; i <= (int)s2; ++i)
		{
			if(check(i) == false)
				continue;
			if(i*i>B || i*i <A || check(i*i) == false)
				continue;
			ans++;
		}

		cout<<"Case #"<<id<<": "<<ans<<endl;
		id++;
	}
	return 0;
}