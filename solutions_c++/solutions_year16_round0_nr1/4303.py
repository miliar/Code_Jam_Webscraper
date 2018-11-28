#include <bits/stdc++.h>
using namespace std;

int main() {
	int t, i, digit;
	unsigned long long n, temp;
	cin >> t;
	for (int z=1; z<=t; ++z)
	{
	    cin >> n;
	    if (n != 0)
	    {
	        unordered_set<int> mySet = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
	        temp = n;
	        i = 1;
	        do
	        {
	            while (temp != 0)
	            {
	                digit = temp%10;
	                temp = temp/10;
	                mySet.erase(digit);
	            }
	            ++i;
	            temp = i*n;
	        } while (!mySet.empty());
	    }
	    if (n==0)
	    {
	        cout << "Case #" << z << ": INSOMNIA" << endl; 
	    }
	    else 
	    {
	        cout << "Case #" << z << ": " << (temp - n) << endl; 
	    }
	}
	return 0;
}
