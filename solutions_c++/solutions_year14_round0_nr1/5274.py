// Pasha Khosravi
#include<iostream>
using namespace std;
const int N = 20;
int d[N];

int grids[2][4][4];
int r1,r2;

void clear(){
	for(int i=0;i<N;i++)
		d[i] = 0;
	r1=r2=0;
}
void read(){
		cin >> r1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin >> grids[0][i][j];		
		cin >> r2;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin >> grids[1][i][j];
}



int main(){
	int test=0;
	cin >> test;
	for(int t=0;t<test;t++){
		clear();
		read();
		r1--; r2--;
		for(int i=0;i<4;i++){
			d[grids[0][r1][i]]++;
			d[grids[1][r2][i]]++;
		}
		bool cheat = true; // do we have possible answer yet or not
		bool badmagican = false;
		int ans = 0;
		for(int i=1;i<17;i++){
			if(d[i]==2){
				if(cheat){
					cheat = false;
					ans = i;
				}
				else
					badmagican = true;
			}	
		}
	//	for(int i=1;i<17;i++) 
	//		cout << d[i];
	//	cout << endl;
		cout << "Case #" << t+1 << ": ";
		if(badmagican)
			cout << "Bad magician!" << endl;
		else if(cheat)
			cout << "Volunteer cheated!" << endl;
		else 
			cout << ans << endl;
	}		
	return 0;	
}



