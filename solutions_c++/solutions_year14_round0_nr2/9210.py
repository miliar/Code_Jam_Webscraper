#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

ifstream fin("test.in");

int main() {

int N = 0; 
int n = 0;
int i,j,k;
double C = 0.0, F = 0.0, X =0.0;
double time1 = 0.0, time2 = 0.0;

double cur_s = 2.0, next_s = cur_s;
double construct_time = 0.0;
double res = 0.0;

fin >> N;
for (n = 1; n <= N; n++) {
fin >> C >> F >> X;

cur_s = 2.0;
next_s = cur_s;
construct_time = C/cur_s;
res = 0.0;

while(1) {
next_s = cur_s + F;
time1 = X/cur_s;
time2 = C/cur_s;
if((time1 < (time2 + X/next_s))) { res += time1; break;}
else {res += time2; cur_s = next_s;}
}

cout << "Case #" << n << ": " << fixed << setprecision(7) << res << endl;
}
}
