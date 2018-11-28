/*
 * A.CPP
 *
 *  Created on: 13-Apr-2013
 *      Author: sandip
 */

#include <iostream>
#include <vector>
#include <unistd.h>
#include <algorithm>
#include <map>
#include <string>
#include <cstdio>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <iomanip>


using namespace std;
void solution(ifstream &in ,ofstream &out);

int main()
{
	long long nTestCase = 0;

	ifstream in("/home/sandip/Downloads/A-large.in",ifstream::in);
	ofstream out("/home/sandip/Downloads/A-large.out",ofstream::out);

	string strTestCase;
	getline(in,strTestCase);
	nTestCase = atoll(strTestCase.c_str());

	for(int i=0; i< nTestCase; i++)
	{
		out<<"Case #"<<i+1<<": ";
		solution(in, out);
		out<<endl;
	}

	in.close();
	out.close();
	return 0;
}

void solution(ifstream &in, ofstream &out)
{
    vector<int> s;
    int S;
    in >> S;
    for(int i=0;i<S+1;i++) {
        char tmp;
        in >> tmp;
        s.push_back(tmp-48);
        //std::cout<< tmp;
    }
    //std::cout << "\n";

    int currentS = 0;
    int friends = 0;

    for(int i=0;i<s.size();i++)
    {
        std::cout << currentS << " " << i << " " << friends << " " << s[i] << std::endl;
        if(s[i] > 0) {
            if(currentS>=i) {
                currentS +=s[i];
            }
            else {
                friends += i-currentS;
                currentS += i-currentS + s[i];
            }
        }
    }
    std::cout << currentS << " " << friends << std::endl;
    out << friends;
}





