#include <iostream>
#include <cstring>
#include <map>
#include <cmath>

using namespace std;

bool palindrome(long double number)
{
	long double check = 0, dig, original = number;

	while(number > 0)
	{
        dig = (long long)number % 10;
        check = check * 10 + dig;
        number = (int)(number / 10);
	}

	return (check == original);
}

long double square(long double number)
{
    long double check = sqrt(number);

	if(check - (int)check == 0)
	    return check;
	
	return 0;
}

int main()
{
	int T;
	long double A, B, root, count;
	map<long double, bool> hash;
	map<long double, bool>::iterator it;

    cin >> T;

	for(int ix = 0; ix < T; ix++)
	{    
	    cin >> A;
	    cin >> B;
        count = 0;
        hash.clear();

        for(long double iy = B; iy >= A; iy--)
        {
            it = hash.find(iy);
            if(it != hash.end() && it->second == true)
            {
                root = square(iy);
                hash.erase(it);

                if(root != 0)
                {
                	it = hash.find(root);
                	if(it != hash.end() && it->second == true)
                	    count++;
                    else if(palindrome(root))
                    {
                         hash.insert(make_pair(root, true));
                         count++;
                    }
                    else
                    	hash.insert(make_pair(root, false));
                }
            }
            else if(palindrome(iy))
            {
            	root = square(iy);
                
                if(root != 0)
                {
                	it = hash.find(root);
                	if(it != hash.end() && it->second == true)
                	    count++;
                    else if(palindrome(root))
                    {
                         hash.insert(make_pair(root, true));
                         count++;
                    }
                    else
                    	hash.insert(make_pair(root, false));
                }
            }
        }

        cout << "Case #" << ix+1 << ": " << count << endl;
    }

    return 0;
}