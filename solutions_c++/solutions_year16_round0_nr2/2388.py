#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <cstring>
using namespace std;

int main()
{
    ifstream infile ("B-large.in");
    ofstream outfile("output.out");
    if (!infile || !outfile){
        return 0;
    }
    int T;
    infile >> T;
    for(int i = 0; i < T; i++) {
        string str;
        infile >> str;
        int len = str.length();
        int ans = 0;
        bool opera = false;//false表示需要找第一个-
        for(int j = len - 1; j >= 0; j--){
            if(!opera){
                if(str[j] == '+')
                    continue;
                else{
                    ans ++;
                    opera = !opera;
                }
            }else{
                if(str[j] == '-')
                    continue;
                else{
                    ans ++;
                    opera = !opera;
                }
            }
        }
        outfile << "Case #" << (i + 1) << ": " << ans << endl;
    }
    infile.close();
    outfile.close();
    return 0;
}
