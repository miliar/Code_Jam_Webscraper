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


void replaceString(std::vector<char> *wholeString, std::vector<char> subString){
	std::vector<char> temp;
	temp.clear();
	char toPut;
	if(subString.at(0)=='-')
		toPut='+';
	else
		toPut='-';

	for(int i=0;i<subString.size();i++){

		temp.push_back(toPut);
	}

	wholeString->erase(wholeString->begin(),wholeString->begin()+subString.size());
	for(int i=0;i<subString.size();i++){
		wholeString->insert(wholeString->begin(),temp.at(i));
	}
}


int main() {

	FILE *fileInput = freopen("B-large.in","r",stdin);
	FILE *fileOutput = freopen("B-large.out","w",stdout);

		int numberOfEntries;
		cin >> numberOfEntries; // there are numberOfEntries +1 ligne inside the text
		std::vector<char> subString;
		std::vector<char> Sbis;
		for(int i=1;i<=numberOfEntries;i++ ){
			cout << "Case #" << i << ": ";
			string S;
			cin >> S;
			Sbis.clear();
			subString.clear();
			for(int i=0;i<S.size();i++){
				Sbis.push_back(S[i]);
			}
			int counter =0;
			bool finish =false;
			int k=1;
			subString.push_back(Sbis.at(0));

			while(!finish){
				if(k==0){
					subString.clear();
					subString.push_back(Sbis.at(0));
					k++;


				}
				if(k<Sbis.size()){
					if(Sbis.at(k)==subString.at(k-1)){
						subString.push_back(Sbis.at(k));
						k++;

					}else{
						replaceString(&Sbis,subString);
						//replace(Sbis.begin(),Sbis.begin()+k-1,subString.at(k-1),Sbis.at(k));
						counter++;
						k=0;
						if(k == Sbis.size()-1){
							if(Sbis.at(k)=='+')
								finish =true;
						}
					}
				}else{//if end of Sbis
					if(Sbis.at(k-1)=='+')
						finish =true;
					else{//Sbis has only '-'
						finish=true;
						counter++;
					}
				}
			}
			cout << counter <<endl;
		}
	std::fclose(stdout);
	return 0;
}
