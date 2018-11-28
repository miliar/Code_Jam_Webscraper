#include <iostream>
#include <math.h>

using namespace std;

#if 1
#define INPUT_FILE  "C-small.in.txt"
#define OUTPUT_FILE "C-small.out.txt"
#else
#define INPUT_FILE  "C-large.in.txt"
#define OUTPUT_FILE "C-large.out.txt"
#endif

int sqrt_table [1001];

bool isFairAndSquare(int number)
{
    int sqrt_number = sqrt_table[number];
    if (sqrt_number == -1) return false;
    
    // Check if both are palindromes
    int last_digit = number%10;
    if (number > 100)
    {
        if ((number/100) != last_digit) return false;
    }
    else
    {
        if ((number > 10) && ((number/10) != last_digit)) return false;
    }
    if ((sqrt_number > 10) && ((sqrt_number/10) != sqrt_number%10))  return false;

    return true;
}

int main(int argc, const char * argv[])
{
    // Pre-process: Fill the sqrt_table. -1 means no integer result.
    for (int i = 1; i < 1001; i++)
    {
        float num = sqrtf((float)i);
        if (num > floorf(num)) sqrt_table[i] = -1;
        else sqrt_table[i] = (int)num;
    }
     
    freopen(INPUT_FILE, "r", stdin);
	freopen(OUTPUT_FILE, "w+", stdout);

    int T, A, B;
    
    cin >> T;

    // For each test case
    for (int t = 0; t < T; t++)
    {
        cin >> A >> B;
        
        int count = 0;
        
        for (int number = A; number<=B; number++)
        {
            if (number == 1000) continue; // Special case. Not a "Fair and Square" number.
            if (isFairAndSquare(number))
            {
                count++;
            }
        }
        
        cout << "Case #" << t+1 << ": " << count;
		cout << endl;
    }

    return 0;
}

