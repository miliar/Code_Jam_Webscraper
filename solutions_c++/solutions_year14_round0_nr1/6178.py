#include <iostream>
using namespace std;
int arr[5][5];
int check[17];
int main(int argc, char const *argv[])
{
	int t,i,j,c;
	cin>>t;
	int rownum;
	for(c=1;c<=t;c++){
		for(i=1;i<=16;i++)check[i]=0;
		cin>>rownum;
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++)cin>>arr[i][j];
		}
		for(i=1;i<=4;i++){
			check[arr[rownum][i]]++;
		}
		cin>>rownum;
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++)cin>>arr[i][j];
		}
		for(i=1;i<=4;i++){
			check[arr[rownum][i]]++;
		}
		int res = 0;
		int resct = 0;
		for(i=1;i<=16;i++){
			if(check[i]==2){
				res = i;
				resct++;
			}
		}
		cout<<"Case #"<<c<<": ";
		if(resct==0)cout<<"Volunteer cheated!";
		else if(resct>1)cout<<"Bad magician!";
		else cout<<res;
		cout<<endl;
	}
	return 0;
}