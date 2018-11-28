#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <string.h>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <fstream>

using namespace std;

pair<bool, int> check(string &t){
    char sign = t[0];
    int index = 0;
    while(t[index] == sign && index < t.length()){
        index++;
    }
    if(index == t.length()){
        if(t[t.length() - 1] == '-')
            return make_pair(false, t.length());
        else
            return make_pair(true, -1);
    }
    else
        return make_pair(false, index);
}

void reset(string &t, int index){

    reverse(t.begin(), t.begin() + index);
    for(int i = 0; i < index; i++){
        if(t[i] == '+'){
            t[i] = '-';
        }
        else{
            t[i] = '+';
        }
    }
}

int main(){
    ifstream in("/Users/tech8/Desktop/Ainput.txt");
    ofstream out("/Users/tech8/Desktop/Aoutput.txt");

    long long t;
    in >> t;
    for(int s = 0; s < t; s++)
    {
            string pancake;
            in >> pancake;
            if(pancake.length() == 1){
                if(pancake[0] == '+'){
                    out << "Case #"<< s + 1 << ": " << 0 << endl;
                    continue;
                }else{
                    out << "Case #"<< s + 1 << ": " << 1 << endl;
                    continue;
                }
            }else {
                int cnt = 0;
                while (true) {
                    pair<bool, int> temp = check(pancake);
                    if (temp.first) {
                        out << "Case #" << s + 1 << ": " << cnt << endl;
                        break;
                    } else {
                        reset(pancake, temp.second);
                        cnt++;
                    }
                }
            }
    }
}




