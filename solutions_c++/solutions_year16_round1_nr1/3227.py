/*
 * a.cpp
 *
 *  Created on: Mar 23, 2016
 *      Author: kathrine
 */
#include <iostream>
#include<set>
#include<string>
#include<cmath>
#include<iterator>
#include <fstream>

using namespace std;

int main()
{
	ifstream in;
	in.open("A-large.in");
	ofstream out;
	out.open("A-large.out");
	int t;
	string s,tmp;
	in>>t;
	for(int k=0;k<t;k++){
		in>>s;
		tmp = "";
		tmp+=s[0];
		for(int i=1;i<s.length();i++){
			if(s[i]>=tmp[0])
				tmp = s[i]+tmp;
			else
				tmp+=s[i];
		}
		out<<"Case #"<<k+1<<": "<<tmp<<endl;

	}
in.close();
out.close();
  return 0;
}

