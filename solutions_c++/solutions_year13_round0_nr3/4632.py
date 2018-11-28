#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <map>
#include <set>
#include <string>

using namespace std;

ifstream in;
ofstream out;

bool Ispal(long long i)
{
    long long k = 0, j = i, m = 0, b;
    while (j != 0)
    {
        j /= 10;
        ++k;
    }
    j = i;
    --k;
    while (k >= m)
    {
        m++;
        b = i / pow(10, k);
        b %= 10;
        if (b != j % 10)
        {
            return 0;
        }
        j /= 10;
        --k;
    }
    return 1;
}


int binsearch(vector <long long> A, long long B)
{
    long long first = 0;
    long long last = A.size();
    long long mid;
    while (first < last)
    {
        mid = first + (last - first) / 2;
        if (B <= A[mid])
        {
            last = mid;
        }
        else
        {
            first = mid + 1;
        }
    }
    if (A[last] < B)
    {
        ++last;
    }
    return last;
}


int binsearch1(vector <long long> A, long long B)
{
    long long first = 0;
    long long last = A.size();
    long long mid;
    while (first < last)
    {
        mid = first + (last - first) / 2;
        if (B <= A[mid])
        {
            last = mid;
        }
        else
        {
            first = mid + 1;
        }
    }
    if (A[last] > B)
    {
        --last;
    }
    return last;
}

int main()
{
    in.open("input.in");
    out.open("output.txt");
    vector <long long> K;
    long long T;
    for (long long i = 1; i <= 1000000; ++i)
    {
        if (Ispal(i))
        {
            K.push_back(i);
        }
    }
    in >> T;
    for (long long i = 0; i < T; ++i)
    {
        long long A, B, a, b, ans = 0;
        in >> A >> B;
        a = sqrt(A);
        if (sqrt(A) * sqrt(A) != A)
        {
            a++;
        }
        b = (sqrt(B));
        for (long long j = binsearch(K,a); j <= binsearch1(K,b); ++j)
        {
            if (Ispal(K[j] * K[j]) && K[j] * K[j] <= B)
            {
                ++ans;
            }
        }
        out << "Case #" << i + 1 << ": " <<  ans << endl;
    }
}
