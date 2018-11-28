#include <iostream>
#include <string>
#include <cmath>

class cpdstr{
public:
	char word[100];
	int NumOfWord[100];
	int length;
};

using namespace std;

int main(){
	int T;

	cin>>T;

	for(int TCN = 1; TCN <= T; TCN++){
		int N;

		cin>>N;
		char str[100][100];
		cpdstr changedstr[100];
		
		for(int i = 0; i<100; i++){
			for(int j = 0; j<100; j++){
				changedstr[i].NumOfWord[j] = 1;
				changedstr[i].word[j] = NULL;
			}
		}


		for(int i = 0; i<N; i++){
			cin>>str[i];
			int k=0;
			char lastWord = '*';
			for(int j = 0; j<strlen(str[i]); j++){
				if(str[i][j] != lastWord){
					changedstr[i].word[k]=str[i][j];
					k++;
					lastWord = str[i][j];
				}
				else
					changedstr[i].NumOfWord[k-1]++;
			}
			changedstr[i].length = k;
		}

		int check = changedstr[0].length;
		bool ct = 0;
		for(int i = 1; i<N; i++){
			if(strcmp(changedstr[i].word, changedstr[i-1].word)){
				ct = 1;
				break;
			}
		}
			
		int average[100] = {0,};

		int min=0;

		if(ct == 1)
			cout<<"Case #"<<TCN<<": Fegla Won"<<endl;
		else{
			for(int i = 0; i<N; i++){
				for(int j = 0; j<changedstr[0].length; j++){
					average[j] += changedstr[i].NumOfWord[j];
				}
			}

			for(int j = 0; j<changedstr[0].length; j++){
				average[j] /= N;
			}

			for(int i = 0; i<N; i++){
				for(int j = 0; j<changedstr[0].length; j++)
					min += abs(average[j]-changedstr[i].NumOfWord[j]);
			}

			cout<<"Case #"<<TCN<<": "<<min<<endl;
		}

	}

	return 0;
}