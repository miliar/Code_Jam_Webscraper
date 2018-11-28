#include <iostream>
#include <set>
#include <stack>
#include <vector>
#include <algorithm>
#include <string.h>
using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int test = 1; test <= T; ++test)
    {
        int n, X;
        cin >> n >> X;

        multiset<int> files;
        for (int i = 0; i < n; ++i)
        {
            int fileSize;
            cin >> fileSize;
            files.insert(fileSize);
        }

        int res = 0;
        do
        {
            set<int>::iterator it = files.end();
            int largeFile = *files.rbegin();
            files.erase(--it);

            int spaceRemains = X - largeFile;

            it = lower_bound(files.begin(), files.end(), spaceRemains);

            if (it == files.end())
            {
                if (!files.empty())
                {
                    files.erase(--it);
                }
            }
            else
            {
                if (*it == spaceRemains || it != files.begin())
                {
                    if (*it > spaceRemains) --it;
                    files.erase(it);
                }
            }

            ++res;
        }
        while (!files.empty());

        cout << "Case #" << test << ": " << res << endl;
    }

    return 0;
}
