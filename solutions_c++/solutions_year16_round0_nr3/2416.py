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

int cur=0, lim, maxsize;
unsigned long long tmp2 = 1;
long long convert(unsigned long long base, unsigned long long n){
unsigned long long answer = n%10;
n/=10;
unsigned long long mult = base;
while (n > 0){
answer += (n % 10) * mult;
mult *= base;
n /= 10;
}
return answer;
}

int isprime(unsigned long long n){
for (int i=2;i<=ceil(sqrt(n));i++){
if (n % i == 0){
return i;
}
}
return -1;
}

void generate(int cursize, unsigned long long n){
if (cur >= lim){
return;
}
if (cursize >= maxsize-2){
unsigned long long t = 11110958061612;
unsigned long long answers[9];
for (int i=1;i<10;i++){
answers[i-1] = isprime(convert(i+1,tmp2+(n*10)+1) );
}
for (int i=0;i<9;i++){
if (answers[i] == -1) return;
}
output<<tmp2+(n*10)+1<<" ";
for (int i=0;i<9;i++) output<<answers[i]<<" ";
output<<"\n";
cur++;
return;
}
generate(cursize+1,(n*10)+1);
generate(cursize+1,(n*10));
//cout<<n<<" 69420 "<<cursize<<" ";
return;
}

int main(int argc, char *argv[]) {
cin.sync_with_stdio(false);
cout.sync_with_stdio(false);
input.sync_with_stdio(false);
output.sync_with_stdio(false);
input.open("/users/jihan/Algorithmic Programming/CodeForces/B261/B261/B261.in.txt");
output.open("/users/jihan/Algorithmic Programming/CodeForces/B261/B261/B261.out.txt");
int cases;
input>>cases;
for (int c=0;c<cases;c++){
output<<"Case #"<<c+1<<": ";
input>>maxsize>>lim;
output<<"\n";
for (int i=1;i<maxsize;i++){
tmp2 *= 10;
}
generate(1, 1);
}

return 0;
}






