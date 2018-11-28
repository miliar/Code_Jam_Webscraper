#include <iostream>
#include<string.h>
using namespace std;

bool allHappy(char S[], int len){
	for(int i=0;i<len;i++){
		if(S[i]=='-') return false;
	}
	return true;
}

void flipea(char S[], int n){
	char aux[n];
	for(int i=0;i<n;i++){
		if(S[i]=='+') aux[n-1-i]='-';
		else aux[n-1-i]='+';
	}
	for(int i=0;i<n;i++){
		S[i]=aux[i];
	}
}

int main(){
	int T,flips,end,numaflip;
	char S[1000];
	cin>>T;
	cin.ignore();
	
	for(int i=0;i<T;i++){
		cin.getline(S,1000,'\n');
		flips=0;
		end=strlen(S)-1;
		while(!allHappy(S,strlen(S))){
			//recalcular end
			while(S[end]=='+' && end>0){
				end--;
			}
			//mirar inicio, ver cuantas flipeo y flipear
			//para dejar - en el máximo de iniciales como sea posible
			numaflip=0;
			while((S[numaflip]=='+') && (numaflip<end)){
				numaflip++;
			}
			if(numaflip!=0){
				flips++;
				flipea(S,numaflip);
			}
			
			//flipear todo hasta end
			flips++;
			flipea(S,end+1);
		}
		cout<<"Case #"<<(i+1)<<": "<<flips<<endl;
	}
}
