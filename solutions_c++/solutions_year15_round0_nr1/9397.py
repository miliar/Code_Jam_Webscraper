#include <iostream>
#include <cstdio>

using namespace std;

int main(){
    int T, max, req, sum, i, c;
    string audience;
    cin>>T;
    for (c=1;T--;++c) {
        cin>>max>>audience;
        req = 0;
        sum = audience[0] - '0';
        for (i=1;i<=max;++i) {
            if (sum < i) {
                req += i - sum;
                sum = i;
            }
            sum += audience[i] - '0';
        }
        printf("Case #%d: %d\n", c, req);
    }
}
