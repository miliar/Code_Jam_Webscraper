#include <bits/stdc++.h>

using namespace std;

int main(){
    int cases;
    scanf("%d", &cases);

    for(int e = 0; e<cases; e++){
        printf("Case #%d: ", e+1);


        int smax;

        char buff[10000];

        scanf("%d", &smax);
        scanf("%s", buff);

        int numStand = 0;
        int numAdded = 0;

        for(int s = 0; s<=smax; s++){
            int numPeople = buff[s] - '0';
            if(!numPeople) continue;

           // printf("%d people seeing if there are %d standing\n", numPeople, s);

            if(numStand >= s){
             //   printf("Yes. %d standing up.\n", numPeople);
                numStand += numPeople;
            } else {
                int diff = s - numStand;
                numAdded += diff;
                numStand += diff;
                numStand += numPeople;
               // printf("Nope. Need %d\n", diff);
            }
           // printf("There are now %d people standing up\n", numStand);
        }

        printf("%d\n", numAdded);


    }

    return 0;
}
