#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cmath>

using namespace std;
int digit_array[15];

bool isPalindrome(long long n)
{
	int l = 0; // length of n
	int i = 0;
	while(n>0)
	{
		digit_array[l++] = (n%10);
		n = n/10;
	}

	while(i < (l/2))
	{
		if(digit_array[i] != digit_array[l-1-i])
			return false;

		i++;
	}

	return true;
}

int idxLessThan(long long n, const vector<long long>& v)
{
	int v_size = v.size();
	int i;
	for(i=0; i<v_size; i++)
	{
		if(v[i]>n)
			break;
	}
	return (i-1);
}

int idxGreaterThan(long long n, const vector<long long>& v)
{
	int v_size = v.size();
	int i;
	for(i=v_size-1; i>=0; i--)
	{
		if(v[i]<n)
			break;
	}
	return (i+1);
}

void printVector(vector<long long>& v)
{
	vector<long long>::iterator it;
	for(it=v.begin(); it!=v.end(); it++)
	{
		printf("%d ", *it);
	}
	printf("\n");
}

int main()
{
	long long a, b;
	int t = 0, T;
	int i;
	int count;
	vector<long long> fair_number_array;
	for(i=1; i<=10000; i++) // generate 'fair and square' numbers list
	{

		if(isPalindrome(i))
		{
			if(isPalindrome(i*i))
			{
				fair_number_array.push_back(i*i);
			}
		}
	}

	//printVector(fair_number_array);
	int start_idx, end_idx;
	//printf("jbnbnb\n");
	scanf("%d", &T);
	while(t<T)
	{
		t++;
		scanf("%lld %lld", &a, &b);
		start_idx = idxGreaterThan(a, fair_number_array);
		end_idx = idxLessThan(b, fair_number_array);
		//printf("start_idx = v[%d] = %lld\n", start_idx, fair_number_array[start_idx]);
		//printf("end_idx = v[%d] = %lld\n", end_idx, fair_number_array[end_idx]);
		count = end_idx - start_idx + 1;
		printf("Case #%d: %d\n", t, count);

	}
	return 0;
}
