#include <stdio.h>
#include <stdlib.h>
using namespace std;

FILE *odp;
long double CookiePerSec, FabricBuildCost, FabricBoost, Destination, Time;

void read(){
    scanf("%Lf %Lf %Lf", &FabricBuildCost, &FabricBoost, &Destination);
}

void program(int TestNumber){
    Time = 0.0;
    CookiePerSec = 2.0;

    read();

    long double TimeToDest, TimeToDestFabric;
    while(true){
        TimeToDest = Destination / CookiePerSec;
        TimeToDestFabric = (FabricBuildCost / CookiePerSec) + (Destination / (CookiePerSec + FabricBoost));
        if (TimeToDest > TimeToDestFabric){
            Time += FabricBuildCost / CookiePerSec;
            CookiePerSec += FabricBoost;
        }
        else{
            Time += Destination / CookiePerSec;
            break;
        }
    }

    fprintf(odp, "Case #%d: %.7Lf\n", TestNumber, Time);
}

int main(){
    int T;
    scanf("%d", &T);

    odp = fopen("/home/staniul/Desktop/Google Code Jam/odp.in", "w");
    for (int i=1; i<=T; i++)
        program (i);

    fclose (odp);
    return 0;
}
