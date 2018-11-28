#include <iostream>
#define ROWS 4
#define COLUMNS 4
using namespace std;

int main() {
	int T, cards[4][4], ans, soln, count, possibleAns;
	cin>>T;
	for(int testCase=1;testCase<=T;++testCase){
		cin>>ans;
		for(int i=0;i<ROWS;++i)
			for(int j=0;j<COLUMNS;++j) 
				cin>>cards[i][j];
		soln=0;
		for(int j=0;j<COLUMNS;++j) soln|=(1<<(cards[ans-1][j]-1));
		cin>>ans;
		for(int i=0;i<ROWS;++i)
			for(int j=0;j<COLUMNS;++j) 
				cin>>cards[i][j];
		count=0;
		for(int j=0;j<COLUMNS;++j) 
			if(soln & (1<<(cards[ans-1][j]-1))){
				count++;
				possibleAns=cards[ans-1][j];
			}
		if(count==0) cout<<"Case #"<<testCase<<": Volunteer cheated!"<<endl;
		else if(count==1) cout<<"Case #"<<testCase<<": "<<possibleAns<<endl;
		else cout<<"Case #"<<testCase<<": Bad magician!"<<endl;
	}
	return 0;
}