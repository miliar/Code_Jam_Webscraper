/*
 * b.cpp
 * Copyright (C) 2015 zhao <zhao@kamel-ThinkPad-X201>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

int D,P[1010];

int main() {

    //Create an input file stream
    fstream in("B-large.in",ios::in);
    fstream out("B-large.out", ios::out);
    int T;
    in>>T;
    for(int index = 1; index <= T; ++index){

        in>>D;
        int peek = 0;
        for(int pos = 0; pos < D; ++pos){
            in>>P[pos];
            peek = max(peek, P[pos]);
        }
        cout<<peek<<endl;
        int ans = peek;
        for(int highest = 1; highest <= peek; ++highest){
            int temp = highest;
            for(int pos = 0; pos < D; ++pos){
                temp += (P[pos] + highest - 1) / highest - 1;
            }
            ans = min(ans, temp);
        }

        string temp = "Case #";
        out << temp.c_str()<<index<<": "<<ans<<endl;
    }

	//Close the file stream
	in.close();
        out.close();
	return 0;
}


