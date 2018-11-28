#include <iostream>
#include <vector>
using namespace std;

int main(){
	int T;
	cin >> T;

	for(int t=1;t<=T;t++){
		int row;
		cin >> row;
		vector < vector <int> > card(4, vector <int> (4,0));
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin >> card[i][j];

		vector <int> first = card[row-1];

		cin >> row;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin >> card[i][j];

		vector <int> second = card[row-1];

		vector <int> ans;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(first[i]==second[j])	ans.push_back(first[i]);

		printf("Case #%d: ", t);
		if(ans.size()==0)	printf("Volunteer cheated!\n");
		else if(ans.size()==1)	printf("%d\n", ans[0]);
		else	printf("Bad magician!\n");

	}

}