#include<fstream>
#include<set>
#include<cmath>
#include<vector>
#include<map>
#include<algorithm>
using namespace std;

long double C, F, X;
long double getIt(long double rate, int limit)
{
    if(limit == 0) return X/rate;
    return C/rate + getIt(rate + F, limit-1);
}
int main()
{
    int T;
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    cin >> T;
    for (int t = 1; t <= T; t++)
    {

        long double rate = 2, t1;
        cin >> C >> F >> X;
        t1 = X/rate;
        long double time = 0;
        for(int limit = 1; time <= t1; limit++)
        {
            time = getIt(rate, limit);
            t1 = min(t1, time);
        }
        cout.precision(10);
        cout.setf( std::ios::fixed, std:: ios::floatfield ); 
        cout <<"Case #" << t << ": " << t1 << endl;
    }
    return 0;
}
