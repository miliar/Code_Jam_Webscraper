#include <iostream>
#include <iomanip> 

using namespace std;

int T;
int tc;

int A[4][4];
int B[4][4];
int ar;
int br;

int solve(){
	tc++;
	cin >> ar;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			cin >> A[i][j];
	cin >> br;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			cin >> B[i][j];
	
	ar--;
	br--;
	
	int loc = 0;
	int nf = 0;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if( A[ar][i] == B[br][j] ){
				loc = A[ar][i];
				nf++;
			}

	cout << "Case #"<<tc<<": ";
	if( nf == 1)
		cout << loc;
	else if(nf > 1)
		cout << "Bad magician!";
	else
		cout <<  "Volunteer cheated!";
	cout << endl;	
	return 0; 
}

int main(){
	cin >> T;
	while(T--) solve();
}
