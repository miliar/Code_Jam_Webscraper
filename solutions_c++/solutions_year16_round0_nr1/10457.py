#include<iostream>
#include<set>
using namespace std;

long long solve(int n)
{	
	if(n == 0) return -1;
	long long cur = 0;
	int last;
	set<int> sets;
	while(sets.size() < 10)
	{
		cur += n;
		long long tmp = cur; 
		while(tmp > 0) 
		{
			last = tmp%10;
			sets.insert(last);
			tmp /= 10;
		}
	}
	return cur;
}

int main()
{
	int T, N;
//	long long cur;
	cin>>T;
	for(int i = 0; i<T; i++)
	{
		cin >> N; 
		long long ans = solve(N);
		if(ans > 0) 
			cout << "Case #" << (i+1)<<": "<< ans << endl;
		else 
			cout << "Case #" << (i+1)<<": "<< "INSOMNIA"<<endl;
	}
	return 0;
}

