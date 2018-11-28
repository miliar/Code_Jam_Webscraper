#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

bool finish(vector<bool>& named) {
    for (int i = 0; i < named.size(); i++) {
        if (named[i] == false) return false;
    }
    return true;
}

int count(int N) {
    vector<bool> named(10, false);
    
    int i = 0;
    while (!finish(named)) {
        i++;
        int cur = N * i;
        
        vector<int> vec(0);
        while (cur) {
            vec.push_back(cur % 10);
            cur /= 10;
        }
        
        for (int j = 0; j < vec.size(); j++) {
            named[vec[j]] = true;
        }
    }
    
    return N * i;
}






int main() {
    
    ifstream infile("A-large.in");
    ofstream outfile("outputLarge.out");
    int a;
    int i = 0;
    infile >> a;
    while (infile >> a)
    {
        i++;
        if (a == 0) outfile << "Case #" << i << ": " << "INSOMNIA"<< endl;
        else  outfile << "Case #" << i << ": " << count(a)<< endl;
    }
    return 0;
}