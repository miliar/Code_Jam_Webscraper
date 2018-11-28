#include<iostream>
#include<cstdio>
using namespace std;

int main(){
	int T,t;

	freopen("A-small-attempt2.in","r",stdin);

	freopen("A.out","w",stdout);//cout<<"888";
	cin>>T;
	t = T;
	int maxn[5][5];
	int arr[2][5];
	while(T--){
        int a;
        cin>>a;
        for(int i = 0; i < 4; i++)
        	for(int j = 0; j < 4; j++)
        		cin>>maxn[i][j];
        for(int i = 0; i < 4; i++)
        	arr[0][i] = maxn[a-1][i];

        cin>>a;
        for(int i = 0; i < 4; i++)
        	for(int j = 0; j < 4; j++)
        		cin>>maxn[i][j];
        for(int i = 0; i < 4; i++)
        	arr[1][i] = maxn[a-1][i];

		cout<<"Case #"<<t - T<<": ";
		int flag = 0,haha;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++){
				if(arr[0][i] == arr[1][j]){
					haha = arr[1][j];
					flag++;
				}
			}
		if(flag == 0) cout<<"Volunteer cheated!"<<endl;
		else if(flag > 1) cout<<"Bad magician!"<<endl;
  else  cout<<haha<<endl;

	}
}
