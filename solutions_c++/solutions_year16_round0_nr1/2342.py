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
    ifstream infile ("A-large.in");
    ofstream outfile("output.out");
    if (!infile || !outfile){
        return 0;
    }
    int T;
    infile >> T;
    int num = 0, first = 0, addNum = 0;
    for(int i = 0; i < T; i++) {
        infile >> first;
        addNum = first;
        vector<int> mark(10, 0);
        int count = 0;
        if(first == 0){
            outfile << "Case #" << (i + 1) << ": INSOMNIA" << endl;
        }else{
            while(true){
                int temp = first, cur = 0;
                bool flag = false;
                while(temp > 0){
                    cur = temp % 10;
                    temp = temp / 10;
                    if(mark[cur] == 0){
                        mark[cur] = 1;
                        count ++;
                        if(count == 10){
                            outfile << "Case #" << (i + 1) << ": " << first << endl;
                            flag = true;
                            break;
                        }
                    }
                }
                if(flag){
                    break;
                }
                first += addNum;
            }
        }
    }
    infile.close();
    outfile.close();
    return 0;
}
