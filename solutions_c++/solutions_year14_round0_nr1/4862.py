// magic.cpp : Defines the entry point for the console application.
//

#include <iostream>
int testcases=0;
int square[4][4];
int s[2][4];
int row[2];

using namespace std;

void readsquare(int a){
	for (int i=0;i<4;i++){
		for (int j=0;j<4;j++)
			cin >> square[i][j];
	}
	for (int i=0;i<4;i++){
		s[a][i]=square[row[a]-1][i];
	}
}
int intersect(int s[2][4]){
	int count=0;
	int found=0;
/*	cout <<"Row" <<row[0]<< endl;
	for(int i=0;i<4;i++){
		cout << s[0][i] << " ";
	}
	cout <<endl;
	cout <<"Row" <<row[1]<< endl;
	for(int i=0;i<4;i++){
		cout << s[1][i] << " ";
	}
	cout <<endl;
*/	
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(s[0][i]==s[1][j]){count++;found=s[1][j];}
		}
	}
		if (count==0) return -1;
		if( count >1) return 100;
		return found;
}
void test(int i){
	cin >> row[0];
	readsquare(0);
	cin >> row[1];
	readsquare(1);
	int x=intersect(s);
	if(x==-1) 
		cout << "Case #"<<i<<": Volunteer cheated!" << endl; 
	else if (x==100)
		cout << "Case #"<<i<<": Bad magician!" << endl;
	else 
		cout << "Case #"<<i<<": "<<x << endl;
}
int main(int argc, char* argv[])
{
	cin >>testcases;

	for(int i=0;i<testcases;i++){
		test(i+1);
	}

	return 0;
}

