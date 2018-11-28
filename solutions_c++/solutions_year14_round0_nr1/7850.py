#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
using namespace std;



int main() 
{
	int cases;
	cin>>cases;
	string answers[cases];
	vector <int> container;
for (int time=0;time < cases; ++time){	
	int row1;
	cin>>row1;
	int row[4];
	int m1[4][4];
	for (int i=0; i<4; i++){
		for (int j=0; j<4; j++){
			cin>>m1[i][j];		
		}
	}
	for (int count=0; count<4; count++){
		row[count]=m1[row1-1][count];
	}

	sort(row, row+4);

	int row2;
	cin>>row2;
	int rows[4];
	int m2[4][4];
	for (int i=0; i<4; i++){
		for (int j=0; j<4; j++){
			cin>>m2[i][j];		
		}
	}

	for (int count=0; count<4; count++){
		rows[count]=m2[row2-1][count];
	}
	sort(rows, rows+4);
	int counts=0;
	for (int n=0; n<4; ++n){
		int element=row[n];

		for (int m=0; m<4; m++){
			if(element < rows[m])
				break;
			else if (element==rows[m]){
				container.push_back(element);
				counts++;
				break;
			}
		}
	

	}

	if (counts==1){
		stringstream ss;
		ss << container.front();
		answers[time] = ss.str();
	}
	else if (counts > 1)
		answers[time]="Bad magician!";
	else if (counts==0)
		answers[time]="Volunteer cheated!";
	container.clear();
}
	for (int last=0; last < cases; ++last){
		cout<<"Case #"<<last+1<<": "<<answers[last]<<endl;
	}

	return 0;


}