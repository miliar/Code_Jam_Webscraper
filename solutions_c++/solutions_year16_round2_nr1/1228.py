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
int numchar[26], numdig[10];
string s;
for (int cas=0;cas<cases;cas++){
output<<"Case #"<<cas+1<<": ";
for (int i=0;i<26;i++)numchar[i] = 0;
for (int i=0;i<10;i++)numdig[i] = 0;
input>>s;
for (int i=0;i<s.size();i++){
numchar[s[i]-'A']++;
}
//zero
numdig[0] = numchar[25];
numchar[25] -= numdig[0];
numchar[4] -= numdig[0];
numchar[14] -= numdig[0];
numchar[17] -= numdig[0];

//two
numdig[2] = numchar[22];
numchar[19] -= numdig[2];
numchar[22] -= numdig[2];
numchar[14] -= numdig[2];

//six
numdig[6] = numchar[23];
numchar[18] -= numdig[6];
numchar[8] -= numdig[6];
numchar[23] -= numdig[6];

//seven
numdig[7] = numchar[18];
numchar[18] -= numdig[7];
numchar[4] -= 2 * numdig[7];
numchar[21] -= numdig[7];
numchar[13] -= numdig[7];

//four
numdig[4] = numchar[20];
numchar[5] -= numdig[4];
numchar[14] -= numdig[4];
numchar[20] -= numdig[4];
numchar[17] -= numdig[4];

//eight
numdig[8] = numchar[6];
numchar[4] -= numdig[8];
numchar[8] -= numdig[8];
numchar[6] -= numdig[8];
numchar[7] -= numdig[8];
numchar[19] -= numdig[8];

//five
numdig[5] = numchar[5];
numchar[5] -= numdig[5];
numchar[8] -= numdig[5];
numchar[21] -= numdig[5];
numchar[4] -= numdig[5];

//three
numdig[3] = numchar[17];
numchar[19] -= numdig[3];
numchar[7] -= numdig[3];
numchar[17] -= numdig[3];
numchar[4] -= 2 * numdig[3];

//nine
numdig[9] = numchar[8];
numchar[8] -= numdig[9];
numchar[13] -= 2*numdig[9];


//one
numdig[1] = numchar[13];

for (int i=0;i<10;i++){
for (int j=0;j<numdig[i];j++){
output<<i;
}
}

output<<"\n";
}

return 0;
}






