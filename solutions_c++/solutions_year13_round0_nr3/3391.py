#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

bool p(long long k)
{
    string s;
    stringstream ss;
    ss << k;
    ss >> s;
    int n = s.length();
    for (int i = 0; i < n / 2; i++)
        if (s[i] != s[n - 1 - i])
            return false;
    return true;
}
vector<long long> res;

int main()
{
    long long N = 10000000;
    for (long long i = 1; i <= N; i++)
        if (p(i) && p(i * i))
            res.push_back(i * i);
    sort(res.begin(), res.end());

    int n;
    cin >> n;
    for (int cs = 1; cs <= n; cs++)
    {
        int A, B;
        cin >> A >> B;
        int s = lower_bound(res.begin(), res.end(), A) - res.begin();
        int t = upper_bound(res.begin(), res.end(), B) - res.begin();
        cout << "Case #" << cs << ": " << t - s << endl;
    }
    return 0;
}
