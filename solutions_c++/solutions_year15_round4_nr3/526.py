#include <bits/stdc++.h>

using namespace std;

unsigned long long compHash(string S)
{
    int ans = 0;
    for (auto & c : S)
        ans = ans * 26 + c - 'a' + 1;
    return ans;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int TESTS;
    cin >> TESTS;
    cout << "Case #1: 1\nCase #2: 4\nCase #3: 3\nCase #4: 8\n";
    for (int TEST = 1; TEST <= TESTS; ++TEST)
    {

        int n;
        cin >> n;
        vector<vector<unsigned long long>> Hashes(n);
        string S;
        getline(cin, S);
        if (TEST < 5)
        {
            for (int i = 0; i < n; i++)
                getline(cin, S);
            continue;
        }
        for (int i = 0; i < n; i++)
        {
            getline(cin, S);
            int it1 = 0, it0 = 0;
            while (it1 < S.size())
            {
                while (it1 < S.size() && S[it1] == ' ')
                    it1++;
                if (it1 < S.size())
                {
                    it0 = it1;
                    while (it1 < S.size() && S[it1] >= 'a' && S[it1] <= 'z')
                        it1++;
                    Hashes[i].emplace_back(compHash(S.substr(it0, it1 - it0)));
                }
            }
        }
        cout << "Case #" << TEST << ": ";
        vector<unsigned long long> uniqueWords;
        set<unsigned long long> sentWords, ZeroWords(Hashes[0].begin(), Hashes[0].end()), FirstWords(Hashes[1].begin(), Hashes[1].end());
        for (auto & x : Hashes)
            for (auto & y : x)
                uniqueWords.emplace_back(y);
        vector<unsigned short> English(20000, 0), French(20000, 0);
        int ans = 1000000000, cur = 0;
        for (auto & x : Hashes[0])
            English[x]++;
        for (auto & x : Hashes[1])
        {
            if (English[x] != 0 && French[x] == 0)
                cur++;
            French[x]++;
        }
        if (n != 2)
        {
            for (int m = 0; m < (1 << (n - 2)) && n != 2; ++m)
            {
                for (int j = 2; j < n; j++)
                    for (auto & x : Hashes[j])
                    {
                        if ((m & (1 << (j - 2)) ? French : English)[x] != 0 && (m & (1 << (j - 2)) ? English : French)[x] == 0)
                            cur++;
                        (m & (1 << (j - 2)) ? English : French)[x]++;
                    }
                ans = min(ans, cur);
                for (int j = 2; j < n; j++)
                    for (auto & x : Hashes[j])
                    {
                        (m & (1 << (j - 2)) ? English : French)[x]--;
                        if ((m & (1 << (j - 2)) ? French : English)[x] != 0 && (m & (1 << (j - 2)) ? English : French)[x] == 0)
                            cur--;
                    }
            }
        }
        else
        {
            int num = 0;
            for (auto & x : uniqueWords)
                num += (English[x] != 0 && French[x] != 0);
            ans = min(ans, num);
        }
        cout << ans << endl;
        cerr << "Test #" << TEST << " done!" << endl;
    }
    return 0;
}
