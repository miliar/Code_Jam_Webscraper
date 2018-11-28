#include<iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int k = 1; k<=t; k++){
		int first, second, a[4][4], b[4][4];
		cin>>first;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				cin>>a[i][j];
		cin>>second;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				cin>>b[i][j];
		//find any element of a[first] array in b[second] array.
		//if only 1 found, thats the answer
		//if multiple found, "Bad magician!"
		//if none found, "Volunteer cheated!"
		
		first -= 1;
		second -= 1;
		int found = 0, count = 0;
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				if(b[second][j] == a[first][i]){
					found = a[first][i];
					count++;
				}
			}
		}
		if(count == 1)
			cout<<"Case #"<<k<<": "<<found<<endl;
		else if(count>1)
			cout<<"Case #"<<k<<": "<<"Bad magician!"<<endl;
		else if(count == 0)
			cout<<"Case #"<<k<<": "<<"Volunteer cheated!"<<endl;
	}
	return 0;
}