#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

int main(){
	int t, test=1, n, min, max, result, average, i, j, k, size, idx_char;
	vector<string> words, diff_chars;
	vector< vector<int> > qnts;
	vector<int>  temp_vector;
	string temp; 
	cin >> t;
	bool impossible;

	while (t--){
		cin >> n;
		words.clear();
		min=-1;
		for(i=0; i<n; i++){
			cin >> temp;
			words.push_back(temp);
		}
/*		for(i=0; i<n; i++){
			cout << words[i] << "\n";
		}
*/		diff_chars.clear();
		temp_vector.clear();
		qnts.clear();
		impossible=false;
		for(i=0; i<n; i++){
			diff_chars.push_back("");
			qnts.push_back(temp_vector);
			for (j=0; j<words[i].size(); j++){
				if(j==0){
					diff_chars[i].append(1, words[i][0]);
					qnts[i].push_back(1);
					idx_char=0;
					continue;
				}
				if(words[i][j-1]==words[i][j]){
					qnts[i][idx_char]++;
				}
				else{
					diff_chars[i].append(1, words[i][j]);//new different char
					qnts[i].push_back(1);
					idx_char++;;
				}
/*				cout << "words[" << i << "] "<< words[i] << "\n";
				cout << "j " << j << "\n";
				cout << "diff_chars[" << i<< "] " << diff_chars[i] << "\n";
				cout << "qnts[" << i<< "].size " << qnts[i].size() << "\n";
				for(k=0; k<qnts[i].size(); k++){
					cout << qnts[i][k];
				}
				cout << "\n";
*/			}
		}
		for(i=0; i<n-1; i++){
			if(diff_chars[i].compare(diff_chars[i+1])==0) continue;
			else {
				impossible = true;
				break;
			}
		}
		result=0;
		if(!impossible){
			for(i=0; i<diff_chars[0].size(); i++){
				min=101;
				max=-1;
//				cout << "qnts posicao i " <<  i << "\n";
				for(j=0; j<qnts.size(); j++){
					if(qnts[j][i]>max) max=qnts[j][i];
					if(qnts[j][i]<min) min=qnts[j][i];
//					cout << qnts[j][i] << " ";
				}
				average = (max+min)/2;
//				cout << "average " << average << " max "<< max << " min " << min << "\n";
				for(j=0; j<qnts.size(); j++){
					result += abs(average-qnts[j][i]);
//					cout << "qnts["<< i << "][" << j << "] "<< qnts[j][i] << " average " << average << " abs "<< abs(average-qnts[j][i]) << " result " << result << "\n";
				}
			}
		}
		if(impossible) cout <<"Case #"<< test++ << ": Fegla Won\n";
		else cout <<"Case #"<< test++ << ": " << result << "\n";
		
	}
	return 1;
}
