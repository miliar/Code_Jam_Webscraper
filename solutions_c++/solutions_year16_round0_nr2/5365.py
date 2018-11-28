#include <iostream>
#include <cstdio>
#include <string>

#define ll long long
using namespace std;

int main()
{
	//freopen("PA4.in", "r", stdin);
	//freopen("PA4.out", "w", stdout);
	ll T, it, i, index, count, j, itr, ktr;
	string str;
	scanf("%lld", &T);
	for(it = 1; it <= T; it++)
	{
		str.clear();
		count = 0;
		cin >> str;
		//string::iterator itr;
		ll arr[str.size()] = {0};
		for(itr = 0; itr < str.size(); itr++)
		{
			if(str[itr] == '+')
				arr[itr]++;
		}
		//for(i = 0; i < str.size(); i++)
		//	cout << arr[i] << "\n";
		index = str.size() - 1;
		while(index >= 0)
		{
			while(arr[index] == 1)
				index--;
			if(arr[index] == 0 && index >= 0)
			{
				ll arb[index+1] = {0};
				if(arr[0])
				{
					ktr = 0;
					while(arr[ktr] == 1)
					{
						arr[ktr] = 0;
						ktr++;
					}
					count++;
				}
				for(i = 0; i <= index; i++)
				{
					arb[i] = arr[i];
				}					
				for(i = 0, j = index ; i <= index; i++, j--)
				{
					//cout << arr[i] << " : arr[i] arb[j] : " << arb[j] << "\n";
					if(arb[j])
						arr[i] = 0;
					else
						arr[i] = 1;
					//cout << "arr[i] " << arr[i] << " for index " << i << "\n";
					//cout << "arr[j] " << arr[j] << " for index " << j << "\n";
				}
				count++;
				index--;
			}
			//cout << "index is : " << index << "\n";
		}
		printf("Case #%lld: %lld\n", it, count);
	}
}
