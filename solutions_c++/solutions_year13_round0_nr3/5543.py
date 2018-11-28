#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ifstream fin("C-small-attempt0.in");
    ofstream fout("FAIRWINNER.txt");

int tc, a ,b, t, k, counter;

fin>>tc;

for (t=0;t<tc;t++)
{

fin>>a>>b;
counter=0;
for (k=a;k<b+1;k++)
{bool Fair=false;
if (k == 1){Fair=true;}
if (k == 4){Fair=true;}
if (k == 9){Fair=true;}
if (k == 121){Fair=true;}
if (k == 484){Fair=true;}

if (Fair){counter++;}
}
fout<<"Case #"<<t+1<<": "<<counter<<endl;
}

    return 0;
    }
