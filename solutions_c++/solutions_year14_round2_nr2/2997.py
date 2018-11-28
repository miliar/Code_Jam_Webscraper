#include <iostream>

using namespace std;

int main()
{
    int a, b, k;
    int t;
    cin >> t;
    for(int z = 1; z<=t; z++)
    {
        cin >> a >> b >> k;
        long long ans = 0;
        for(int i=0; i<a; i++)
            for(int j=0; j<b; j++){
                if((i&j)<k)
                    ans++;
            }
        cout << "Case #" << z << ": " << ans << endl;
    }
}
