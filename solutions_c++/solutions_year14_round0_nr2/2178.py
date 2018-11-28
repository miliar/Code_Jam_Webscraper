#include <vector>
#include <list>
#include <map>
#include <fstream>
#include <iostream>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


using namespace std;


ifstream fin("B-large.in");
ofstream fout("B-out.out");
int main(){
int t;
fin>>t;
for (int tests=0;tests<t;tests++){
long double f0 = 2.0;
long double c,f,x;
fin>>c>>f>>x;
fout.precision(12);
long double upper = x/c;
int up = ceil(upper);
double time[up+1];
time[0]=x/f0;
double factime[up+1];
factime[0] = 0;
for (int i=1;i<=up;i++)time[i]=0;
for (int i=1;i<=up;i++){
    factime[i] = factime[i-1] + c/(f0+(i-1)*f);
    time[i] = factime[i] + x/(f0+i*f);
    if (time[i]>time[i-1]){
        fout<<"Case #"<<tests+1<<": "<<time[i-1]<<endl;      
        break;
    }
    if (i==up){
        fout<<"Case #"<<tests+1<<": "<<time[i]<<endl;
    }
    
}


}

//system("pause");
return 0;
}
