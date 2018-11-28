#include <iostream>
#include <queue>
#include <cstdio>
using namespace std;



int main(){
	int T;
	scanf("%d ", &T);
	for(int x = 0; x < T; x++){
		int a;
		int b;
		int cartas1[5][5];
		int cartas2[5][5];
		scanf("%d ", &a);
		for(int i=1; i<5; i++)
			for(int j=1;j<5;j++)
				scanf("%d ", &cartas1[i][j]);
		scanf("%d ", &b);
		for(int i=1; i<5; i++)
			for(int j=1;j<5;j++)
				scanf("%d ", &cartas2[i][j]);
		queue<int> q;
		for(int j=1; j<5; j++)
			for(int k=1; k<5; k++)
				if(cartas1[a][j]==cartas2[b][k])
					q.push(cartas1[a][j]);
		cout << "Case #" << x+1 << ": ";
		if(q.size() == 0)
			cout << "Volunteer cheated!" << endl;
		else if(q.size() > 1)
			cout << "Bad magician!" << endl;
		else{
			int elem = q.back();
			cout << elem << endl;
		}





	}
}
