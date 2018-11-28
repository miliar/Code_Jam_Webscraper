#include <bits/stdc++.h>
using namespace std;

int main() {
	int t, ans;
	string stack;
	char curr;
	cin >> t;
	for (int z=1; z<=t; ++z)
	{
	    cin >> stack;
	    int len = stack.length();
	    curr = stack[0];
	    ans = 0;
	    for (int i=1; i<len; ++i)
	    {
	        if (curr != stack[i])
	        {
	            ++ans;
	            curr = stack[i];
	        }
	    }
	    if ('-' == curr)
	    {
	        ++ans;
	    }
	    cout << "Case #" << z << ": " << ans << endl;
	}
	
	return 0;
}

