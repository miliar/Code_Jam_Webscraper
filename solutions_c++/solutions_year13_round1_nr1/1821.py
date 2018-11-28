#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;

#if 1
#define INPUT_FILE  "A-small-attempt0.in.txt"
#define OUTPUT_FILE "A-small.out.txt"
#else
#define INPUT_FILE  "A-large.in.txt"
#define OUTPUT_FILE "A-large.out.txt"
#endif


unsigned long long radius, paint, num_circles, used_paint;

int main(int argc, const char * argv[])
{
    freopen(INPUT_FILE, "r", stdin);
	freopen(OUTPUT_FILE, "w+", stdout);
    
    unsigned int T, t;
    
    cin >> T;
    
    // For each test case
    for (t = 0; t < T; t++)
    {
        cin >> radius >> paint;
        used_paint = 0;
        num_circles = 0;
        bool run_out_of_paint = false;
        radius++;
        
        while (!run_out_of_paint)
        {
            double paint_needed = 2 * radius - 1;
            used_paint += paint_needed;
            if (used_paint>=paint)
            {
                if (used_paint==paint)
                {
                   num_circles++; 
                }
                run_out_of_paint = true;
            }
            else
            {
                num_circles++;
                radius+=2;
            }
        }
        
        cout << "Case #" << t+1 << ": " << num_circles << endl;
    }
    return 0;
}