#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int n;

    cin >> n;
    double c,f,x,d,t = 0;
    for (int i = 0; i < n; i++){
        cin >> c >> f >> x;
        cout << "Case #" << i+1 << ": ";
        t = 0;
        d = 2;
        while (true) {
            if (x/d <= c/d+x/(d+f)){
                t += x/d;
                break;
            } else {
                t += c/d;
                d += f;
            }
        }
        printf("%.7lf\n",t);

    }

    return 0;
}
