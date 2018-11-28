#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int t;
	int row1,row2;
	int arr[4][4];
	int i,j,c=1;
	int flag[20];
	cin>>t;
	for(c=1;c<=t;c++){
		memset(flag,0,sizeof(flag));
		printf("Case #%d: ",c);
		cin>>row1;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++){
				cin>>arr[i][j];
				if(i==row1-1)
					flag[arr[i][j]]++;
			}


		cin>>row2;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++){
				cin>>arr[i][j];
				if(i==row2-1)
					flag[arr[i][j]]++;
			}

		vector<int> inter;
		for(i=1;i<=16;i++)
			if(flag[i]==2)
				inter.push_back(i);

		if(inter.size()==1){
			cout<<inter[0]<<endl;
		}
		else if(inter.size()==0){
			cout<<"Volunteer cheated!"<<endl;
		}
		else	cout<<"Bad magician!"<<endl;




	}

	return 0;
}
