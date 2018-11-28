#include <iostream>

using namespace std;

int main() {
//    cout << "Hello, World!" << endl;

//    freopen("input.txt","r",stdin);
//    freopen("output.txt","w",stdout);

    int t;
    cin >> t;
    for(int tc = 1; tc <= t; tc++)
    {
        long n;
        cin >> n;
        int remaining = 10;
        if(n == 0)
            cout << "Case #" << tc << ": " << "INSOMNIA" << endl;
        else
        {
            int marked[10] = {0};
            long nextValue = 0;

            while(remaining > 0)
            {
                nextValue += n;
                long value = nextValue;

                while(value > 0)
                {
                    int nr = value % 10;
                    value = value/10;
                    if(marked[nr] == 0)
                        remaining--;
                    marked[nr]++;
                }
            }

            cout << "Case #" << tc << ": " << nextValue << endl;

        }
    }

    return 0;
}