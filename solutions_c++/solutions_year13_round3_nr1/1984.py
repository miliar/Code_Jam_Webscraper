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

inline bool is_consonant(char letter)
{
    if ((letter == 'a') ||
        (letter == 'e') ||
        (letter == 'i') ||
        (letter == 'o') ||
        (letter == 'u'))
    {
        return false;
    }
    return true;
}

int find_next_substring(string name, unsigned int c, unsigned int n)
{
    const int end = (int)name.size();
    int num_cons = 0;
    while (c < end)
    {
        if (is_consonant(name[c]))
            num_cons++;
        else
            num_cons=0;
        
        if (num_cons==n)
            return c-(n-1);
        
        c++;
    }
    return -1; // end of string
}

int main(int argc, const char * argv[])
{
    freopen(INPUT_FILE, "r", stdin);
	freopen(OUTPUT_FILE, "w+", stdout);
    
    unsigned int T, t;
    
    cin >> T;
    
    // For each test case
    for (t = 0; t < T; t++)
    {
        string name;
        int n;
        int n_value = 0;
        int length;
        int c = 0;
        int last_index = -1;
        
        cin >> name >> n;
        
        length = (int)name.size();
        
        while (c < length)
        {
            int index = find_next_substring(name, c, n);
            if (index < 0) break;
            
            const int ln = index - (last_index + 1);
            const int rn = length - (index + n);
            n_value += (ln+1) * (rn+1);
            c = index + 1;
            last_index = index;
        }
        
        cout << "Case #" << t+1 << ": " << n_value << endl;
    }
    return 0;
}