#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <bits/stdc++.h>
using namespace std;


//int pp[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313};
//vector<int> primes (pp, pp + sizeof(pp));

#define cout fout
#define cin fin


int main() {
    //Enter your code here. Read input from STDIN. Print output to STDOUT
	ofstream fout("C:\\Users\\Harry\\Desktop\\temp");
	ifstream fin("C:\\Users\\Harry\\Desktop\\A-large.in");
	int t;
	cin>>t;
	string buff;
	getline(cin, buff);



	for(int tc = 1; tc <=t; tc++){
		string str;
		vector<char>vec;
		cin>>str;
		vec.push_back(str[0]);
		for(int i=1; i<str.size(); i++){
			if(str[i] >= vec[0]){
				vec.insert(vec.begin(), str[i]);
			}
			else{
				vec.push_back(str[i]);
			}
		}
		cout<<"Case #"<<tc<<": ";
		for(int i=0; i<vec.size(); i++)
			cout<<vec[i];
		cout<<endl;
	}


	fout.close();
	return 0;
}
