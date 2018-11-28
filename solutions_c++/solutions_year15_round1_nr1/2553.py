#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int m[10001];
int main()
{
    int T;
    cin >> T;
    string case_str = "Case #";
    string colon = ": ";
    int count = 1;
    while(T--)
    {
        int N;
        cin >> N;
        long long int method1 = 0;
        long long int method2 = 0;

        cin >> m[0];
        double max_rate = 0;
        for(int i = 1; i < N; i++)
        {
            cin >> m[i];
            if(m[i] < m[i-1])
            {
                method1 += m[i-1] - m[i];
                if(max_rate < (m[i-1] - m[i])/10.0)
                {
                    max_rate = (m[i-1] - m[i])/10.0;
                }
            }
        }
        // method2
        for(int i = 0; i < N-1; i++)
        {
            if(m[i] > 10 * max_rate)
            {
                method2 += 10 * max_rate;
            }
            else
            {
                method2 += m[i];
            }
        }

        cout << case_str << count++ << colon << method1 << " " << method2 << endl;
    }
    return 0;
}
