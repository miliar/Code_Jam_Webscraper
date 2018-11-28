#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::string;

#define NDEBUG

#ifndef NDEBUG
#define debug_log cout << "DEBUG_LOG [" << __FILE__ << ":" << __LINE__ << "]: "
#else
#define debug_log if (0) cout
#endif

using std::cin;

int main() {
    int count_testcases;
    cin >> count_testcases;

    for (int i = 0; i != count_testcases; ++i) {
        int shyness_max;
        cin >> shyness_max;

        string audience_shyness;
        cin >> audience_shyness;
        // make sure the length of audience_shyness is (shyness_max + 1)
        audience_shyness = audience_shyness.substr(0, shyness_max + 1);

        debug_log << "audience_shyness readed: " << audience_shyness << endl;

        int count_friends = 0;
        unsigned clapped_audience = audience_shyness[0] - '0';
        for (size_t j = 1; j < audience_shyness.length(); ++j) {
            if (clapped_audience < j) {
                count_friends += j - clapped_audience;
                clapped_audience += j - clapped_audience;
            }
            clapped_audience += audience_shyness[j] - '0';
        }

        cout << "Case #" << i + 1 << ": " << count_friends << endl;
    }
    
    return 0;
}
