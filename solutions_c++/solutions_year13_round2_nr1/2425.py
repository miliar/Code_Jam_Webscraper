#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;

#if 1
#define INPUT_FILE  "A-small-attempt3.in.txt"
#define OUTPUT_FILE "A-small.out.txt"
#else
#define INPUT_FILE  "A-large.in.txt"
#define OUTPUT_FILE "A-large.out.txt"
#endif


int main(int argc, const char * argv[])
{
    freopen(INPUT_FILE, "r", stdin);
	freopen(OUTPUT_FILE, "w+", stdout);
    
    unsigned int T, t, N, n;
    unsigned long long A;
    
    cin >> T;
    
    // For each test case
    for (t = 0; t < T; t++)
    {
        unsigned long long num_moves = 0;
        unsigned long long mote;
        vector<unsigned long long> vmotes;
        unsigned long long num_moves_removing_motes = 0;

        cin >> A >> N;
        for (n = 0; n < N; n++)
        {
            cin >> mote;
            vmotes.push_back(mote);
        }
        sort(vmotes.begin(),vmotes.end());
        
        for (unsigned int i=0; i<N; i++)
        {
            if (!(A>vmotes[i]))
            {
                if ((2*A-1) > vmotes[i])
                {
                    num_moves++;      // mote sized (A-1) added
                    A = 2*A-1;
                }
                else
                {
                    // Is it better to remove motes or add them?
                    const unsigned int remaining_motes = N - i;
                    unsigned int motes_to_add = 0;
                    bool solution_found = false;
                    
                    if ( num_moves_removing_motes == 0 )
                    {
                        num_moves_removing_motes = num_moves + remaining_motes;
                    }
                    
                    for (unsigned int j=0; j<remaining_motes; j++)
                    {
                        A = 2*A-1;
                        motes_to_add++;
                        if (A > vmotes[i]) { break; }
                    }
                    
                    if (motes_to_add < remaining_motes)
                    {
                        // Better to add
                        num_moves += motes_to_add;
                    }
                    else
                    {
                        // Better to remove
                        num_moves += remaining_motes;
                        solution_found = true;
                    }


                    // Is it better than our previous solution by removing motes?
                    if (num_moves > num_moves_removing_motes)
                    {
                        num_moves = num_moves_removing_motes;
                        solution_found = true;
                    }
                    
                    if (solution_found) break;
                }
            }
            A += vmotes[i]; // eat the mote
        }
        
        cout << "Case #" << t+1 << ": " << num_moves << endl;
    }
    return 0;
}