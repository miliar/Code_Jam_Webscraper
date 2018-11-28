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


ifstream fin("B-small-attempt0.in");
ofstream fout("B.out");
int main(){
int t;
fin>>t;
for (int tests=0;tests<t;tests++){

long long a,b,k;
fin>>a>>b>>k;

long long ans = 0;
for (long long i=0;i<a;i++)
    for (long long j=0;j<b;j++)
        if ((i&j)<k)ans++;







fout<<"Case #"<<tests+1<<": ";
fout<<ans<<endl;
}

//system("pause");
return 0;
}
