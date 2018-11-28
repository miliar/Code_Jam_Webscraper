#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
using namespace std;

int main(){
    ifstream fin("A-largey.in");
    ofstream fout("kaylinwinnerlarge.txt");

int tc, t, g, i, j, seconds, ans1, ans2, rate;
int times[1005];
for (i = 0; i<1005; i++){
    times[i] = -1;
}
fin>>tc;
for (t=0;t<tc;t++){
      fin>>seconds;
      ans1 = 0;
      ans2 = 0;
      rate = 0;
      for (g=1; g<seconds + 1;g++) {
            fin>>times[g];
            if (times[g-1]-times[g] > rate){
                rate = times[g-1]-times[g];
            }
      }
        for (j=1;j<seconds+1;j++){
            if (times[j-1]>times[j]){
                ans1 += times[j-1] - times[j];
            }
        }
        for (j=1;j<seconds;j++){
            if (times[j] < rate){
                ans2 += times[j];
            }
            else{
                ans2 += rate;
            }
        }


      fout<<"Case #"<<t+1<<": "<<ans1<<" "<<ans2<<endl;
}

    return 0;
    }
