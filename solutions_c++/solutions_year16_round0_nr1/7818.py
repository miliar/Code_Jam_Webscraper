//Author : Aman Sinha
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <cstring>
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
#include <climits>
#include <queue>
#include <iterator>
using namespace std;
typedef long long int ill;
#define fl(i,START,END) for(size_t i=START;i<END;++i)
#define rfl(i,START,END) for(size_t i=START;i>END;--i)

bool pairCompare1(const std::pair<string, int>& firstElem, const std::pair<string, int>& secondElem) {
  return firstElem.second > secondElem.second;
}

bool pairCompare2(const std::pair<int, int>& firstElem, const std::pair<int, int>& secondElem) {
  return firstElem.first < secondElem.first;
}

void init(int arr[],int size)
{
	fl(i,0,size)
	{
		arr[i] = 0;
	}
}
map <int,bool> numbers;
int main()
{
	int t;
	cin>>t;
	fl(k,1,t+1)
	{
		numbers.clear();
		ill answer = 0;
		ill n;
		cin>>n;
		ill temp = n;
		if(n==0)
		{
			cout<<"Case #"<<k<<": "<<"INSOMNIA"<<endl;
			continue;	
		}
		else
		{
			int count=0;
			while(count<10)
			{
				ill temp1 = temp;
				while(temp)
				{
					if(numbers[temp%10] == false)
					{
						numbers[temp%10] = true;
						++count;
						if(count==10)
						{
							answer = temp1;
						}
					}
					temp/=10;
				}
				temp= temp1 + n;
			}
			cout<<"Case #"<<k<<": "<<answer<<endl;
		}
	}
	return 0;
}

