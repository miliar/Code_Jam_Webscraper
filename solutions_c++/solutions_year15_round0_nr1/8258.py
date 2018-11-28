#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <string>
using namespace std;

const int wow = '0';

int main(){
    freopen ("input.txt", "rt", stdin);
    freopen ("output.txt", "wt", stdout);
    int T;
    scanf ("%d", &T);
    for (int t = 1; t <= T; t++){
        string skynes;
        skynes.clear();
        int max, friendz = 0, people = 0 ;
        scanf ("%d", &max);
        scanf ("%s", &skynes[0]);
        for (int i = 0 ; i <= max + 1; i++){
            int n = skynes[i] - wow;
            if (people >= i){
                people += n;
           }
            else{
                friendz+= i - people;
                people +=  i - people + n;
            }
        }
        printf ("Case #%d: %d \n", t, friendz);
    }

    return 0;
}
