#include <sstream>
#include <iostream>
#include <set>
#include <stdio.h>
using namespace std;

int main() {
	freopen("A-small-attempt0 (2).in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	int T,n1,n2;
	int m1[4][4];
	int m2[4][4];
	cin>>T;
	for(int caseNumber=1;caseNumber<=T;caseNumber++) {
		cin>>n1;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>m1[i][j];
			}
		}
		cin>>n2;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>m2[i][j];
			}
		}
		set<int> s;
		s.clear();
		for(int i=0;i<4;i++){
			s.insert(m1[n1-1][i]);
		}
		int count=0;
		int result;
		for(int i=0;i<4;i++){
			if(s.find(m2[n2-1][i])!=s.end()){
				count++;
				result=m2[n2-1][i];
			}
			
		}
		printf("Case #%d: ", caseNumber);
		if(count==0) cout<<"Volunteer cheated!"<<endl;
		if(count==1) cout<<result<<endl;
		if(count>1) cout<<"Bad magician!"<<endl;
	}
	return 0;
}

