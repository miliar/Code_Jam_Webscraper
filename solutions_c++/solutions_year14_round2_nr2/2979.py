#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    int T;
    cin >> T;
    int A,B,K;
    long count;
    for(int t =1; t <= T;t++)
    {
        count =0;
        cin >> A >> B >> K;
        for(int a = 0;a < A;a++ )
        {
            for(int b = 0 ; b < B; b++)
            {
                if((a & b) < K)
                    count++;
            }
        }
        cout << "Case #" << t <<": " << count<<endl;
    }
}
