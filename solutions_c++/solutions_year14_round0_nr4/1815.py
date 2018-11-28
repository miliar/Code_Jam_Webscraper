#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("D-small-attempt0.in");
ofstream fout("1.out");

int main()
{
    int n; fin >> n;
    for (int t=1; t<=n; t++)    
    {
        int m; fin >> m;
        double a[1010], b[1010];
        for (int i=0; i<m; i++) fin >> a[i];
        for (int i=0; i<m; i++) fin >> b[i];
        sort(a, a+m); sort(b, b+m);
        int index = 0, ans1 = 0, ans2 = 0;
        bool use[1010] = {0};
        for (int i=0; i<m; i++)
        {
            bool flag = 0;
            for (int j=0; j<m; j++)
                if (b[j] > a[i] && !use[j]) { flag = 1; use[j] = 1; break; }
            if (!flag) { ans2 ++; use[index++] = 1; }
        }
        index = 0;   
        for (int i=0; i<m; i++)
        {
            if (a[i] > b[index]) { ans1 ++; index ++; }
        }
        fout << "Case #" << t << ": " << ans1 << ' ' << ans2 << endl;
    }
    //system("pause");
    return 0;
}
