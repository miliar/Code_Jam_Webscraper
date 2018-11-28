#include <iostream>
#include <cstdio>
#include <vector>
#include <sstream>

using namespace std;


int main() {
    int n;
    cin >> n;
    for(int ii = 1; ii<=n; ++ii) {
        int k, c, s;
        cin>> k >> c >> s;
        printf("Case #%d:",ii);
        for(int i = 1; i<=s; ++i)
            printf(" %d",i);
        cout<<endl;
    }
    return 0;
}
