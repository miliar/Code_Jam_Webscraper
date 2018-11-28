#include <iostream>
#include <cstdint>
#include <vector>
#include <sstream>

using namespace std;

bool isfairs(const string& val)
{
    for(size_t i = 0 ; i < val.size()/2 ; ++i) {
        if(val[i] != val[val.size()-1-i]) {
            return false;
        }
    }
    return true;
}

bool isfair(size_t val)
{
    stringstream ss;
    ss << val;
    return isfairs(ss.str());
}

void mkfairs(std::string s, size_t maxlen, std::vector<size_t>& accum)
{
    // Just ignore those starting with 0s, don't wanna think about it
    // cout << s << endl;
    accum.push_back(strtoul(s.c_str(), 0, 10));

    // Inc the mid.
    size_t mid = s.size()/2 - (s.size() % 2 == 0 ? 1 : 0);
    if(s[mid] - '0' < 9) {
        ++s[mid];
        if(s.size() % 2 == 0) ++s[mid+1];
        mkfairs(s, maxlen, accum);
    } else {
        // Inc the next outer one and zero the mid.
        s[mid] = '0';
        if(s.size() % 2 == 0) s[mid+1] = '0';
        int i = mid-1;
        for( ; i >= 0 ; --i) {
            if(s[i] - '0' < 9) {
                ++s[i];
                ++s[s.size()-i-1];
                break;
            } else {
                s[i] = '0';
                s[s.size()-i-1] = '0';
            }
        }
        // Resize?
        if(i == -1) {
            if(s.size()+1 <= maxlen) {
                if(s.size()+1 > 2) {
                    mkfairs("1" + string(s.size()-1, '0') + "1", maxlen, accum);
                } else {
                    mkfairs(string(s.size()+1, '1'), maxlen, accum);
                }
            }
        } else {
            mkfairs(s, maxlen, accum);
        }
    }
}

int main(int argc, char* argv[])
{
    if(argc == 1) {
        cerr << "Need the upper limit." << endl;
    }

    // First, generate all potential fair numbers in the potential range:
    std::vector<size_t> fairs;
    mkfairs("1", 7, fairs);

    size_t T;
    cin >> T;

    for(size_t i = 0 ; i < T ; ++i) {
        cout << "Case #" << i+1 << ": ";
        size_t lower, upper;
        cin >> lower >> upper;

        size_t count = 0;
        for(size_t fair : fairs) {
            size_t fair2 = fair*fair;
            if(lower <= fair2 && fair2 <= upper && isfair(fair*fair)) {
                count++;
            }
        }
        cout << count << endl;
    }

    return 0;
}
