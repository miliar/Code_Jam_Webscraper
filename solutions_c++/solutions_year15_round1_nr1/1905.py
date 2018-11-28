#include <fstream>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main (void)
{
    ifstream in("A.in");
    ofstream out("A.op");

    cout.rdbuf(out.rdbuf());

    int T;
    in >> T;

    for (int t = 1; t <= T; t++)
    {
        int N;
        in >> N;
        vector<long> M(N);

        for(int i = 0; i < N; i++)
        {
            in >> M[i];
        }

        // method 1

        long minAte1 = 0;
        long maxDif = 0;
        

        for (int i = 1; i < N; i++)
        {
            long dif = M[i] - M[i-1];
            if (dif < 0)
            {
                minAte1 -= dif;
                if (-dif > maxDif)
                {
                    maxDif = -dif;
                }
            }
        }

        // method 2: 
        
        long minAte2 = 0;

        for (int i = 0; i < N-1; i++)
        {
            if (M[i] < maxDif)
            {
                minAte2 += M[i];
            }
            
            else
            {
                minAte2 += maxDif;
            }
        }       
        
        
        cout << "Case #" << t << ": " << minAte1 << " " << minAte2 << endl;

    }    

    return 0;
}
