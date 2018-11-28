#include <iostream>
#include <vector>
#include <math.h>
#include <string>

using namespace std;

int main(int argc, char** argv){
	int T;
	cin>>T;

	for(int i=0; i<T; i++){
		bool possible=true;
		int N;
		cin>>N;

		vector<char> dictionary;
		vector<int> average;
		vector<int> words[N];
		
		for(int j=0; j<N; j++){
			string word;

			char pc=' ',c=' ';
			int index=0;
			cin>>word;
			for(int k=0;k<word.size();k++){
				c=word[k];
				if(c!=pc && j==0){
					dictionary.insert(dictionary.begin()+dictionary.size(),c);
					average.insert(average.begin()+average.size(),1.0);
				}
				
				if(c!=pc){
					if(dictionary[index]==c){
						words[j].insert(words[j].begin()+words[j].size(),0);
						index++;
					}else{
						possible=false;
					}
				}

				if(possible){
					average[index-1]+=1.0;
					words[j][index-1]++;
				}

				pc=c;
			}
			if(index<dictionary.size())
				possible=false;
		}
		
		cout<<"Case #"<<i+1<<": ";
		int act=0;
		if(possible){
			for(int j=0; j<dictionary.size(); j++){
				for(int k=0; k<N; k++){
					act+=(fabs(rint(average[j]/N)-words[k][j]));
				}				
			}

			cout<<act<<"\n";
		}else{
			cout<<"Fegla Won\n";
		}
	}
}
