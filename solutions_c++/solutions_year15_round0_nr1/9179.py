#include <iostream>
#include<fstream>
using namespace std;

#define cin fin
#define cout fout

int main() {
    ifstream fin("input.in");
    ofstream fout("output.out");

	int t,n,cnt=0,shy,x;
	string s;
	cin>>t;
	for(int p=1;p<=t;p++){
		cin>>n>>s;
		cnt=0;
		shy=0;
		for(int i=0;i<s.length();i++){
			x = s[i]-'0';
			if(x!=0){
				if(shy<i){
					cnt = cnt + (i-shy);
					shy = i+x;
				}
				else{
					shy+=x;
				}
			}
		}
		cout<<"Case #"<<p<<": "<<cnt<<endl;
	}
	return 0;
}
