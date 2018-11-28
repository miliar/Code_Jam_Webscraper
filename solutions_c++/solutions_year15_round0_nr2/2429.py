#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int getTime(vector<int> v, int x) {
    int splits = 0;
    for (int i = 0; i < v.size(); i++) {
        splits += (v[i] - 1) / x;
    }
    return splits + x;
}

int main()
{
    ifstream f("C:/Users/Rebecca/Downloads/B-large.in");
    ofstream out;
    out.open("C:/Users/Rebecca/Downloads/result4.txt");

    int numtests;
    f >> numtests;
    for (int i = 0; i < numtests; i++) {
        int diners;
        f >> diners;
        vector<int> v;
        for (int j = 0; j < diners; j++) {
            int x;
            f >> x;
            v.push_back(x);
        }
        int max = v[0];
        for (int j = 1; j < v.size(); j++) {
            if (v[j] > max) max = v[j];
        }
        int best = getTime(v, 1);
        for (int j = 2; j <= max; j++) {
            int time = getTime(v, j);
            if (time < best) best = time;
        }
        out << "Case #" << i+1 << ": " << best << endl;
    }
    out.close();
    return 0;
}

