#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;
    
    for(int i = 0; i < T; i++)
    {
            int A, B, K, sum = 0;
            cin >> A >> B >> K;
            
            for(int j = 0; j < A; j++)
                    for(int k = 0; k < B; k++)
                    	if((j&k) < K) sum++;
            cout << "Case #" << i+1 << ": " << sum << endl;
            
    }
    
    return 0;
}
