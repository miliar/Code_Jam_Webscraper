#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

#include <vector>
#include <queue>
#include <stack>
#include <array>
#include <map>
#include <set>
#include <iterator>
#include <algorithm>
#include <numeric>
#include <functional>

using namespace std;

bool allt(bool flag[10] ){
    for (int i=0; i<10; ++i) {
        if (!flag[i]) return false;
    }
    return true;
}

void pf(bool flag[10] ){
    for (int i=0; i<10; ++i) {
        cout << i << " is " << flag[i] << " ";
    }
    cout << endl;
}

unsigned long long solve(const int & x) {
    bool flag[10] = {0};

//    cout << "x = " << x << endl;
    if (x == 0) return -1;
    unsigned long long y = x;
    unsigned long long z = x;
    for(; y>0; y /= 10) {
        flag[y%10] = true;
    }
//    pf(flag);
    unsigned i = 2;
    while (!allt(flag)) {
        //! all_of(flag.begin(), flag.end(), [](bool i){ return i;} )) {
        if(i>200) return -1;
        y = x * i;
        z = y;
//        cout << "i = " << i << " new y = " << y << endl;
        for(; y>0; y /= 10) flag[y%10] = true;
//        pf(flag);
        ++i;
    }
    return z;
}

int main(int argc, char * argv[])
{
    int t;
    scanf("%d",&t);
    while(t--) {
        int x;
        scanf("%d",&x);
        static int id = 0;
        printf("Case #%d: ",++id);
        int y = solve(x);
        if (y > 0) {
            printf("%d\n", y);
        } else {
            printf("INSOMNIA\n");
        }
    }
    return 0;
}
