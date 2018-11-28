#include <iostream>
#include <cstdio>
#include <set>
#include <string>
#include <iterator>
#include <algorithm>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
    freopen("B-small-attempt0.in","r",stdin); //输入重定向，输入数据将从in.txt文件中读取
    freopen("B-small-attempt0.out","w",stdout); //输出重定向，输出数据将保存在out.txt文件中

    int i, j, k;
    double C, F, X, V;
    int number;
    cin >> number;

    for (i = 0; i < number; i ++) {
        cin >> C;
        cin >> F;
        cin >> X;

        V = 2;

        double minTime = X / V;
        double T = 0, T2;
        for (j = 0; j < 10000; j ++) {
            T += C / (V + (j * F));
            T2 = X / (V + (j + 1) * F);
            minTime = min(minTime, T + T2);
        }

        cout << "Case #" << i + 1 << ": " << setiosflags(ios::fixed) << setprecision(7) << minTime << endl;
    }
    return 0;
}
