#include<fstream>
#include<iostream>
#include<algorithm>
#include<cassert>
using namespace std;

// 0: 1 / 1: i / 2: j / 3: k / 4: -1 / 5: -i / 6: -j / 7: -k
int mult_table[8][8] = 
 {{0, 1, 2, 3, 4, 5, 6, 7},
  {1, 4, 3, 6, 5, 0, 7, 2},
  {2, 7, 4, 1, 6, 3, 0, 5},
  {3, 2, 5, 4, 7, 6, 1, 0},
  {4, 5, 6, 7, 0, 1, 2, 3},
  {5, 0, 7, 2, 1, 4, 3, 6},
  {6, 3, 0, 5, 2, 7, 4, 1},
  {7, 6, 1, 0, 3, 2, 5, 4}};

long long l;
long long x;
int s[10000];

bool run()
{
    cin >> l >> x;
    char t;
    for (int i = 0; i < l; i += 1)
    {
        cin >> t;
        s[i] = (t - 'i') + 1;
    }

    long long first_i = -1;
    long long last_k = -1;

    int cnt = 0;
    for (long long i = 0; i < min(4ll,x)*l && first_i == -1; i += 1)
    {
        cnt = mult_table[cnt][s[i % l]];
        if (cnt == 1)
            first_i = i+1;
    }
    cnt = 0;
    for (long long j = x*l-1; j >= max(0ll,x-4)*l && last_k == -1; j -= 1)
    {
        cnt = mult_table[s[j % l]][cnt];
        if (cnt == 3)
            last_k = j;
    }

    if (first_i == -1 || last_k == -1)
        return false;

    if (first_i >= last_k)
        return false;

    if (last_k - first_i < l)
    {
        int middle = 0;
        for (long long i = first_i; i < last_k; i += 1)
        {
            middle = mult_table[middle][s[i % l]];
        }
        return middle == 2;
    }
    else
    {
        int middle_a = 0;
        int middle_b = 0;
        int middle_c = 0;

        while (first_i % l != 0)
        {
            middle_a = mult_table[middle_a][s[first_i % l]];
            first_i += 1;
        }
        while (last_k % l != 0)
        {
            middle_c = mult_table[s[(last_k-1) % l]][middle_c];
            last_k -= 1;
        }
        assert ((last_k - first_i) % l == 0);

        int f = (last_k - first_i) / l;
        int total = 0;
        for (int i = 0; i < l; i += 1)
        {
            total = mult_table[total][s[i]];
        }
        for (int j = 0; j < f; j += 1)
        {
            middle_b = mult_table[middle_b][total];
        }

        return mult_table[middle_a][mult_table[middle_b][middle_c]] == 2;
    }
}


int main()
{
    int tc;
    cin >> tc;
    for (int i = 0; i < tc; i += 1)
    {
        cout << "Case #" << (i+1) << ": " << (run() ? "YES" : "NO") << "\n";
    }
}
