#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int n,f[1000];
vector<pair<int,int> > a;

int left(int index)
{
    int ans = 0;
    for (int i = index + 1; i < n; i++)
        if (a[i].second < a[index].second)
            ans++;
    return ans;
}

int right(int index)
{
    int ans = 0;
    for (int i = index + 1; i < n; i++)
        if (a[i].second > a[index].second)
            ans++;
    return ans;
}

int main()
{
    int tt;
    cin >> tt;
    for (int ii = 0; ii < tt; ii++)
    {
        cin >> n;
        a.clear();
        for (int i = 0; i < n; i++)
        {
            int tmp;
            cin >> tmp;
            a.push_back(make_pair(tmp,i));
        }
        sort(a.begin(),a.end());
        f[0] = min(left(0),right(0));
        for (int i = 1; i < n; i++)
            f[i] = f[i - 1] + min(left(i),right(i));
        cout << "Case #" << ii + 1 << ": " << f[n - 1] << endl;
    }
    return 0;
}
