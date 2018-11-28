

#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char** argv) 
{
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        
        int N;
        cin >> N;
        int maxDif = 0;
        int acum = 0;
        int acum2 = 0;

        int last = 0;
        int current = 0;
        cin >> last;

        vector<int> vec;
        vec.push_back(last);
        
        for (int j = 1; j < N; j++) {
            cin >> current;
            vec.push_back(current);
            int dif = current - last;
            
            if (dif < 0) {
                acum += (-dif);
            }
            if (-dif > maxDif) {
                maxDif = -dif;
            }
            last = current;
        }

        for (int j = 0; j < N-1; j++) {
            acum2 += min(vec[j], maxDif);
        }


        printf("Case #%d: %d %d\n", i+1, acum, acum2);
    }


}
