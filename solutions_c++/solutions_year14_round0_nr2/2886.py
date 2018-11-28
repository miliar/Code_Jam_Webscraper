#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    int t;
    double c, f, x, totalTime, currentP;
    fstream file, file2;
    file.open("B-large.in");
    file2.open("output.txt", ios::out);
    if(file.is_open()){
        file >> t;
        for(int tt=1 ; tt<=t ; tt++){
            file >> c >> f >> x;
            currentP=2;
            totalTime=0;

            while(true){
                if((c/(currentP))>=((x/currentP)-(x/(currentP+f)))){
                    totalTime+=(x/currentP);
                    break;
                }
                else{
                    totalTime+=(c/currentP);
                    currentP+=f;
                }
            }

            file2 << "Case #" << tt << ": " << fixed << setprecision(7) << totalTime << endl;
        }
        file.close();
    }
    file2.close();

    return 0;
}
