#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <stack>
#include <functional>
#include <fstream>
#include <deque>
#include <queue>
#include <iostream>
#include <fstream>
#include <ctime>
#include <sstream>
#include <climits>

using namespace std;


bool istrue(string s)
{
    int i = 0;
    bool a[257];
    memset(a, false, 257*sizeof(bool));
    while(i < s.size())
    {
        while((i+1 < s.size()) && s[i] == s[i+1] )
        {
            ++i;
        }
        if(a[s[i]])
            return false;
        a[s[i]] = true;
        ++i;
    }
    return true;
}

int main()
{
    ios_base::sync_with_stdio(0);
    fstream in("input.txt");
    fstream out("output.txt");
    int n;
    in >> n;
    for(int i = 1; i <= n; ++i)
    {
        int k;
        in >> k;
        vector<string> a;
        for(int j = 0; j < k; ++j)
        {
            string s;
            in >> s;
            a.push_back(s);
        }
        int *my = new int[15];
        for(int j = 0; j < 15; ++j)
            my[j] = j;
        int ans = 0;
        string answer;
        for(int j = 0; j < k; ++j)
            answer += a[j];
        if(istrue(answer))
            ++ans;
        while(next_permutation(my, my + k))
        {
            string res;
            for(int z = 0; z < k; ++z)
            {
                for(int m = 0; m < k; ++m)
                    if(my[m] == z)
                        res += a[m];
            }
            if(istrue(res))
                ++ans;
        }

        out << "Case #" << i << ": " << ans << endl;
    }
    system("pause");
    return 0;
}