#include <iostream>
#include <string>
#include <cstring>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <vector>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <iomanip>
#include <fstream>
#include <ctime>
#define pb push_back
typedef long long int i64;
typedef unsigned long long u64;
using namespace std;
ifstream fin("a.in");
ofstream fout("a.out");
int T;
vector<string> answers;
void read()
{
    int c1[4][4], c2[4][4];
    int answer1, answer2;
    fin >> answer1;
    for(int i = 0; i < 4; ++i)
    {
        for(int j = 0; j < 4; ++j)
        {
            fin >> c1[i][j];
        }
    }
    fin >> answer2;
    for(int i = 0; i < 4; ++i)
    {
        for(int j = 0; j < 4; ++j)
        {
            fin >> c2[i][j];
        }
    }
    vector<int> uniques;
    for(int i = 0; i < 4; ++i)
    {
        for(int j = 0; j < 4; ++j)
        {
            if(c1[answer1-1][i] == c2[answer2-1][j])
            {
                uniques.pb(c1[answer1-1][i]);
            }
        }
    }
    if(uniques.size() == 0)
    {
        answers.pb("Volunteer cheated!");
    }
    else if(uniques.size() == 1)
    {
        string ans = "";
        if(uniques[0] > 9)
            ans += (uniques[0] / 10 + '0');
        ans += (uniques[0] % 10 + '0');
        answers.pb(ans);
    }
    else answers.pb("Bad magician!");
}
int main()
{
    ios::sync_with_stdio(false);
    fin >> T;
    for(int i = 0; i < T; ++i)
    {
        read();
    }
    for(int i = 0; i < T; ++i)
    {
        fout<<"Case #"<<i+1<<": "<<answers[i]<<"\n";
    }
    return 0;
}
