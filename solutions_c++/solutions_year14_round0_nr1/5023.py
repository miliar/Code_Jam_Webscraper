#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
   int T,r1,r2,a;
   int row1[4],row2[4];
   cin>>T;
   for(int t = 1; t <= T; t++){
	cin>>r1;
	for(int i = 0; i < 4; i++){
	   for(int j = 0; j < 4; j++){
		cin>>a;
		if(i == r1 - 1)
		   row1[j] = a;
	   }
	}
	cin>>r2;
	for(int i = 0; i < 4; i++){
	   for(int j = 0; j < 4; j++){
		cin>>a;
		if(i == r2 - 1)
		   row2[j] = a;
	   }
	}
	int count = 0, num = 0;
	for(int i = 0; i < 4;i++){
	    for(int j = 0; j < 4; j++){
		if(row1[i] == row2[j]){
			count ++;
			num = row1[i];
		}
	    }
	}
	cout<<"Case #"<<t<<": ";
	if(count == 1) cout<<num<<endl;
	else if(!count) cout<<"Volunteer cheated!\n";
	else cout<<"Bad magician!\n";
   }
   return 0;
}
