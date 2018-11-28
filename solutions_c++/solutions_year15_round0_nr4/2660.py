#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ifstream fin("D-small-attempt22.in");
    ofstream fout("ok3.txt");

int tc, x, r, c, area, t;

fin>>tc;
for (t=0;t<tc;t++)
{
fin>>x>>r>>c;
area = r * c;
if (x == 1){
    fout<<"Case #"<<t+1<<": GABRIEL"<<endl;
}
else if (area < x){
    fout<<"Case #"<<t+1<<": RICHARD"<<endl;
}
else if (area % x != 0){
    fout<<"Case #"<<t+1<<": RICHARD"<<endl;
}
else if (x == 3 && area < 5){
            fout<<"Case #"<<t+1<<": RICHARD"<<endl;
        }
else if (x == 4 && area < 11){
            fout<<"Case #"<<t+1<<": RICHARD"<<endl;
        }
else{
        fout<<"Case #"<<t+1<<": GABRIEL"<<endl;
}
}

    return 0;
    }
