#include <iostream>
#include <algorithm>

using namespace std;

vector<int> sizes;

int min(int a, int b)
{
    return a < b ? a : b;
}

int solve(int c_size, size_t pos)
{
    if(pos == sizes.size() - 1) return c_size > sizes[pos] ? 0 : 1;

    if(c_size > sizes[pos]) return solve(c_size + sizes[pos], pos + 1);

    if(c_size == 1) return 1 + solve(c_size, pos + 1);

    return 1 + min(solve(c_size, pos + 1),
                   solve(c_size+c_size-1, pos));
}

int main()
{
    int case_n;
    cin >> case_n;
    for(int c = 1; c <= case_n; ++c)
    {
        int c_size;
        int mote_number;
        int s;
        cin >> c_size;
        cin >> mote_number;
        sizes.clear();
        for(int i = 0; i < mote_number; ++i)
        {
            cin >> s;
            sizes.push_back(s);
        }

        sort(sizes.begin(), sizes.end());

        cout << "Case #" << c << ": " << solve(c_size, 0) << endl;
    }
    return 0;
}
