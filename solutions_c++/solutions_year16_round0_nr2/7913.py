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

int flip(vector<int> arr, int i)
{
    int temp, start = 0;
    int count = 0;
    while (start < i)
    {
        temp = arr[start];
        arr[start] = arr[i];
        arr[i] = temp;
        count=1;
        start++;
        i--;
    }
    return count;
}
 
/* Returns index of the maximum element in arr[0..n-1] */
int findMax(vector<int> arr, int n)
{
   int mi, i;
   for (mi = 0, i = 0; i < n; ++i)
       if (arr[i] >= arr[mi])
              mi = i;
   return mi;
}

int findMin(vector<int> arr, int n)
{
   int mi, i;
   for (mi = 0, i = 0; i < n; ++i)
       if (arr[i] <= arr[mi])
              mi = i;
   return mi;
}
 
// The main function that sorts given array using flip 
// operations
int pancakeSortasc(vector<int> arr, int n)
{
    // Start from the complete array and one by one reduce
    // current size by one
    int flip_count = 0;
    for (int curr_size = n; curr_size > 1; --curr_size)
    {
        // Find index of the maximum element in 
        // arr[0..curr_size-1]
        int mi = findMax(arr, curr_size);
 
        // Move the maximum element to end of current array
        // if it's not already at the end
        if (mi != curr_size-1)
        {
            // To move at the end, first move maximum number
            // to beginning 
            flip_count+=flip(arr, mi);
            // Now move the maximum number to end by reversing
            // current array
            flip_count+=flip(arr, curr_size-1);
        }
    }
    return flip_count;
}

int pancakeSortdesc(vector<int> arr, int n)
{
    // Start from the complete array and one by one reduce
    // current size by one
    int flip_count = 0;
    for (int curr_size = n; curr_size > 1; --curr_size)
    {
        // Find index of the minimum element in 
        // arr[0..curr_size-1]
        int mi = findMin(arr, curr_size);
 
        // Move the minimum element to end of current array
        // if it's not already at the end
        if (mi != curr_size-1)
        {
            // To move at the end, first move minimum number
            // to beginning 
            flip_count+=flip(arr, mi);
            // Now move the minimum number to end by reversing
            // current array
            flip_count+=flip(arr, curr_size-1);
        }
    }
    return flip_count;
}

map<char,int> hash1;

int main()
{
	int t;
	cin>>t;
	hash1['-'] = 0;
	hash1['+'] = 1;
	fl(k,1,t+1)
	{
		string s;
		cin>>s;
		vector<int> arr;
		vector<int> arr1;
		int i=0;
		while(i<s.length())
		{
			char temp = s[i];
			while(i+1<s.length() && s[i] == s[i+1])
			{
				++i;
			}
			arr.push_back(hash1[temp]);
			arr1.push_back(hash1[temp]);
			++i;
		}
		int flip_count_asc=pancakeSortasc(arr,arr.size());
		int flip_count_desc=pancakeSortdesc(arr1,arr1.size());
		if(flip_count_asc == 0 )
		{
			if(arr[0] == 0)
			{
				++flip_count_asc;
			}
		}
		else
		{
			++flip_count_asc;
		}
		if(flip_count_desc == 0 )
		{
			if(arr1[arr1.size()-1] == 0)
			{
				flip_count_desc+=2;
			}
		}
		else
		{
			flip_count_desc+=2;
		}
		cout<<"Case #"<<k<<": "<<min(flip_count_desc,flip_count_asc)<<endl;	
	}
	return 0;
}

