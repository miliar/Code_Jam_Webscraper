#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <list>
#include <ctime>
#include <vector>
#include <fstream>
#include <algorithm>
#include <iomanip>
#define  epsilon 1e-5
#include <list>
#include <queue>
#include <stack>
#include <deque>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <hash_set>
#include <hash_map>

using namespace std;

bool isValid(string a)
{
    bool seen[26];
    for(int i = 0; i < 26; i++)seen[i] = 0;

    for(int i = 0; i < a.length(); i++)
    {
        if(seen[a[i] - 'a'])return false;

        seen[a[i] - 'a'] = 1;
        char t = a[i];
        while(a[i] == t && i < a.length())
        {
            i++;
        }
        i--;
    }
    return true;
}

string concatenate(string a[], int len)
{
    string ret;
    for(int i = 0; i < len; i++)
    {
        ret = ret + a[i];
    }
    return ret;
}

void factorial(int fact[], int n)
{
    fact[0] = 0;
    fact[1] = 1;
    for(int i = 2; i <= n; i++)
        fact[i] = i*fact[i - 1];
}

int main()
{
    ofstream out("output.txt");
    int tcase;
    cin >> tcase;
    int rez[tcase];

    for(int i = 0; i < tcase; i++)
    {
        int n;
        cin >> n;
        string a[n];
        int fact[n];
        int cnt = 0;
        factorial(fact, n);

        for(int j = 0; j < n; j++)cin >> a[j];
        int tt = fact[n];

        for(int j = 0; j < tt; j++)
        {
             next_permutation(a, a + n);
            if( isValid( concatenate(a, n) ) ) cnt++;
        }
        rez[i] = cnt;
    }

    for(int i = 0; i < tcase; i++)
        out << "Case #" << i + 1 << ": " << rez[i] << endl;
}
