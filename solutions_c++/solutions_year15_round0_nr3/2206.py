#include <algorithm>
#include <iostream>
using namespace std;

//  1  i  j  k -- 1 2 3 4
// -1 -i -j -k -- 5 6 7 8
int bar(int x, int y)
{
    static int table[4][4] = {{1,2,3,4},{2,5,4,7},{3,8,5,2},{4,3,6,5}};
    int sign = 1;
    if (x > 4) {
        x -= 4;
        sign *= -1;
    }
    if (y > 4) {
        y -= 4;
        sign *= -1;
    }
    int v = table[x-1][y-1];
    if (sign == -1)
        if (v <= 4)
            v += 4;
        else
            v -= 4;
    return v;
}

int find(int L, int X, char *s, int index, int v)
{
    int temp = s[index++%L];
    while (temp != v && index < L*X)
        temp = bar(temp, s[index++%L]);
    return index;
}

int foo(int L, int X, char *s)
{
    if (L*X < 3)
        return 0;
    for (int i = 0; i < L; i++)
        if (s[i] == 'i')
            s[i] = 2;
        else if (s[i] == 'j')
            s[i] = 3;
        else
            s[i] = 4;

    int index = find(L, X, s, 0, 2); // i
    if (index >= L*X) return 0;
    while (index < L*X) {
        int index2 = find(L, X, s, index, 3); // j
        if (index2 >= L*X) return 0;
        while (index2 < L*X) {
            int temp = s[index2%L];
            for (int i = index2+1; i < L*X; i++)
                temp = bar(temp, s[i%L]);
            if (temp == 4) return 1; // k
            index2 = find(L, X, s, index2, 1); // 1
            if (index2 >= L*X) return 0;
        }
        index = find(L, X, s, index, 1); // 1
        if (index >= L*X) return 0;
    }
    return 0;
}

int main()
{
    int *temp = new int[1000000];
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int result = 0;

        int L, X;
        cin >> L >> X;
        char *s = new char[L+1];
        cin.get();
        cin.getline(s, L+1);
        result = foo(L, X, s);
        delete[] s;

        cout << "Case #" << t+1 << ": " << (result==0?"NO":"YES") << endl;
    }
    delete[] temp;
    return 0;
}
