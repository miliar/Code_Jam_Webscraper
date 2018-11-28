#include<iostream>
#include<cstdio>
using namespace std;
int a[4][4];
int b[4][4];
int main()
{
	int tt,r1,r2,elm,vl;
	cin>>tt;
	for(int t=1;t<=tt;t++)
	{	
		cin>>r1;r1--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
				cin>>a[i][j];
		}
		cin>>r2;r2--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
				cin>>b[i][j];
		}
		int cnt = 0;
		for(int i=0;i<4;i++){
			int vl = a[r1][i];
			for(int j=0;j<4;j++){
				if(vl == b[r2][j]){
					cnt++;
					elm=vl;
				}
			}
		}
		if(cnt == 0)
			cout << "Case #"<<t<<": "<< "Volunteer cheated!" <<endl;	
		else if(cnt == 1)
			cout << "Case #"<<t<<": "<< elm <<endl;
		else if(cnt > 1)
			cout << "Case #"<<t<<": "<< "Bad magician!" <<endl;
	}
	return 0;
}

