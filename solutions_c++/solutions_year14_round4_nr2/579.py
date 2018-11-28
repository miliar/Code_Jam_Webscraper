#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>

using namespace std;

ifstream in("b_large.in");
ofstream out("b_large.out");

/*int inv(const vector <int>& a, int start, int end)
{
    int inversia = 0;
    if (start < 0)
        return 0;
    for (int i = start; i <= end; ++i)
    {
        for (int j = start; j < i; ++j)
            if (a[j] > a[i])
                inversia++;
    }
    return inversia;
}

int invObr(const vector <int>& a, int start, int end)
{
    if (end >= a.size())
        return 0;
    int inversia = 0;
    for (int i = start; i <= end; ++i)
    {
        for (int j = i + 1; j <= end; ++j)
            if (a[j] > a[i])
                inversia++;
    }
    return inversia;
}*/

int tanel(vector <int>& a, int m, int i)
{
    int qanak = 0;
    while (m != i)
    {
        if (i < m)
        {
            swap(a[m], a[m - 1]);
            m--;
        }
        else
        {
            swap(a[m], a[m + 1]);
            m++;
        }
        qanak++;
    }
    return qanak;
}

int main()
{
    int number;
    in >> number;
    for (int t = 1; t <= number; ++t)
    {
        int n;
        in >> n;
        vector <int> v(n);
        int maxim = 0;
        for (int i = 0; i < n; ++i)
        {
            in >> v[i];
            if (v[i] > v[maxim])
                maxim = i;
        }

        int answer = 0, start = 0, end = n - 1;

        while (start < end)
        {
            int minim = start;
            for (int j = start; j <= end; ++j)
                if (v[minim] > v[j])
                    minim = j;

            if (abs(start - minim) < abs(end - minim))
            {
                answer += tanel(v, minim, start);
                start++;
            }
            else
            {
                answer += tanel(v, minim, end);
                end--;
            }
        }


        /*for (int i = 0; i < n; ++i)
        {
            vector <int> a(v);  
            int m = maxim;
            int qanak = 0;
            while (m != i)
            {
                if (i < m)
                {
                    swap(a[m], a[m - 1]);
                    m--;
                }
                else
                {
                    swap(a[m], a[m + 1]);
                    m++;
                }
                qanak++;
            }

            int u1 = inv(a, 0, m - 1);
            int u2 = invObr(a, m + 1, n - 1);

            //cout << t << ": " << qanak << " " << u1 << " " << u2 << endl;

            if (qanak + u1 + u2 < answer || answer == -1)
                answer = qanak + u1 + u2;
        }*/
        
        out << "Case #" << t << ": " << answer << endl;
    }
    return 0;
}