#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
using namespace std;

int main(){
    ifstream fin("A-large.in");
    ofstream fout("ovationwinner.txt");

int tc, smax, counter, t, point, diff;
bool noshy;
string shy;
fin>>tc;
for (t=0;t<tc;t++){
        counter = 0;
        diff = 0;
        fin>>smax>>shy;
        for (point = 0; point < smax+1; point++){
            if (counter < point){
                diff += point - counter;
                counter += point - counter;
            }
            counter += shy[point] - 48;
            //fout<<"counter is"<<counter<<"diff is"<<diff<<endl;
        }
        fout<<"Case #"<<t+1<<": "<<diff<<endl;
}

    return 0;
    }
