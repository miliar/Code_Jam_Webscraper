#include<bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)

int arr[5][5][5];

int main()
{
	ios::sync_with_stdio(false);
	
	arr[1][1][1]=1;
	arr[2][1][1]=1;
	arr[2][1][2]=1;
	arr[3][1][1]=1;
	arr[4][1][1]=1;
	arr[4][1][2]=1;
	arr[1][2][1]=1;
	arr[1][2][2]=1;
	arr[2][2][1]=1;
	arr[2][2][2]=1;
	arr[3][2][1]=1;
	arr[3][2][2]=1;
	arr[3][2][3]=1;
	arr[4][2][1]=1;
	arr[4][2][2]=1;
	arr[1][3][1]=1;
	arr[2][3][1]=1;
	arr[2][3][2]=1;
	arr[2][3][3]=1;
	arr[3][3][1]=1;
	arr[4][3][1]=1;
	arr[4][3][2]=1;
	arr[4][3][3]=1;
	arr[1][4][1]=1;
	arr[1][4][2]=1;
	arr[2][4][1]=1;
	arr[2][4][2]=1;
	arr[3][4][1]=1;
	arr[3][4][2]=1;
	arr[3][4][3]=1;
	arr[4][4][1]=1;
	arr[4][4][2]=1;
	arr[3][3][3]=1;
	arr[4][3][4]=1;
	arr[3][4][4]=1;
	arr[4][4][4]=1;
	
	int t;
	cin>>t;
	FOR(i,1,t+1)
	{
		cout<<"Case #"<<i<<": ";
		
		int x,r,c;
		cin>>x>>r>>c;
		
		if(arr[r][c][x])
			cout<<"GABRIEL";
		
		else
			cout<<"RICHARD";
		
		cout<<"\n";
	}	
		
	return 0;
}
