#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <iterator>
using namespace std;

#define REP(i,N) for (int i = 0; i < N; ++i)

//cout.precision(6);
//cout.setf( std::ios::fixed, std:: ios::floatfield ); // floatfield set to fixed

typedef unsigned long long int ulli;
typedef unsigned int ui;
typedef long long ll;

typedef vector<int> vi;

int dWar(vector<double> a, vector<double> b)
{
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

//    cout.precision(6);
//    cout.setf( std::ios::fixed, std:: ios::floatfield ); // floatfield set to fixed
    
//    copy(a.begin(), a.end(), ostream_iterator<double>(cout, " ")); cout << endl;
//    copy(b.begin(), b.end(), ostream_iterator<double>(cout, " ")); cout << endl;
    
    int res = 0;
    int N = a.size();
    int bIx = 0;
    
    REP(i, N)
    {
        if (a[i] > b[bIx])
        {
            res++;
            bIx++;
        }
    }

    return res;
}

int war(vector<double> a, vector<double> b)
{
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    
    int N = a.size();
    int bPos = 0;
    
    REP(i,N)
    {
        double aTest = a[i];
        while (bPos < N && b[bPos] < aTest)
        {
            bPos++;
        }
        if (bPos >= N)
        {
            return N - i;
        }
        bPos++;
    }
    
    return 0;
}

int main()
{
    int caseCount;
    cin >> caseCount;
    
    for (int csIx = 1; csIx <= caseCount; ++csIx)
    {
        int N;
        cin >> N;
        vector<double> a(N), b(N);
        REP(i,N)
        {
            cin >> a[i];
        }
        REP(i,N)
        {
            cin >> b[i];
        }
        cout << "Case #" << csIx << ": " << dWar(a,b) << " " << war(a,b) << endl;
    }
    
    return 0;
}
