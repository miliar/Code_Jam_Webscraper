// First.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>

using namespace std;

bool isPol (long long n)
{
    vector <long long> pol;
    while (n)
    {
        int k = n % 10;
        n /= 10;
        pol.push_back (k);
    }
    for (int i = 0; i < pol.size () / 2; i++)
        if (pol [i] != pol [pol.size () - i - 1])
            return false;
    return true;
}

int main(int argc, char* argv[])
{
    ifstream in ("data.txt");
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin >> T;
    vector <long long> data;
    for (int i = 0; i < 39; i++)
    {
        long long t;
        in >> t;
        data.push_back (t);
    }
    in.close ();
    for (int k = 0; k < T; ++k)
    {
        int count = 0;
        double n1, m1;
        double sn, sm;
        cin >> n1 >> m1;
        long long n, m;
        sn = sqrt (n1);
        sm = sqrt (m1);
        n = floor (sn);
        m = floor (sm);
        n += (n * n != n1);
        int min = -1, max = -1;
        for (int i = 0; i < 39; i++)
        {
            if ((!(min + 1)) && (n <= data [i]))
                min = i;
            if ((min + 1) && (m >= data [i]))
                max = i;
        }
        if ((min + 1) && (max + 1))
        {
            cout << "Case #" << k + 1 << ": " << max - min + 1 << endl;
        }
        else
            cout << "Case #" << k + 1 << ": 0" << endl;
    }
	return 0;
}

/*bool isPol (long long n)
{
    vector <long long> pol;
    while (n)
    {
        int k = n % 10;
        n /= 10;
        pol.push_back (k);
    }
    for (int i = 0; i < pol.size () / 2; i++)
        if (pol [i] != pol [pol.size () - i - 1])
            return false;
    return true;
}

int main(int argc, char* argv[])
{
//    input.txt
//    1
//    1 100000000000000
    freopen("input.txt","r",stdin);
    freopen("data.txt","w",stdout);
    int T;
    cin >> T;
    for (int k = 0; k < T; ++k)
    {
        int count = 0;
        double n1, m1;
        double sn, sm;
        cin >> n1 >> m1;
        long long n, m;
        sn = sqrt (n1);
        sm = sqrt (m1);
        n = floor (sn);
        m = floor (sm);
        n += (n * n != n1);
        for (long long i = n; i <= m; ++i)
            if ((isPol (i)) && (isPol (i * i)))
                cout << i << endl;
    }
	return 0;
}*/

