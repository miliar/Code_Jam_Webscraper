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

bool two(vector<int> a, pair<int, int> &indices){
        int maxx = 0;
        for(int i = 0;  i < a.size(); i++){
            if(a[i] > maxx){
                maxx = a[i];
            }
        }
        int first = 0;
        int second = 0;
        bool flag = false;
        bool checktwo = false;
        for(int i = 0;  i < a.size(); i++){
            if(a[i] == maxx && flag == false && a[i] != 0){
                flag = true;
                first = i;
            } else {
                if(a[i] == maxx && flag == true && a[i] != 0){
                    second = i;
                    checktwo = true;
                    break;
                }
            }
        }
        if(checktwo == true){
            pair<int, int> temp;
            temp.first = first;
            temp.second = second;
            indices = temp;
            return true;
        }else{
            pair<int, int> temp;
            temp.first = first;
            temp.second = second;
            indices = temp;
            return false;
        }
}

bool difference(vector<int> a, pair<int, int> &indices){
    int maxx = 0;
    int maxindex = 0;
    int nextmaxindex = 0;
    for(int i = 0;  i < a.size(); i++){
        if(a[i] > maxx){
            maxx = a[i];
            maxindex = i;
        }
    }
    int nextmax = 0;
    for(int i = 0;  i < a.size(); i++){
        if(a[i] != maxx){
            if(a[i] > nextmax && a[i] != 0){
                nextmax == a[i];
                nextmaxindex = i;
            }
        }
    }
    if(maxx - nextmax >= 2){
        pair<int, int> temp;
        temp.first = maxindex;
        temp.second = nextmaxindex;
        indices = temp;
        return true;
    }else{
        pair<int, int> temp;
        temp.first = maxindex;
        temp.second = nextmaxindex;
        indices = temp;
        return false;
    }
}

bool debuger(vector<int> a, int total){
    for(int i = 0; i < a.size(); i++){
        if(100*a[i] > total*50){ for(int i = 0; i < a.size(); i++)cout << a[i] << " "; cout << endl; cout << a[i] << " failed" << endl; return false; }
    }
    return true;
}

int main(){
    ifstream in("/Users/tech8/Desktop/Ainput.txt");
    ofstream out("/Users/tech8/Desktop/Aoutput.txt");
    long long int test_case;
    in >> test_case;

    for(long long int s = 0; s < test_case; s++) {

        int n;
        in >> n;
        vector<int> a(n, 0);
        int total = 0;
        for(int i = 0; i < n; i++){
            in >> a[i];
            total = total + a[i];
        }
        vector<string> result;
        out << "Case #" << s + 1 << ": ";
        while(total != 0){
            pair<int, int> temp;
            if(two(a,temp)){
                int first = temp.first;
                int second = temp.second;
                total = total - 2;
                char y = first + 'A';
                char z = second + 'A';
                a[first]--;
                a[second]--;
                string res = "";
                res.push_back(y);
                res.push_back(z);
                result.push_back(res);
            }else{ //take only the first component second one is a dummy zero
                if(difference(a, temp)){//diff of two
                    int first = temp.first;
                    total = total - 2;
                    char y = first + 'A';
                    a[first] = a[first] - 2; //remove two from max
                    string res = "";
                    res.push_back(y);
                    res.push_back(y);
                    result.push_back(res);
                }else{ //diff of 1
                    int first = temp.first;
                    total = total - 1;
                    char y = first + 'A';
                    a[first]--; //remove one from max
                    string res = "";
                    res.push_back(y);
                    result.push_back(res);
                }
            }
        }
        if(result[result.size() - 1].length() == 1){
            for(int i = 0; i < result.size() - 2; i++){
                out << result[i] << " ";
            }
            string f = result[result.size() - 2];
            string r = result[result.size() - 1];
            if(f.length() == 2){
                char d = f[0];
                char e = f[1];
                char g = r[0];
                out << d << " " << e << g;
            }else{
                char d = f[0];
                char g = r[0];
                out << d << g; out << " ";
            }
        }else{
            for(int i = 0; i < result.size(); i++){
                out << result[i] << " ";
            }
        }
        out << endl;
    }
}

