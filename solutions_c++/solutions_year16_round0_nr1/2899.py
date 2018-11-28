#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

void getCnt(int c, int N){
    if(N == 0){
        cout << "Case #" << c <<": INSOMNIA" << endl;
        return;
    }
    vector<bool> v(10, false);
    int cnt = 0;
    int p = 1;
    while((N % 10) == 0){
        N /= 10;
        v[0] = true;
        cnt = 1;
        p *= 10;
    }

    int n = N;
    int t = n;
    int r;
    while(true){
        while(t){
            r = t % 10;
            if(!v[r])
            {
                v[r] = true;
                ++cnt;
                if(cnt == 10)
                {
                    cout << "Case #" << c <<": " << n*p << endl;
                    return;
                }
            }
            t /= 10;

        }
        n += N;
        t = n;
    }
}

int main()
{
    int cnt;
    cin >> cnt;
    int N;
    for(int i=1; i<=cnt; i++){
        cin >> N;
        getCnt(i, N);
    }
    return 0;
}
