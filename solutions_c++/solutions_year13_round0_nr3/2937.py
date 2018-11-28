#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <math.h>
using namespace std;

bool isFair(int n)
{
    char str[64];
    int i = 0, value = n;
    while (value)
    {
        str[i++] = (value % 10) + 0x30;
        value /= 10;
    }
    str[i] = 0;
    if (atoi(str) == n)
        return true;
    
    return false;
}

int main (int argc, char * const argv[])
{
	freopen("input3.txt", "rt", stdin);
	freopen("output3.txt", "wt", stdout);
	
	int T;
	cin >> T;
	
    for(int t = 0; t < T; t++)
    {
        int A, B;
        cin >> A;
        cin >> B;
        
		int a = (int)sqrt((double)A) - 1;
        if (a < 0)
            a = 0;
        int b = (int)sqrt((double)B) + 1;
        int s = 0;
        
        for (int i = a; i <= b; i++)
        {
            int fair = i * i;
            if (fair >= A && fair <= B && isFair(fair) && isFair(i))
                s++;
        }
        
        cout << "Case #" << t+1 << ": " << s << endl;
        
	}
	
	return 0;
}

