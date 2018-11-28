#include <algorithm>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

void work(ifstream &fin, int caseno)
{
    int n;
    string s;
    fin >> n;
    fin >> s;
    int sum = 0;
    int ans = 0;
    for (int i = 0; i <= n; ++i) {
        int cnt = i - sum;
        if (cnt > 0) {
            ans += cnt;
            sum += cnt;
        }
        sum += s[i] - '0';
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
