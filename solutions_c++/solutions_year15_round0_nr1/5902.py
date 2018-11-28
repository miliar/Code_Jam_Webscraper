#include <iostream>
#include <string>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(false);

    int T;

    cin >> T;

    for(int testcase = 0;testcase<T;testcase++)
    {
        int Smatrix[1005];
        int Smax;
        cin >> Smax;

        string instring;
        cin >> instring;

        for(int c = 0;c<= Smax;c++)
        {
            Smatrix[c] = instring[c] - '0';
        }

        int answer = 0;
        int totalstanding = 0;


        for(int Si = 0;Si<=Smax;Si++)
        {
            if(totalstanding >= Si)
            {
                totalstanding = totalstanding + Smatrix[Si];
            }
            else
            {
                answer = answer++;//(Si - totalstanding);
                totalstanding = totalstanding + 1 + Smatrix[Si];
            }
        }

        cout << "Case #" << testcase+1 << ": " << answer << endl;
    }

    return 0;
}
