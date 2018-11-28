#include <iostream>
#include <iomanip>

using namespace std;

enum {
    MAX_CACHE = 100000
};

int main() {
    int count = 0, cases;
    cout << fixed << setprecision(7);

    cin >> cases;
    while (count < cases) {
        double cache[MAX_CACHE] = {0};
        double c, f, x;
        
        cin >> c >> f >> x;
        int k = (int) (x / c - 2 / f);
        k = k < 0 ? 0 : k;
        // cerr << "k=" << k << endl;
        // prepare sum(c/(2+i*f),{i,0,k-1})
        cache[0] = c / 2;
        for (int i=0; i<k; i++) {
            cache[i+1] = cache[i] + c / (2.0  + (i+1) * f);
        }

        double result;
        if (k > 0)
            result = cache[k-1] + (x / (2 + k * f));
        else
            result = (x / (2 + k * f));

        if (result > (cache[k] + x / (2 + (k+1) * f)))
            cerr << "ERROR1: " << c << ", " << f << ", " << x << " > " << (cache[k] + x / (2 + (k+1) * f)) << endl;
        if (k > 0)
            if (result > (cache[k-2] + x / (2 + (k-1) * f)))
                cerr << "ERROR2: " << c << ", " << f << ", " << x << " > " << (cache[k] + x / (2 + (k+1) * f)) << endl;

        cout << "Case #" << ++count << ": " << result << endl;
    }

    return 0;
}
