#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

string words[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
vector<pair<int, int> > generateOrder()
{
    map<char, set<int> > rep;
    vector<pair<int, int> > result;
    for (int i = 0; i < 10; i++)
    {
        for(int j = 0; j < words[i].size(); ++j)
        {
            rep[words[i][j]].insert(i);
        }
    }
    while(result.size() != 10)
    {
        for (int j = 0; j < 256; ++j)
        {
            if (rep.count(j) && rep[j].size() == 1)
            {
                int value = *rep[j].begin();
                cerr << (char)  j << endl;
                cerr << words[value] << endl;
                result.push_back(make_pair(j - 'A', value));
                for (int i = 0; i < 256; i++)
                {
                    if (rep.count(i))
                    {
                        rep[i].erase(value);
                    }
                }
                rep.erase(j);
            }
        }
        //cerr << (*rep.begin()).first << endl;
        //cerr << (*rep.begin()).second.size() << endl;
        cerr << "size" <<  rep.size() << endl;
    }
    return result;
}
int main()
{
    vector<pair<int, int> > order = generateOrder();
    int testNum;
    cin >> testNum;
    cerr << testNum;
    for (int i = 0; i < testNum; ++i)
    {
        vector<int> count(26, 0);
        string str;
        cin >> str;
        for (int j = 0; j < str.size(); ++j)
        {
            count[str[j] - 'A']++;
        }
        vector<int> answer;
        for (int j = 0; j < order.size(); ++j)
        {
            int letter = order[j].first;
            int rep = order[j].second;
            while(count[letter] > 0)
            {
                for (int k = 0; k < words[rep].size(); ++k)
                {
                    count[words[rep][k] - 'A']--;
                }
                answer.push_back(rep);
            }
        }
        sort(answer.begin(), answer.end());
        cout << "Case #" << i + 1 << ": ";
        for (int j = 0; j < answer.size(); ++j)
        {
            cout << answer[j];
        }
        cout << endl;
    }
    return 0;
}