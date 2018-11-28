#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;

#if 1
#define INPUT_FILE  "B-small-attempt0.in.txt"
#define OUTPUT_FILE "B-small.out.txt"
#else
#define INPUT_FILE  "B-large.in.txt"
#define OUTPUT_FILE "B-large.out.txt"
#endif


int main(int argc, const char * argv[])
{
    freopen(INPUT_FILE, "r", stdin);
	freopen(OUTPUT_FILE, "w+", stdout);
    
    unsigned int T, t, a, A, b, B, K;
    
    cin >> T;
    
    // For each test case
    for (t = 0; t < T; t++)
    {
        cin >> A >> B >> K;
        
        int count = 0;
        
        for (a = 0; a < A; a++)
        {
            for (b = 0; b < B; b++)
            {
                if ( (b&a) < K )
                {
                    count++;
                }
            }
        }
        
        cout << "Case #" << t+1 << ": " << count << endl;
    }

    return 0;
}