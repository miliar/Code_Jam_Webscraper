//
// Created by Yuxiang LI on 09/04/16.
//
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int T;
vector<bool> s(101),temp(101);

int lastMinus(int l){
    while(l >= 0 && s[l])
        l--;
    return l;
}

int firstMinus(int l){
    int i = 0;
    while(i < l && s[i])
        i++;
    return i;
}

int main(){
    ifstream in("B-large.in");
    ofstream out("output.out");
    in >> T;
    string ss;
    getline(in,ss);
    for(int cases = 1; cases <= T; cases++){
        getline(in,ss);
        //cout << ss << endl;
        int l = ss.length();
        for (int i = 0; i < l; i++)
            s[i] = ss[i] == '+' ? true:false;
        int flip = 0;
        int last = lastMinus(l-1);
        while(last != -1) {
            if (last == 0) {
                s[0] = true;
                flip++;
                last = -1;
            } else {
                int first = firstMinus(l);
                //cout << first <<' ' << last << endl;
                for (int i = 0; i <= last - first; i++)
                    temp[i] = (!s[last - i]);
                for (int i = 0; i <= last - first; i++) {
                    s[i] = temp[i];
                    //cout << s[i];
                }
                if (first != 0)
                    flip++;
                for (int i = last - first+1; i < l; i++) {
                    s[i] = true;
                    //cout << s[i];
                }
                flip++;
                //cout << endl;
                last = lastMinus(l - 1);
            }
        }

        out << "Case #" << cases << ": " << flip << endl;
    }
    in.close();
    out.close();
    return 0;
}
