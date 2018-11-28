//  g++ b.cpp - b -std=c++11 && ./b < b.in > b.out
#include <iostream>
#include <set>
using namespace std;

int main(){
	int t,n,lines, num, s[2501];
	set<int> resp;
	cin >> t;
	for(int i=1; i<=t;i++){
		cin >> n;
		lines = (2*n-1)*n;
		for(int j=0;j<2501;j++){
			s[j]=0;
		}

		for(int j=0;j<lines;j++){
			cin >> num;
			s[num]++;
		}

		for(int j=1;j<2501;j++){
			if(s[j]%2!=0) resp.insert(j);
		}

		cout << "Case #"<< i << ":";
		for (set<int>::iterator it=resp.begin(); it!=resp.end(); ++it)
    			cout << ' ' << *it;
		cout << endl;
		resp.clear();
	}

}