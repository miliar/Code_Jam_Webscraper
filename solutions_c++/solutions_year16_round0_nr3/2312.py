#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

typedef long long ll;


bool isPrime(ll num)
{
	if(num <= 1) return false;
	if(num == 2) return true;
	if(num % 2 == 0) return false;
	int m = std::sqrt(num);
	for(int i = 3; i <= m; i+=2)
		if(num % i == 0)
			return false;
	return true;
	
}


ll getFac(ll num)
{
	if(num <= 1) return -1;
	if(num == 2) return -1;
	if(num % 2 == 0) return 2;
	ll m = std::sqrt(num);
	for(ll i = 3; i <= m; i+=2)
		if(num % i == 0)
			return i;
	return num;
	
}

bool jamNumber(ll num, vector<ll> &nums)
{
	nums.clear();
	for(int base = 2; base <= 10; base++)
	{
		ll temp = num;
		ll numS = 0;
		for(int loc = 0; temp > 0; loc++)
		{
			numS += (temp % 10) * pow(base, loc);
			temp /= 10;
		}
		//cout << numS << " " << getFac(numS) << endl;
		if(isPrime(numS))
		{
			return false;
		}else
		{
			nums.push_back(getFac(numS));
		}
		
	}
	
	return true;
}

ll base10To2(ll num)
{
	vector<ll> dig;
	ll temp = num;
	while(temp > 0)
	{
		dig.push_back(temp % 2);
		temp /= 2;
	}
	ll answer = 0;
	for(int i = 0; i < dig.size(); i++)
	{
		answer *= 10;
		answer += dig.at(dig.size() - 1 - i);
	}
	return answer;
	
}

int main()
{
	ll casses = 0;
	cin >> casses;
	vector<ll> nums;
	for(int caseNum = 0; caseNum < casses; caseNum++)
	{
		cout << "Case #" << caseNum + 1 << ":" << endl;
		ll num = 1;
		ll n, j;
		cin >> n >> j;
		num *= pow(2, n - 1);
		num += 1;
		while(j > 0)
		//while(true)
		{
			if(jamNumber(base10To2(num), nums))
			{
				cout << base10To2(num);
				
				for(int i = 0; i < nums.size(); i++)
				{
					cout << " " << nums.at(i);
				}
				cout << endl;
				j--;
			}
			num += 2;
		}
	}
	//jamNumber(1001);
	//cout << jamNumber(100011, nums) << endl;
	//cout << base10To2(35) << endl;
	return 0;
}
