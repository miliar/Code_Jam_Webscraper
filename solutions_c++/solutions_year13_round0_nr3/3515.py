#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ofstream f("a.txt");
    int a[] = {1, 4, 9, 121, 484};
    int t;
    cin >> t;
    int k = 1;
    while (t--) {
        int x,b;
        cin >> x >> b;
        int c = 0;
        for (int i = 0; i < 5; i++) {
            if (a[i] <= b && a[i] >= x)
                c++;
        }
        cout << "Case #" << k++ << ": " << c << endl;
        f << "Case #" << k - 1 << ": " << c << endl;
    }
    return 0;
}
