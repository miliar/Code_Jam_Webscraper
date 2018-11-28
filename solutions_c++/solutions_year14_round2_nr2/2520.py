#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;



int main()
{
    int T;
    freopen("fis.in","r",stdin);
    freopen("fis.out","w",stdout);
    cin >> T;

    for(int i = 0; i < T; i++){
        int A,B,K;
        cin >> A >> B >> K;
        int sol = 0;
            for(int q= 0 ; q < A; q++)
            {
                for(int z = 0; z < B; z++){
                    if((q & z) < K)
                        sol++;
                }
            }
    cout << "Case #" << (i+1) <<": " <<sol << endl;
    }

    return 0;
}
