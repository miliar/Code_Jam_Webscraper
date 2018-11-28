#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <string>
using namespace std;

const int rew = '0';

int main(){
    freopen ("input.txt", "rt", stdin);
   freopen ("output.txt", "wt", stdout);
    int T;
    scanf ("%d", &T);
    for (int t = 1; t <= T; t++){
        string skyness;
        skyness.clear();
        int Smax, friends = 0, peoples = 0 ;
        scanf ("%d", &Smax);
        scanf ("%s", &skyness[0]);
        for (int i = 0 ; i <= Smax + 1; i++){
            int n = skyness[i] - rew;
            if (peoples >= i){
                peoples += n;
           }
            else{
                friends += i - peoples;
                peoples +=  i - peoples + n;
            }
        }
        printf ("Case #%d: %d \n", t, friends);
    }

    return 0;
}
