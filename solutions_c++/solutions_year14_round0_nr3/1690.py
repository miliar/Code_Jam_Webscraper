#include<iostream>

using namespace std;
const int maxD = 100;
int maze[maxD][maxD];
int d[maxD][maxD];
int t=0;
int T=0;
int R=0,C=0,M=0;
bool possible = false;
// -1 -> c
void printAns(){
	cout << "Case #" << t+1 << ": " << endl;
	for(int i=0;i<R;i++){
		for(int j=0;j<C;j++)
			if(maze[i][j]==-1)
				cout << 'c';
			else if(maze[i][j]==1)
				cout << '*';
			else
				cout << '.';
		cout << endl;
	}
}

// Assuming the (x,y) is NOT a bomb itself
inline int bombs(int x,int y){
	int c=0;
	for(int i=-1;i<2;i++)
		for(int j=-1;j<2;j++)
			if(x+i>=0 && x+i<R && y+j>=0 && y+j<C)
				if(maze[x+i][y+j]==1)
					c++;
	return c;
}


void dfs(int x,int y){
	d[x][y] = 1;
	//cout << "dfs " << x << " " << y << " "<<bombs(x,y)<< endl;
	bool XY = (bombs(x,y)==0);
	if(!XY) return;
	for(int i=-1;i<2;i++)
		for(int j=-1;j<2;j++){
			//cout << "##" << x+i << " " << y+j << endl;
			if(x+i>=0 && x+i<R && y+j>=0 && y+j<C){	
				if(!d[x+i][y+j])
						dfs(x+i,y+j);
			}
		}
}

void clearD(){
	for(int i=0;i<maxD;i++)
		for(int j=0;j<maxD;j++)
			d[i][j] = 0;
}
bool check(){
	int count = 0;
	for(int i=0;i<R;i++)
		for(int j=0;j<C;j++)
			if(maze[i][j] ==1)
				count++;
	if(count != M)
		return false;

	for(int i=0;i<R;i++)
		for(int j=0;j<C;j++)
			if(maze[i][j]==0){
				clearD();
				dfs(i,j);
				
				/* DEBUG *
				
				printAns();
				for(int X=0;X<R;X++){
					for(int Y=0;Y<C;Y++)
						cout << d[X][Y];
					cout << endl;
				}
				cout << "------------------" << endl;
				maze[i][j] = 0;
				/* */

				bool ok = true;
				for(int X=0;X<R;X++)
					for(int Y=0;Y<C;Y++)
						if(maze[X][Y]==0 && !d[X][Y])
							ok = false;
				if(ok){
					maze[i][j]=-1;
					printAns();
					return true;
				}
			}
	return false;

}

void recurs(int i,int j){
	//cout << i << " " << j << endl;
	if(possible)
		return;
	if(i>=R)
		return;
	maze[i][j] = 1;
	if(j+1<C)
		recurs(i,j+1);
	else
		recurs(i+1,0);
	maze[i][j] = 0;
	if(j+1<C && !possible)
		recurs(i,j+1);
	else
		recurs(i+1,0);

	if(possible)
		return;
	if(check()){
		possible = true;
	}
}

int main(){
	cin >> T;
	for(t=0;t<T;t++){
		cin >> R >> C >> M;
		possible = false;		
		recurs(0,0);

		// Printing
		
		if(!possible){
			cout << "Case #" << t+1 << ": " << endl;
			cout << "Impossible" << endl;
		}
		//else
		//	printAns();
	}
	return 0;
}
