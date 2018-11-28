#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <omp.h>

using namespace std;

class Quaternion
{
public:
    Quaternion(int a_, int b_, int c_, int d_) : a(a_), b(b_), c(c_), d(d_)
    {}

    bool isI()
    {
        return a == 0 && b == 1 && c == 0 && d == 0;
    }

    bool isJ()
    {
        return a == 0 && b == 0 && c == 1 && d == 0;
    }

    bool isK()
    {
        return a == 0 && b == 0 && c == 0 && d == 1;
    }

public:
    int a,b,c,d;
};

Quaternion operator*(const Quaternion& q1, const Quaternion& q2)
{
    return Quaternion(q1.a*q2.a - q1.b*q2.b - q1.c*q2.c - q1.d*q2.d,
                      q1.a*q2.b + q1.b*q2.a + q1.c*q2.d - q1.d*q2.c,
                      q1.a*q2.c - q1.b*q2.d + q1.c*q2.a + q1.d*q2.b,
                      q1.a*q2.d + q1.b*q2.c - q1.c*q2.b + q1.d*q2.a);        
}

Quaternion ONE(1,0,0,0);
Quaternion I(0,1,0,0);
Quaternion J(0,0,1,0);
Quaternion K(0,0,0,1);

Quaternion at(string& str, int len, int index)
{
    char c = str.at(index % len);
    switch(c)
    {
    case 'i':
        return I;
    case 'j':
        return J;
    case 'k':
        return K;
    }
    return ONE;
}

#define AT(i) (at(str, len, (i)))

string solve(string str, int times, int len)
{
    int length = times * len;
    Quaternion current = ONE;
    for (int i = 0; i < length; i++)
    {
        current = current * AT(i);
        if (current.isI())
        {
            Quaternion current2 = ONE;
            for (int j = i+1; j < length; j++)
            {
                current2 = current2 * AT(j);
                if (current2.isJ())
                {
                    Quaternion current3 = ONE;
                    for (int k = j+1; k < length; k++)
                    {
                        current3 = current3 * AT(k);                        
                    }
                    if (current3.isK())
                    {
                        return "YES";
                    }
                }
            }
        }
    }
    return "NO";
}

int main_serial()
{
    double start = omp_get_wtime();
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        int len, times;
        cin >> len;
        cin >> times;
        string str;
        cin >> str;
        cout << "Case #" << i+1 << ": " << solve(str, times, len) << endl;
    }
    double end = omp_get_wtime();
    cout << "Time: " << end - start << " seconds." << endl;
    return 0;
}

struct Input
{
    string str;
    int times;
    int len;
};

int main()
{
    //double start = omp_get_wtime();
    int T;
    cin >> T;
    vector<Input> inputs(T);
    for (int i = 0; i < T; i++)
    {
        cin >> inputs[i].len;
        cin >> inputs[i].times;
        string str;
        cin >> inputs[i].str;        
    }
    const int numThreads = 4;
    vector<map<int,string>> results(numThreads);

    #pragma omp parallel for num_threads(numThreads) schedule(dynamic, 1)
    for (int i = 0; i < T; i++)
    {
        int threadId = omp_get_thread_num();
        stringstream ss;
        ss << "Case #" << i+1 << ": " << solve(inputs[i].str, inputs[i].times, inputs[i].len);
        results[threadId][i] = ss.str();
    }

    map<int,string> merge;
    for (int i = 0; i < numThreads; i++)
    {
        merge.insert(results[i].begin(), results[i].end());
    }

    for (auto it = merge.begin(); it != merge.end(); it++)
    {
        cout << it->second << endl;
    }
    //double end = omp_get_wtime();
    //cout << "Time: " << end - start << " seconds." << endl;
    return 0;
}