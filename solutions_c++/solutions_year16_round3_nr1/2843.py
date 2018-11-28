#include <iostream>
#include <tuple>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <map>

#define all(x) (x).begin(), (x).end()
#define Max(a, b) (a) >= (b) ? (a) : (b)
#define miN(a, b) (a) <= (b) ? (a) : (b)
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

using namespace std;

int getMaxPos(vector<int> v)
{
    int max = 0, max_pos = 0, i = 0;
    vector<int>::iterator it = v.begin();
    while(it != v.end())
    {
        if(*it > max)
        {
            max = *it;
            max_pos = i;
        }
        ++i; ++it;
    }
    return max_pos;
}

bool check(vector<int>::iterator begin, vector<int>::iterator end, int total, int& max_pos)
{
    vector<int>::iterator it = begin;
    int max = 0, max_tmp_pos = 0, i=0;
    while(it != end)
    {
        if(*it > max)
        {
            max = *it;
            max_tmp_pos = i;
        }
        if((((float)*it)/total) > ((float)1/2))
        {
            return false;
        }
        ++it; ++i;
    }
    max_pos = max_tmp_pos;
    return true;
}

void process()
{
    int total =0, N = 0;
    int max_pos = 0, max= 0;
    vector<int> senators = vector<int>();

    cin >> N;

    forn(i,N) {
        int p_i = 0;
        cin >> p_i;
        if(p_i > max)
        {
            max = p_i;
            max_pos = i;
        }
        total += p_i;
        senators.push_back(p_i);
    }

    while(total > 0)
    {
        max_pos = getMaxPos(senators);
        --senators[max_pos];
        --total;
        cout << ((char)(max_pos + 65));
        int tmp_mx_pos = getMaxPos(senators);
        --senators[tmp_mx_pos];
        --total;
        if(check(all(senators), total, max_pos))
        {
            cout << ((char)(tmp_mx_pos + 65));
        }
        else
        {
            ++senators[tmp_mx_pos];
            ++total;
        }
        cout << ' ';
    }
    cout << endl;
}

int main(int argc, char* argv[])
{
    int numberOfTestCases = 0;

    scanf("%d", &numberOfTestCases);

    for(int i = 0 ; i< numberOfTestCases ; i++)
    {
        printf("Case #%d: ", i + 1);
        process();
    }
}
