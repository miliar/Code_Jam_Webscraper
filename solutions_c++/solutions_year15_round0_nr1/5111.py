#include <iostream>
#include <cassert>

using namespace std;

void prologue()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    FILE *fp = freopen("/Users/-RooneY-/Desktop/src/input", "r", stdin);
    assert(fp);
    
    FILE *fpw = freopen("/Users/-RooneY-/Desktop/src/output", "w", stdout);
    assert(fpw);
}

int main()
{
    prologue();
 
    int t;
    cin >> t;
    
    for (int test = 1; test <= t; ++test)
    {
    	int smax;
    	string sstr;
    	
    	cin >> smax;
    	cin >> sstr;
    	
    	assert(sstr.size() == smax + 1);
    	
    	for (int add = 0; add <= smax; ++add)
    	{
    		bool valid = true;
    		int standup_count = add;
    		
    		for (int level = 0; level <= smax && valid; ++level)
    		{
    			if (standup_count >= level)
    				standup_count += sstr[level] - '0';
    			else
    				valid = false;
    		}
    		
    		if (valid)
    		{
    			cout << "Case #" << test << ": " << add << endl;
    			break;
    		}
    	}
    }
    
    return 0;
}