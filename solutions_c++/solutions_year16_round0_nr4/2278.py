#include <iostream>
#include <math.h>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string.h>
#include <fstream>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <iomanip>
#define ull unsigned long long
#define ll long long
#define inf 1000000000000
#define bil 1000000000

using namespace std;

ifstream input;
ofstream output;



int main(int argc, char *argv[]) {
cin.sync_with_stdio(false);
cout.sync_with_stdio(false);
input.sync_with_stdio(false);
output.sync_with_stdio(false);
input.open("/users/jihan/Algorithmic Programming/CodeForces/B261/B261/B261.in.txt");
output.open("/users/jihan/Algorithmic Programming/CodeForces/B261/B261/B261.out.txt");
int cases;
input>>cases;
for (int cas=0;cas<cases;cas++){
output<<"Case #"<<cas+1<<": ";
ull k, c, s;
input>>k>>c>>s;
for (int i=0;i<k;i++){
output<<i+1<<" ";
}
output<<"\n";
}

return 0;
}






