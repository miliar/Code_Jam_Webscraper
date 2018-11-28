#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

map<long long, long long> tree;

bool IsPalindrome(long long n)
{ 
	int tem = n;
	int rev = 0;
	while (n > 0)
	{
		int dig = n % 10;
		rev = rev * 10 + dig;
		n = n / 10;
	}

	return rev == tem;
}

long long read(long long idx){
	long long sum = 0;
	while (idx > 0){
		sum += tree[idx];
		idx -= (idx & -idx);
	}
	return sum;
}

void update(long long idx ,long long val){
	while (idx <= 1000){
		tree[idx] += val;
		idx += (idx & -idx);
	}
}

void GeneratePowers(long long n)
{
	for(int i=1;i*i <= n;i++)
	{
		if(IsPalindrome(i*i) && IsPalindrome(i))
			update(i*i,1);	
	}
}

int main() {
	
	ifstream cin("C-small-attempt0.in");
	ofstream cout("output.txt");


	int t;
	cin >> t;

	GeneratePowers(1000);

	for(int cs = 1; cs<=t; cs++)
	{
		long long a,b;
		cin >> a >> b;
		long long ans = read(b) - read(a);
		if(read(a) - read(a-1))
			ans++;

		cout << "Case #" << cs << ": " << ans << endl;
	}

	system("pause");
	
}
