#include <iostream>
using namespace std;

int main() {
	int t,count=1;
	cin>>t;
	while(t--){
		int a1,a2,m1[4][4],m2[4][4],n,mat = 0,no;
		bool flag = 0;
		cin>>a1;
		for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++)
		cin>>m1[i][j];
		cin>>a2;
		for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++)
		cin>>m2[i][j];
		for(n = 0; n < 4; n++)
		for(int j = 0; j < 4; j++)
			if(m1[a1-1][n] == m2[a2-1][j]) { 
				mat++;
				no = m1[a1-1][n];
		}
		if(mat == 0)
			cout<<"Case #"<<count<<": Volunteer cheated!"<<endl;
		else if(mat == 1)
			cout<<"case #"<<count<<": "<<no<<endl;
		else
			cout<<"Case #"<<count<<": Bad magician!"<<endl;
	count++;	
	}
	// your code goes here
	return 0;
}