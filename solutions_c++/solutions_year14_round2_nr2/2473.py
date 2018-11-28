#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

int main()
{
    int num_cases;
    cin >> num_cases;

    for(int case_num = 1; case_num <= num_cases; ++case_num) {
    	int a, b, k;
    	cin >> a >> b >> k;

        int num_ways = 0;
        for(int i = 0; i < a; ++i)
        for(int j = 0; j < b; ++j)
    	   if((i&j) < k)
                num_ways++;
    	
    	cout << "Case #" << case_num << ": " << num_ways << endl;
    }

	return 0;
}