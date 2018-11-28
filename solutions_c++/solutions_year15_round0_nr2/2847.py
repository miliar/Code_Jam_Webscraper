#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;

void work(ifstream &fin, int caseno)
{
    int n;
    fin >> n;
    int p[1000];
    for (int i = 0; i < n; ++i) {
        fin >> p[i];
    }
    sort(p, p + n);

    int ans = p[n - 1];
    for (int i = p[n - 1]; i > 0; --i) {
        int cnt = i;
        for (int j = n - 1; j >= 0; --j) {
            if (p[j] <= i)
                break;
            cnt += (p[j] + (i - 1)) / i - 1; 
            if (cnt > ans)
                break;
        }
        if (cnt < ans)
            ans = cnt;
    }

    cout << "Case #" << caseno << ": " << ans << endl;
}

int main()
{
    ifstream fin;
    fin.open("input");
    int n;
    fin >> n;
    for (int i = 0; i < n; ++i) {
        work(fin, i + 1);
    }
    fin.close();
    return 0;
}
