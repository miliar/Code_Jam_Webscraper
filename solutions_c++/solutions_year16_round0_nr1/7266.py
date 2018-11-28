#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <set>
#include <cstring>
#include <memory>
#include <vector>
#include <cassert>

using namespace std;

int used[10];
int currently;

void update(int x, int mark)
{
    while (x > 0) {
        int c = x % 10;
        if (used[c] != mark) {
            currently++;
        }
        used[c] = mark;
        x /= 10;
    }
}

int main(int argc, char* argv[])
{
    ifstream in;
    in.open("input.txt");
    ofstream out;
    out.open("output.txt");
    
    ios_base::sync_with_stdio(false);
    
    int tests;
    in >> tests;
    for (int t = 1; t <= tests; t++) {
        int num;
        in >> num;
        if (num == 0) {
            out << "Case #" << t << ": INSOMNIA\n";
            continue;
        }
        
        currently = 0;
        int times = 1;
        update(num, t);
        while (currently != 10) {
            times++;
            update(num * times, t);
        }
        out << "Case #" << t << ": " << num * times << "\n";
    }
    
    in.close();
    out.close();
}

