#include <iostream>

using namespace std;

bool seen[20];

int main()
{

    int t; cin >> t;

    for(int i = 1; i <= t; i++){

        int n; cin >> n;

        for(int j = 0; j < 10; j++)
                seen[j] = false;

        int ans = -1;

        for(int j = 1; j <= 10000; j++){
            long long product = 1LL * n * j;

            while(product){
                seen[ product % 10 ] = true;
                product /= 10;
            }

            bool done = true;
            for(int k = 0; k < 10; k++)
            {
                if(!seen[k]) done = false;
            }

            if(done) {
                ans = j;
                break;
            }
        }

        if(ans == -1)
            cout << "Case #" << i << ": INSOMNIA" << endl;
        else
            cout << "Case #" << i << ": " << 1LL * ans * n << endl;

    }
    return 0;
}
