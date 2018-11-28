#include <iostream>
#include <algorithm>
#include <fstream>
#include <set>

using namespace std;

int A[4][4], B[4][4];

int main()
{
    ifstream cin("input.txt");
	//ofstream cout("out.txt");
	int t,n;
	cin>>t;
	for(int i=0; i<t; i++)
	{
		set<int> S;
		int a1, a2, temp;
		cin>>a1;a1--;
		for(int j=0; j<4; j++) for (int k=0; k<4; k++) cin>>A[j][k];
		cin>>a2;a2--;
		pair<set<int>::iterator, bool> myp;
		for(int j=0; j<4; j++) for (int k=0; k<4; k++) cin>>B[j][k];
		for(int j=0; j<4; j++) {
			myp=S.insert(A[a1][j]);
			if(!myp.second) temp = A[a1][j];
		}
		for(int j=0; j<4; j++){
			myp=S.insert(B[a2][j]);
			if(!myp.second) temp = B[a2][j];
		}
		if(S.size()==8) cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		else if(S.size()==7) cout<<"Case #"<<i+1<<": "<<temp<<endl;
		else cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
	}
    return 0;
}