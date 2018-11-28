/*헤더 선언*/
#include <iostream>
#include <fstream>
#include <string>
#include <assert.h>

using namespace std;

char swipe(char c);

int main()
{ 
	ifstream in; in.open("B-large.in");
	assert(in.is_open());
	ofstream out; out.open("B-large.out");
	int T; //number of test cases
	string S;
	int count=0;
	int flip=0;

	in>>T;
	for(int i=1;i<=T;i++){
		in>>S;
		flip=0;
		for(;;){
			count=0;
			for(int j=0;j<S.length();j++)
				if(S[j]=='+')
					count++;
			if(count==S.length()){
				out<<"Case #"<<i<<": "<<flip<<endl;
				break;
			}
			else if(S[0]=='+'){
				for(int k=0;S[k]=='+';k++)
					S[k]='-';
				flip++;
			}
			
			else{			
				for(int j=S.length()-1;j>=0;j--){
					string P; P=S;
					if(S[j]=='-'){
						for(int k=0;k<=j;k++)
							S[k]=swipe(P[j-k]);
						flip++;
						break;
					}
				}

			}
		}
	}
		in.close(); out.close();
  return 0;
}

char swipe(char c){
	if(c=='+')
		return '-';
	else if(c=='-')
		return '+';
}