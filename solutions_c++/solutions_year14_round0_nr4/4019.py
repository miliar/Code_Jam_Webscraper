#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int do_war(const vector<double>& v1, const vector<double>& v2) // v1 and v2 are sorted using <
{
    vector<double>::const_iterator iter2 = v2.begin();
    for(int i1=0; i1<v1.size(); i1++)
    {
        iter2 = lower_bound(iter2, v2.end(), v1[i1]);
        if(iter2 == v2.end())
        {
            return v1.size()-i1;
        }
        iter2++;
    }
    return 0;
}

int do_war_dec(const vector<double>& v1, const vector<double>& v2) // v1 and v2 are sorted using >
{
    vector<double>::const_iterator iter2 = v2.begin();
    for(int i1=0; i1<v1.size(); i1++)
    {
        iter2 = lower_bound(iter2, v2.end(), v1[i1], greater<double>());
        if(iter2 == v2.end())
        {
            return i1;
        }
        iter2++;
    }
    return v1.size();
}

int main()
{
    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
    {
        int N;
        cin >> N;
        vector<double> v1(N), v2(N);
        for (int i=0; i<N; i++)
            cin >> v1[i];
        for (int i=0; i<N; i++)
            cin >> v2[i];
        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end());
        vector<double> v1r(v1.rbegin(), v1.rend());
        vector<double> v2r(v2.rbegin(), v2.rend());
        cout << "Case #" << t << ": " << do_war_dec(v1r, v2r) << " " << do_war(v1, v2) << endl;
    }
    return 0;
}
