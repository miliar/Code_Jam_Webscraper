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


string s1, s2;
int dig1[3], dig2[3];
int best1, best2;
int least;
int pow10[4];

void test(int size, int num1, int num2){
if (size == s1.size()){
int diff = num1-num2;
if (diff < 0) diff *= -1;
if (least > diff){
least = diff;
best1 = num1;
best2 = num2;
}
else if (least == diff){
if (best1 > num1 || (best1 == num1 && best2 > num2)){
best1 = num1;
best2 = num2;
}
}
return;
}
if (dig1[size] != -1){
if (dig2[size] != -1){
test(size+1,
num1+(pow10[s1.size()-size-1]*dig1[size]),
num2+(pow10[s1.size()-size-1]*dig2[size]));
}
else{
for (int i=0;i<10;i++)
test(size+1,
num1+(pow10[s1.size()-size-1]*dig1[size]),
num2+(pow10[s1.size()-size-1]*(i)));
}
}
else{
if (dig2[size] != -1){
for (int i=0;i<10;i++)
test(size+1,
num1+(pow10[s1.size()-size-1]*(i)),
num2+(pow10[s1.size()-size-1]*dig2[size]));
}
else{
for (int i=0;i<10;i++){
for (int j=0;j<10;j++){
test(size+1,
num1+(pow10[s1.size()-size-1]*(i)),
num2+(pow10[s1.size()-size-1]*(j)));
}
}
}
}
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


pow10[0] = 1;
pow10[1] = 10;
pow10[2] = 100;
pow10[3] = 10000;
for (int cas=0;cas<cases;cas++){
output<<"Case #"<<cas+1<<": ";
input>>s1>>s2;
for (int i=0;i<s1.size();i++){
if (s1[i] == '?') dig1[i] = -1;
else dig1[i] = s1[i] - '0';
}

for (int i=0;i<s2.size();i++){
if (s2[i] == '?') dig2[i] = -1;
else dig2[i] = s2[i] - '0';
}
least=100000000;
test(0, 0, 0);

int siz;
if (best1 >= 100) siz = 3;
else if (best1 >= 10) siz = 2;
else siz = 1;

for (int i=0;i<s1.size()-siz;i++){
output<<0;
}
output<<best1<<" ";

if (best2 >= 100) siz = 3;
else if (best2 >= 10) siz = 2;
else siz = 1;

for (int i=0;i<s2.size()-siz;i++){
output<<0;
}
output<<best2;


output<<"\n";
}

return 0;
}






