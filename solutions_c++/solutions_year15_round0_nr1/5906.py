#include <iostream>
#include <string>
#include <vector>
#include <string>
#include <set>
#include <cmath>
#include <map>
#include <list>
#include <algorithm>
#include <utility>

using namespace std;

int main()
{
    unsigned int N;
    cin >> N;
    for(int n = 1; n <= N; ++n)
    {
        unsigned int smax;
        cin >> smax;
        string str;
        vector<unsigned int> ss(smax + 1, 0);
        cin >> str;
        for(int i = 0; i < smax + 1; ++i)
        {
            ss[i] = str[i] - 48;
        }
        unsigned int up = 0;
        unsigned int need = 0;
        for(int i = 0; i < smax + 1; ++i)
        {
            if(i > up)
            {
                need += i - up;
                up = i;
            }
            up += ss[i];
        }
        cout << "Case #" << n << ": " << need << endl;
    }
    return 0;
}
