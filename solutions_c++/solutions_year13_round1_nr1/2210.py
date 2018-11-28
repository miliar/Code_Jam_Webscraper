#include <iostream>
#include <fstream>
using namespace std;
int T,Case,r,t,x,sum,i,ans;
int main(){
	ifstream cin  ("A.in");
	ofstream cout ("A.out");
	cin >> T;
	for(Case=1;Case<=T;++Case){
		cin >> r >> t;
		for(sum=i=0;i<23333;++i){
			sum+=2*(r+2*i)+1;
			if(sum>t) break;
		}
		cout << "Case #" << Case << ": " << i << endl;
	}
	return 0;
}
