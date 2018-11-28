#include <iostream>
#include <string>
#include <cassert>
#include <vector>

using namespace std;

vector<int> find_consecutive_consonants(const string &s, int N)
{
    vector<int> ret;
    for (size_t i = 0; i <= s.size() - N; ++i)
    {
        bool found = true;
        for (int j = 0; j < N; ++j)
        { 
            switch (s[i + j])
            {
                case 'a': case 'e': case 'i': case 'o': case 'u':
                    found = false;
                    break;
            }
        }
        if (found)
            ret.push_back(i);
    }
    return ret;
}

int calc_n_value(const string &s, int N)
{
    int count = 0;
    vector<int> cc = find_consecutive_consonants(s, N);
    int len = s.size();
    for (int s = 0; s <= len - N; ++s)
    {
        for (int e = N; e <= len; ++e)
        {
            for (size_t i = 0; i < cc.size(); ++i)
            {
                if (s <= cc[i] && cc[i] + N - 1 < e)
                {
                    count += 1;
                    break;
                } 
            }
        }
    }

    return count;
}

void test()
{
    {
        string s = "quartz";
        vector<int> v = find_consecutive_consonants(s, 3);
        cout << v.size() << endl;
        assert(1 == v.size());
        assert(3 == v[0]);
        assert(4 == calc_n_value(s, 3));
    }

    {
        string s = "straight";
        vector<int> v = find_consecutive_consonants(s, 3);
        cout << v.size() << endl;
        assert(2 == v.size());
        assert(0 == v[0]);
        assert(5 == v[1]);
        assert(11 == calc_n_value(s, 3));
    }

    {
        string s = "gcj";
        vector<int> v = find_consecutive_consonants(s, 2);
        cout << v.size() << endl;
        assert(2 == v.size());
        assert(0 == v[0]);
        assert(1 == v[1]);
        assert(3 == calc_n_value(s, 2));
    }

    {
        string s = "tsetse";
        vector<int> v = find_consecutive_consonants(s, 2);
        cout << v.size() << endl;
        assert(2 == v.size());
        assert(0 == v[0]);
        assert(3 == v[1]);
        assert(11 == calc_n_value(s, 2));
    }
}

int main()
{
//    test();
    int T, N;
    string name;
    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        cin >> name >> N;
        cout << "Case #" << i + 1 << ": " << calc_n_value(name, N) << endl;
    }
    return 0;
}




