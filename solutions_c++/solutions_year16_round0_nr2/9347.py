#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

vector<bool> gen(string &str) {
    vector<bool> vec(0);
    for (int  i = 0; i < str.size(); i++) {
        if (str[i] == '+') vec.push_back(true);
        else vec.push_back(false);
    }
    return vec;
}

void revenge(vector<bool>& vec, int n) {
    for (int i = 0; i <= n; i++) {
        vec[i] = !vec[i];
    }
    reverse(vec.begin(), vec.begin()+n+1);
}

// void pt(vector<bool>& vec) {
//     for (int i = 0; i <vec.size(); i++) {
//         cout<<vec[i];
//     }
//     cout<<endl;
// }

int flip(string str) {
    vector<bool> vec = gen(str);
    int res = 0;
    for (int i = vec.size()-1; i > 0; i--) {
        if (vec[i]) continue;
        
        if (vec[0]) {
            int j = 0;
            while (j < i && vec[j+1]) j++;
            revenge(vec, j);
            res++;
        } 
        
        revenge(vec, i);
        res++;
    }
    
    if (!vec[0]) res++;
    
    return res;
}

int main() {
    ifstream infile("B-large.in.txt");
    ofstream outfile("outputLarge.out");
    string a;
    int i = 0;
    infile >> a;
    while (infile >> a)
    {
        i++;
        outfile << "Case #" << i << ": " << flip(a)<< endl;
    }
    return 0;

}