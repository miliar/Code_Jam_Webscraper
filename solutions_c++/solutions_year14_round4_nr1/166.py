#include<iostream>
#include<algorithm>
using namespace std;

int file[10000],size,used[10000];

int main()
{
    int tt;
    cin >> tt;
    for (int ii = 0; ii < tt; ii++)
    {
        int n;
        memset(used,0,sizeof(used));
        cin >> n >> size;
        for (int i = 0; i < n; i++)
            cin >> file[i];
        sort(file,file + n);
        int ans = 0;
        for (int i = n - 1; i >= 0; i--)
        {
            if (used[i]) continue;
            used[i] = 1;
            int rest = size - file[i];
            int tmp = -1;
            for (int j = 0; j < i; j++)
                if (file[j] <= rest && !used[j])
                    tmp = j;
            if (tmp >= 0) used[tmp] = 1;
            ans++;
        }
        cout << "Case #" << ii + 1 << ": " << ans << endl;
    }
    return 0;
}
