#include <iostream>
#include <fstream>
#include <cassert>
#include <algorithm>
#include <vector>
using namespace std;

const char * infile="A-large.in";
const char * outfile="pa-large.out";

int getans(vector<int> &s, int X) {
    int n = s.size();
    
    int ans=0;
    int i=0, j=n-1;
    while (i<=j) {
        if (i==j) {
            ans++; break;
        }
        
        if (s[i]+s[j] > X) {
            j--;
            ans++;
        }
        else {
            i++; j--;
            ans++;
        }
    }
    
    return ans;    
}

int main() {
    ifstream fin(infile);
    ofstream fout(outfile);
    
    int test;
    fin >> test;
    for (int count=1; count<=test; count++) {
        int n, X;
        fin >> n >> X;
        vector<int> s;
        for (int i=0; i<n; i++) {
            int a;
            fin >> a;
            s.push_back(a);
        }
        
        sort(s.begin(), s.end());
        
        fout << "Case #" << count << ": " << getans(s, X) << endl;
    }
    
    return 0;
}
