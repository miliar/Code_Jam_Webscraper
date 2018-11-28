#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

ifstream fin("test.in");

int main() {
int N = 0; 
int tc = 0;
int i,j,k;
double Atime = 0.0, Ttime = 0.0;
double C = 0.0, F = 0.0, X =0.0;
fin >> N;
for (tc = 1; tc <= N; tc++) {
fin >> C >> F >> X;
double x_left = X;
double prev_speed = 2.0;
double next_speed = prev_speed;
double build_next_time = C/prev_speed;
double total_time = 0.0;
while(1) {
next_speed = prev_speed + F;

Atime = x_left/prev_speed;
Ttime = C/prev_speed;
if((Atime < (Ttime + x_left/next_speed))) { 
total_time += Atime; break;
}
else { //build next
total_time += Ttime;
prev_speed = next_speed;
}
}

cout << "Case #" << tc << ": " << fixed << setprecision(7) << total_time << endl;
}
}
