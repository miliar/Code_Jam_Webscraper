#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

int main()
{
    //freopen("data.in", "rt", stdin);
    //freopen("data.out", "wt", stdout);
    int T, a, b, c;
    scanf("%d", &T);
    for(int i = 1; i <= T; ++i) {
            scanf("%d%d%d", &a, &b, &c);
            cout<< "Case #"<< i << ": ";
            for(int j = 1; j <= c; ++j)
                cout<<j<<' ';
            cout<<'\n';
    }
    return 0;
}
