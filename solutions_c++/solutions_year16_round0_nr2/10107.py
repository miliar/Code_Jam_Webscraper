#include <stdio.h>
#include <stdlib.h>
#include <queue>
#include <string>
#include <unordered_set>

using namespace std;

bool isHappy(string s){
	for(int i=0; i<s.length(); i++){
		if(s[i] == '-')
			return false;
	}
	return true;
}

string flip(string str, int n){
	int i=0, j=n-1;	
	char aux;
	
	while(j>=i){
	
		aux = str.at(i);
		str[i] = str[j] == '-' ? '+' : '-';
		str[j] = aux == '-' ? '+' : '-';
	
		i++; j--;
	}
	
	return str;
}

int flipper(string str){

	queue< pair<string, int> > myq;
	unordered_set<string> mset;
	
	myq.push( make_pair(str, 0) );
	mset.insert(str);

	while(!myq.empty()){
	
		string s = myq.front().first;
		int count = myq.front().second;
		
		if( isHappy(s) ) {
			return count;
		}
		
		myq.pop();		
		mset.insert(s);	
		
		for(int i=1; i<=s.length(); i++){		
			string flipped = flip(s, i);
			
			if( mset.find(flipped) == mset.end())		
				myq.push( make_pair(flipped, count+1) );		
		}
	}
}

int main(int argc, char **argv){

	int T;
	scanf("%d", &T);
	
	for(int t=1; t<=T; t++){

		char str[101];
		scanf("%s", str);
		
		printf("Case #%d: %d\n", t, flipper(string(str)) );
	}

	return 0;
}
