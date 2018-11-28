#include <stdio.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

class Solution{
public:
    void solute(){
        fstream file("A-large.in");
        ofstream out("out");
        int T, N;
        file>>T;

        for(int i=0;i<T;i++){
            file>>N;
            vector<int> v(10, 0);
            if(N==0) {
                out << "Case #" << i + 1 << ": INSOMNIA" << endl;
                continue;
            }
            int j=0;
            while(find(v.begin(), v.end(), 0)!=v.end()){
                count(v, N*++j);
            }
            out<<"Case #" << i + 1 << ": "<<N*j<<endl;
        }
        out.close();
    }
    void count(vector<int>& v, int num){
        while(num>0){
            v[num%10]=1;
            num/=10;
        }
    }
};

int main() {
    Solution solution;
    solution.solute();
    return 0;
}