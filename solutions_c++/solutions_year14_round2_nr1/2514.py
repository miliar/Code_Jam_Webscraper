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

typedef struct fString
{
    string s;
    unsigned int i;
    unsigned int l;
} fString;

unsigned int getNumEqualLetters(char cChar, fString *sLine)
{
    unsigned int count = 0;
    while (sLine->i < sLine->l)
    {
        if (cChar == sLine->s[sLine->i]) // advance index
        {
            sLine->i++;
            count++;
        }
        else break;
    }
    return count;
}

int main(int argc, const char * argv[])
{
    freopen(INPUT_FILE, "r", stdin);
	freopen(OUTPUT_FILE, "w+", stdout);
    
    unsigned int T, t, N, n;
    fString lines [100];
    
    cin >> T;
    
    // For each test case
    for (t = 0; t < T; t++)
    {
        int nmoves = 0;
        bool possible = false;
        bool solved = false;
        char cChar;
        
        cin >> N;
        for (n = 0; n < N; n++)
        {
            cin >> lines[n].s;
            lines[n].i = 0;
            lines[n].l = (unsigned int)lines[n].s.length();
        }
        
        while (!solved)
        {
            vector<unsigned int> vCounters;
            if (lines[0].i < lines[0].l)
                cChar = lines[0].s[lines[0].i];
            else
            {
                // are we finished
                for (int i = 1; i < N; i++)
                {
                    if (lines[i].i < lines[i].l)
                    {
                        goto print_solution;
                    }
                }
                possible = true;
                goto print_solution;
            }
            
            for (int i = 0; i < N; i++)
            {
                unsigned int numLetters = getNumEqualLetters(cChar,&lines[i]);
                vCounters.push_back(numLetters);
            }
            sort(vCounters.begin(),vCounters.end());
            
            if (vCounters[0]==0)
            {
                // All finished?
                for (int i = 1; i < N; i++)
                {
                    if (vCounters[i] != 0)
                    {
                        goto print_solution;
                    }
                }
                possible = true;
                goto print_solution;
            }
            
            // Solve
            
            for (int j = N-1; j>0; j--)
            {
                if ( vCounters[j] == vCounters[j-1] ) continue;
                
                if ( N - j > j )
                {
                    nmoves += j;   // add letters
                    for (int k = j - 1; k > -1; k--)
                    {
                        vCounters[k]++;
                    }
                }
                else
                {
                    nmoves += N-j; // remove letters
                    for (int k = j; k < N; k++)
                    {
                        vCounters[k]--;
                    }
                }
                j++; // Try again with the same counter
            }
        }
        
    print_solution:
        
        cout << "Case #" << t+1 << ": ";
        if (possible)
        {
            cout << nmoves << endl;
        }
        else
        {
            cout << "Fegla Won" << endl;
        }
    }
    return 0;
}