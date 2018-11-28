#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
int main(){
	int t,it=1;
	cin >> t;
	while(t--){
		int a[4][4],b[4][4];
		int m,n,c=0,ans;
		cin>>m;;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin>>a[i][j];
			}
			
		}
		cin>>n;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin>>b[i][j];
			}
			
		}
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if(a[m-1][i]==b[n-1][j]){
					c++;
					ans=a[m-1][i];
				}
			}
			
		}
		cout << "Case #"<<it<<": ";
		if(c==1){
			cout<<ans;
		}
		else if(c==0){
			cout<<"Volunteer cheated!";
		}
		else
		cout<<"Bad magician!";
		
		cout<<"\n";
		it++;
		
	}
	return 0;
}

