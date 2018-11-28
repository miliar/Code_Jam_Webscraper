#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
using namespace std;


bool doit(vector<vector<int> > lawn) {
     vector<int> xmax(100);
     vector<int> ymax(100);
     
     for (int i = 0; i < lawn.size(); i++) {
         int themax = 0;
         for (int j = 0; j < lawn[0].size(); j++) {
             themax = max(themax, (int)(lawn[i][j]));
         }
         xmax[i] = themax;
         //cout << "XMAX " << i << " " << xmax[i] << endl;
     }
         
     for (int j = 0; j < lawn[0].size(); j++) {
         int themax = 0;
         for (int i = 0; i < lawn.size(); i++) {
             themax = max(themax, (int)(lawn[i][j]));
         }
         ymax[j] = themax;
         //cout << "YMAX " << j << " " << ymax[j] << endl;
     }
     
     for (int i = 0; i < lawn.size(); i++) {
         for (int j = 0; j < lawn[0].size(); j++) {
             int val = (int)(lawn[i][j]);             
             if (val != min(xmax[i], ymax[j])) return false;
         }
     }
     return true;
                    
}
     

int main() {
    ifstream infile("C:/a.in");
    ofstream outfile("C:/a.out");
    int numCases = 0;
    infile >> numCases;
    for (int i = 0; i < numCases; i++) {
        int length = 0, width = 0;
        infile >> length >> width;
        vector<vector<int> > vec;
        for (int j = 0; j < length; j++) {
            vector<int> v;
            for (int k = 0; k < width; k++) {
                int i;
                infile >> i;
                v.push_back(i);
                }
            vec.push_back(v);
        }
        bool ok = doit(vec);
        outfile << "Case #" << (i+1) << ": ";
        if (ok) outfile << "YES" << endl;
        else outfile << "NO" << endl;
    }    
    outfile.close();
    //system("PAUSE");
    return 0;
    
}
