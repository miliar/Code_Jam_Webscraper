#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
        int T;
        cin >> T;
        for (int i = 0; i < T; i++)
        {
                double C,F,X;
                cin >> C >> F >> X;
                double K = F*(X-C)/C;
                K = (K-2)/F;
                int n = (int)K;
                if (K - double(n) > 0)
                        n++;
                //cout << n << endl;
                double time = 0;
                double speed = 2;
                for (int j = 0; j < n; j++)
                {
                        time += C/speed;
                        speed += F;
                        //cout << time << " " << speed << endl;
                }
                time += X/speed;
                cout.setf(ios::fixed);
                cout<<"Case #" << i + 1 << ": " << setprecision(7)<<time<<endl;
        }
        return 0;
}
