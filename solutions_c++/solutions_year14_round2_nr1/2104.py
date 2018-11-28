//============================================================================
// Name        : q1.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <stack>
#include <map>

using namespace std;

int main() {

	ifstream input("/home/user/workspace_cpp/q1/src/A-small-attempt2.in");
	ofstream output("/home/user/workspace_cpp/q1/src/outputSSS");

	string line;
	int casenum;
	input >> casenum;

	for (int i=0;i<casenum;i++){
		int n=0;
		bool won=false;
		int count = 0;
		input >> n;
		if (n==2){
			string str1="";
			string str2="";
			input >> str1;
			input >> str2;

			if (str1==str2){
				count = 0;
			}else{
				int ii=0;
				int jj=0;
				while(ii<str1.length() && jj<str2.length()){
					if (str1[ii]!=str2[jj] && ii==0 && jj==0){
						won =true;
						break;
					}

					if (str1[ii]==str2[jj]){
						ii++;
						jj++;
						continue;
					}

					if (str1[ii]!=str2[jj]){
						if (str1[ii]==str1[ii-1]){
							count++;
							ii++;
						}else{
							if (str2[jj]==str2[jj-1]){
								count++;
								jj++;
							}else{
								won=true;
								break;
							}
						}
					}
				}

				if (ii==str1.length()&& jj!=str2.length()){
					while (jj<str2.length()){
						if (str2[jj]!=str2[jj-1]){
							won=true;
							break;
						}else{
							jj++;
							count++;
						}
					}
				}

				if (ii!=str1.length()&& jj==str2.length()){
					while (ii<str1.length()){
						if (str1[ii]!=str1[ii-1]){
							won=true;
							break;
						}else{
							ii++;
							count++;
						}
					}
				}


			}
		}


		if (won==true){
			output << "Case #" << i+1 << ": " << "Fegla Won" << endl;
		}else{
			output << "Case #" << i+1 << ": " << count << endl;
		}
	}

	input.close();
	output.close();

	return 0;
}

