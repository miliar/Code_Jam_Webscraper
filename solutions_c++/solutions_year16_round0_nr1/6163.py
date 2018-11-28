#include <iostream>
#include <set>
#include <string>
#define INF 4294967296 
using namespace std;
int main()
{
    int T;
    cin >> T;
    for(int i = 1 ; i <= T ; i++) {
        set<char> seen;
        int N;
        cin >> N;
        if(N == 0) {
            cout << "Case #" << i << ": INSOMNIA" << endl;
            continue;
        }
        for(long j = N ; j < INF; j += N) {
            string to_str = to_string(j);
            const char * cstr = to_str.c_str();
            while(*cstr != '\0') {
                seen.insert(*cstr);
                ++cstr;
            }
            if(seen.size() == 10) {
                cout << "Case #" << i << ": " << to_str << endl;
                break;
            }
        }
        if(seen.size() != 10) {
            cout << "Case #" << i << ": INSOMNIA" << endl;
        }
    }
}
