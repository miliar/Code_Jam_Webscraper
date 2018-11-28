#include <algorithm>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int T = 0;
    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        int N = 0;
        cin >> N;

/*        vector<pair<int, char>> parties;
        for (int i = 0; i < N; ++i)
        {
            int p = 0;
            cin >> p;
            parties.push_back(make_pair(p, 'A' + i));
        }

        sort(parties.rbegin(), parties.rend());
*/

        vector<int> parties;
        copy_n(istream_iterator<int>(cin), N, back_inserter(parties));

        cout << "Case #" << (i + 1) << ": ";

        int max = *max_element(parties.begin(), parties.end());
        while (max > 0)
        {
            vector<int> maxElems;
            for (int i = 0; i < parties.size(); ++i)
            {
                if (parties[i] == max)
                    maxElems.push_back(i);
            }

            if (maxElems.size() % 2)
            {
                cout << static_cast<char>('A' + maxElems[0]) << ' ';
                --parties[maxElems[0]];
            }

            for (int i = maxElems.size() % 2 ? 1 : 0; i < maxElems.size(); i += 2)
            {
                cout << static_cast<char>('A' + maxElems[i]) << static_cast<char>('A' + maxElems[i + 1]) << ' ';
                --parties[maxElems[i]];
                --parties[maxElems[i + 1]];
            }

/*            string output;
            for (size_t i = 0; i < parties.size(); ++i)
            {
                if (parties[i] == max)
                {
                    output += 'A' + i;
                    --parties[i];
                    if (output.size() == 2)
                    {
                        cout << output << ' ';
                        output.clear();
                    }
                }
            }
            if (!output.empty())
                cout << output << ' ';
*/
            max = *max_element(parties.begin(), parties.end());
        }

/*        while (parties[0].first > 0)
        {
            int max = parties[0].first;
            for (size_t i = 0; i < parties.size() && parties[i].first == max; i += 2)
            {
                cout << parties[i].second;
                --parties[i].first;
                if (i < parties.size() - 1)
                {
                    cout << parties[i + 1].second;
                    --parties[i + 1].first;
                }
                cout << ' ';
            }
        }
*/
        cout << '\n';
    }

    return 0;
}

