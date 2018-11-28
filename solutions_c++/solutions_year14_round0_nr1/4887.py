#include <iostream>
#include <cstdio>
#include <set>
#include <string>
#include <iterator>
#include <algorithm>
#include <vector>
using namespace std;



int main() {
    freopen("A-small-attempt0.in","r",stdin); //输入重定向，输入数据将从in.txt文件中读取
    freopen("A-small-attempt0.out","w",stdout); //输出重定向，输出数据将保存在out.txt文件中

    int arrangement1[4][4], arrangement2[4][4];
    int i, j, k;
    int number;
    cin >> number;
    int row1, row2;
    for (i = 0; i < number; i ++) {
        cin >> row1;
        for (j = 0; j < 4; j ++) {
            for (k = 0; k < 4; k ++) {
                cin >> arrangement1[j][k];
            }
        }
        cin >> row2;
        for (j = 0; j < 4; j ++) {
            for (k = 0; k < 4; k ++) {
                cin >> arrangement2[j][k];
            }
        }

        //开始计算啦
        row1 --;
        row2 --;

        set <int> s1, s2;
        vector <int> intersection;

        for (k = 0; k < 4; k ++) {
            s1.insert(arrangement1[row1][k]);
            s2.insert(arrangement2[row2][k]);
        }
        //ostream_iterator <int> (cout, " ")
        set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), back_inserter(intersection));

        if (intersection.size() == 1) {
            cout << "Case #" << i + 1 << ": " << intersection[0] << endl;
        } else if (intersection.size() == 0) {
            cout << "Case #" << i + 1 << ": " << "Volunteer cheated!" << endl;
        } else {
            cout << "Case #" << i + 1 << ": " << "Bad magician!" << endl;
        }
    }

    fclose(stdin);
    fclose(stdout);

    return 0;
}
