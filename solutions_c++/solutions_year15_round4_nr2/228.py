#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>

using namespace std;
const int MAXN = 110;

ifstream fin ("B.in");
ofstream fout ("B.out");

int N;
double V, X;
vector <pair <double, double> > lo, hi;

inline bool cmp (pair <double, double> left, pair <double, double> right)
{
    return left.second < right.second;
}

int main()
{
    int T; fin >> T;
    fout << fixed << setprecision(9);
    
    for (int test = 1; test <= T; test++)
    {
        fin >> N >> V >> X;
        lo.clear(); hi.clear();
        
        double tot = 0, flow = 0;
        for (int i = 0; i < N; i++)
        {
            double R, C;
            fin >> R >> C;
            C -= X;
            
            if (abs (C) <= 1e-5)
                flow += R;
            else if (C < 0)
                lo.push_back (make_pair (R, C));
            else
                hi.push_back (make_pair (R, C));
            tot += C * R;
        }
        
        //fout << tot << "\n";
        if (tot < 0)
        {
            tot = -tot;
            swap (lo, hi);
            for (int i = 0; i < lo.size(); i++)
                lo[i].second = -lo[i].second;
            for (int i = 0; i < hi.size(); i++)
                hi[i].second = -hi[i].second;
        }
        
        sort (hi.begin(), hi.end(), cmp);
        
        double diff = 0;
        for (int i = 0; i < lo.size(); i++)
        {
            diff -= lo[i].first * lo[i].second;
            flow += lo[i].first;
        }
        
        for (int i = 0; i < hi.size(); i++)
        {
            if (diff >= hi[i].first * hi[i].second)
            {
                diff -= hi[i].first * hi[i].second;
                flow += hi[i].first;
            }
            else
            {
                flow += (diff / hi[i].second);
                diff = 0;
                break;
            }
        }
        
        fout << "Case #" << test << ": ";
        if (flow <= 1e-5)
            fout << "IMPOSSIBLE\n";
        else
            fout << V / flow << "\n";
    }
    return 0;
}
