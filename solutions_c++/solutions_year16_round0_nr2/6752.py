#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define ANS 1023
int out = 0;
int main() {
	int t;
	int n;
	string str;
	cin >> t;
 	for(int i =0;i <t;i++){
	 	cin >> str;
	 	int count1 =0;
	 	char curr ;
	 	curr = str[0];
	 	for(int j=1; j<str.length();j++)
 		{
 			if(str[j] != curr)
			{
				count1++;
				curr = str[j];
			}	 		
 		}
 		if(curr == '-')
 			count1++;

 		cout << "Case #"<< (i+1)<<": " << count1 << endl;
 	}
	return 0;
}

