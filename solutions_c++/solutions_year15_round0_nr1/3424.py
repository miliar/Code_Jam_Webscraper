#include <iostream>
#include <fstream>
#define cin in
#define cout out
using namespace std;

ifstream in("primadonna.in");
ofstream out("primadonna.out");

int t;

int main(){

	cin >> t;
	int s;
	string sh;
	for(int k=1;k<=t;k++){
		cin >> s >>sh;
		int tot=0;
		int add=0;
		int tmp;
		for(int i=0;i<sh.size();i++){
			if(i>tot && (sh[i]-'0')>0){
				tmp=i-tot;
				tot+=tmp;
				add+=tmp;
			}
			tot+=(sh[i]-'0');
		}
		cout<<"Case #"<<k<<": "<<add<<"\n";
	}

	return 0;
}
