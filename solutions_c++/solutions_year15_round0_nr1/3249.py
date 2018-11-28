#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <sstream>

using namespace std;

bool can_standing_ovation(const string &shyness, int start_sum = 0)
{
    int n = shyness.size();
    int sum = start_sum;
    for(int i = 0; i < n; ++i)
    {
        if(sum < i) 
        {
            return false;
        }
        sum += shyness[i] - '0';
    }
    return true;
}

int main(int argc, char *argv[]) {
    int TC;
    string buf;
    getline(cin, buf);
    istringstream in1(buf);
    in1 >> TC;
    
    for(int tc = 1; tc <= TC; ++tc)
    {
        int smax = 0;
        string shyness = "";
        getline(cin, buf);
        istringstream in2(buf);
        in2 >> smax >> shyness;
        
        int m = (smax + 1) * 9;
        int ans = 0;
        for(ans = 0; ans <= m; ++ans)
        {
            if(can_standing_ovation(shyness, ans))
            {
                break;
            }
        }
        cout << "Case #" << tc << ": " << ans << '\n';
    }
    return 0;
}
