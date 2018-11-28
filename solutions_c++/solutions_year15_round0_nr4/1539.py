#include <iostream>
#include <cstdio>
using namespace std;
int main()
{   int t;

    freopen("output.txt", "w", stdout);
    cin >> t;
    char a[2][8] ={"RICHARD", "GABRIEL"};
    for (int kase = 1; kase <= t; kase++)
    {   int x, r, c;
        cin >> x >> r >> c;
        int ans = 2;
        if (x >= 7) ans = 0;
        else if (r * c % x != 0) ans = 0;
        else if (x > max(r, c)) ans = 0;
        else if (((x-1)/2+1) > r  || ((x-1)/2+1) > c)  ans = 0;
        else
        {  switch(x){
            case 1: ans = 1;
                    break;
            case 2: ans = 1;
                    break;
            case 3: ans = 1;
                    break;
            case 4: if (r > 2 && c > 2)ans = 1;
                    else ans = 0;
                    break;
            default: break;
                    }
        }
        cout << "Case #" << kase << ": " << a[ans] << endl;
    }
    fclose(stdout);

    return 0;
}
