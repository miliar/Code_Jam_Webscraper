/*
 * a.cpp
 * Copyright (C) 2015 zhao <zhao@kamel-ThinkPad-X201>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {

	//Create an input file stream
	fstream in("A-large.in",ios::in);
    fstream out("A-large.out", ios::out);
    int T;
    in>>T;
    for(int index = 1; index <= T; ++index){
        int n, ans = 0, sum = 0;
        string str;
        in>>n>>str;
        cout<<n<<str<<endl;
        for(int pos = 0; pos <= n; ++pos){
            if(pos > sum){
                int delta = pos - sum;
                sum += delta;
                ans += delta;
            }
            sum += str[pos] - '0';
        }
        string temp = "Case #";
        out << temp.c_str()<<index<<": "<<ans<<endl;
    }

	//Close the file stream
	in.close();
    out.close();
	return 0;
}


