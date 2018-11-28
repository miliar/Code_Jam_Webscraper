#include <iostream>
#include <stack>
using namespace std;

int main() {
	// your code goes here
	int t,i=1;
	int r1,r2;
	int c1[4];
	int c2[4];
	int aux;
	cin >> t;
	while (t--){
		cin >> r1;
		for(int a=0;a<4;a++)
			if (a+1==r1)
			  cin >> c1[0] >> c1[1] >> c1[2]>>c1[3];
			else
			  cin >> aux >> aux >> aux>> aux;
			  
		cin >> r2;
		for(int a=0;a<4;a++)
			if (a+1==r2)
			  cin >> c2[0] >> c2[1] >> c2[2]>>c2[3];
			else
			  cin >> aux >> aux >> aux>> aux;
		
		int p = 0;
		std::stack<int> pilha;
		for(int a=0;a<4;a++) { //cout <<c1[a] << " ";
			for(int b=0; b<4;b++)
			   if (c1[a]==c2[b]){
			   	 pilha.push(c1[a]);
			   	 p++; break;
			   }
		}
		cout << "Case #" << i << ": ";
		if (p == 0) cout << "Volunteer cheated!";
		else if (p == 1) cout << pilha.top();
		else cout << "Bad magician!";
		cout << endl;
		i++;
	}
	return 0;
}