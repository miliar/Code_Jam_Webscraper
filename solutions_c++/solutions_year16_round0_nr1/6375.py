#include <iostream>
#include <cstdio>
#include <math.h>
#include <vector>
#include <stdlib.h>     /* abs */
#include <string.h>
#include <unordered_map>
#include <list>
#include <algorithm>
using namespace std;

int main() {

	FILE *fileInput = freopen("A-large.in","r",stdin);
	FILE *fileOutput = freopen("A-large.out","w",stdout);

	std::vector<char> listDigits;
	std::vector<char>::iterator it;

		string N;
		int k=2;
		int numberOfEntries;
		cin >> numberOfEntries; // there are numberOfEntries +1 ligne inside the text

		for(int i=1;i<=numberOfEntries;i++ ){
			cin >> N;
			int Number = std::stoi(N);

			listDigits.push_back(N[0]);

			for(int i=1;i<N.size();i++){

				it = find (listDigits.begin(), listDigits.end(), N[i]);
				if(it == listDigits.end()){//not found
					listDigits.push_back(N[i]);
				}
			}
			string NumberToString="";
			int NumberNew;
			while(listDigits.size() != 10 && k<=100){
				NumberNew = k*Number;
				NumberToString = to_string(NumberNew);

				for(int j=0;j<NumberToString.size();j++){
					it = find (listDigits.begin(), listDigits.end(), NumberToString[j]);
					if(it == listDigits.end()){//not found
						listDigits.push_back(NumberToString[j]);
					}
				}

				k++;
			}

			cout << "Case #" << i << ": ";
			if(listDigits.size() == 10)
				cout << NumberToString << endl;
			else
				cout << "INSOMNIA" << endl;

			listDigits.clear();
			k=2;
		}
	std::fclose(stdout);
	return 0;
}
