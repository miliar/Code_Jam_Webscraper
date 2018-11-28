#include<iostream>
#include<fstream>

using namespace std;

int main(){
	ifstream i("A.txt");
	ofstream o;
	o.open("Aout.txt");
	
	string S;
	unsigned int T, pi, pj;
	
	i>>T;
	for(int cnt=0; cnt<T; cnt++){
		
		i>>S;
		string lastWord;
		int len = S.length();
		pj = 1;
		lastWord.insert(0, 1, S[0]);
		for(pi=1; S[pi]!='\0'; pi++){
			pj = lastWord.length();
			if(S[pi]>=lastWord[0]){
				lastWord.insert(0, 1, S[pi]);
			}else{
				lastWord.insert(pj, 1, S[pi]);
			}
		}
		
		o<<"Case #"<<cnt+1<<": "<<lastWord<<endl;
	}	
	
	i.close();
	o.close();
	return 0;
}
