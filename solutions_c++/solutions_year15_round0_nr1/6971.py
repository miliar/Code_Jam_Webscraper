// =====================================================================================
//
//       Filename:  probA.cpp
//
//    Description:  c++
//
//        Version:  1.0
//        Created:  04/10/2015 20:08:05
//       Revision:  none
//       Compiler:  g++
//
//         Author:  Sanjay Yepuri (), sanjay.yepuri@gmail.com
//   Organization:  
//
// =====================================================================================
#include <c++/v1/iostream>
#include <c++/v1/fstream>

using namespace std;
fstream in("in.txt");

int main(){
    int testcase = 0;
    in >> testcase;
    for(int test = 0; test < testcase; ++test){
        int total = 0; 
        int max;
        int invite = 0;
        in >> max;
        string line;
        getline(in, line);
        for(int i = 1; i < line.length(); ++i){
            if(total < i-1){
                invite += (i-1-total);
                total += (i-1-total) + (line[i]-'0');
            }
            else{
                total += line[i]-'0';
            }
        }
        printf("Case #%d: %d\n",test+1, invite);
    }
}
