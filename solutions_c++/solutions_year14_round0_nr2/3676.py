#include <iostream>
#include <fstream>
#include <cstdio>
using namespace std;

int n;
double c, f, x;

int main() {
    ifstream fin("B.in");
    FILE *fout = fopen("B.out", "w");
    fin >> n;
    for (int i = 0; i < n; i++) {
        fin >> c >> f >> x;
        double fintime = x / 2.0, time = 0;
        double production = 2;
        double cookies = 0;
        while (true) {
            double addtime = (c - cookies) / production;
            if (time + addtime + (x - cookies) / (production + f) < fintime) {
                fintime = time + addtime + (x - cookies) / (production + f);
                production += f;
                time += addtime;
                cookies = 0;
            }
            else {
                break;
            }
        }
        fprintf(fout, "Case #%d: %1.7f\n", i + 1, fintime);
    }
}
