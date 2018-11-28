#include <fstream>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <algorithm>
using namespace std;

class Solution{
public:
    void solute(){
        ifstream file("B-large.in", ios::in);
        ofstream out("out");
        int T;
        string str;
        getline(file, str);
        stringstream ss;
        ss<<str;
        ss>>T;
        int x=2;
        for(int i=0;i<T;i++){
            int number = 0;
            getline(file, str);
            int v;
            x=2;
            for(int i=0;i<str.length();i++){
                if(str[i]=='-') v=0;
                else v=1;
                if(x!=v){
                    number++;
                    x=v;
                }
            }
            out<<"Case #"<<i+1<<": "<<(x==1?number-1:number)<<endl;
        }
        out.close();
        file.close();
    }


};

int main() {
    Solution solution;
    solution.solute();
    return 0;
}