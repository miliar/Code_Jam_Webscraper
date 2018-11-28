#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

#define LEN 110

vector< vector<char> > fns;

void square_and_add(vector<char> pal)
{

    vector<char> square(LEN, 0);
    for(int i = 0; i < LEN / 2; i++) for(int j = 0; j < LEN / 2; j++)
    {
        square[LEN - 1 - i - j] += pal[LEN - 1 - i] * pal[LEN - 1 - j];
    }
    fns.push_back(square);
}

vector<char> half;

vector<char> get_pal(bool odd)
{
    vector<char> pal = vector<char>(LEN, 0);
    int pos = LEN - half.size() * 2 + (odd == true);
    for(int i = 0; i < half.size(); i++) pal[pos++] = half[i];
    for(int i = half.size() - 1 - (odd == true); i >= 0; i--) pal[pos++] = half[i];
    return pal;
}

void rec(int pos, int square_sum)
{
    int d_start = (pos == 0 ? 1 : 0);
    if(pos == half.size() - 1)
    {
        for(int d = d_start; d < 10; d++)
        {
            half[half.size() - 1] = d;
            if(square_sum * 2 + d * d < 10) square_and_add(get_pal(true));
            if(square_sum * 2 + d * d * 2 < 10) square_and_add(get_pal(false));
        }
    }
    else
    {
        for(int d = d_start; square_sum + d * d < 5; d++)
        {
            half[pos] = d;
            rec(pos + 1, square_sum + d * d);
        }
    }
}

void prepare()
{
    for(int len = 1; len <= 25; len++)
    {
        half = vector<char>(len);
        rec(0, 0);
    }
    sort(fns.begin(), fns.end());
}

vector<char> string_to_vector(string s)
{
    vector<char> v(LEN, 0);
    for(int i = 0; i < s.size(); i++) v[LEN - s.size() + i] = int(s[i] - '0');
    return v;
}

int solve(string A, string B)
{
    vector<char> a = string_to_vector(A), b = string_to_vector(B);
    return int(upper_bound(fns.begin(), fns.end(), b) - lower_bound(fns.begin(), fns.end(), a));
}

int main()
{
    prepare();
    freopen("Clarge2.in", "r", stdin);
    freopen("Clarge2.out", "w", stdout);
    int T = 0;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        string A, B;
        cin >> A >> B;
        cout << "Case #" << i << ": " << solve(A, B) << endl;
    }
}
