//#include<bits/stdc++.h>
#include<iostream>
using namespace std;
int main()
{
	//freopen("A-small-attempt0.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
	int test = 0;
	cin>>test;
	int t=0;
	int a[4][4]={0}, b[4][4]={0};
	while(++t <= test )
	{
		int x=0,y=0, count=0 ,num=0;
		cin>>x;
		for(int i=0;i<4;i++)
		{
			for(int j=0 ;j<4;j++ )
			{
				cin>> a[i][j] ;
			}
		}
		cin>>y;
		
		for(int i=0;i<4;i++)
		{
			for(int j=0 ;j<4;j++ )
			{
				cin>> b[i][j] ;
			}
		}
		for( int i= 0; i<4; i++ )
		{
			for( int j =0 ; j< 4; j++ )
			{
				if( a[x-1][i] == b[y-1][j] )
				{
					count++;
					num = a[x-1][i];					
				}
			}
		}
		if(count == 0 )
		{
			cout<<"Case #"<<t<<": Volunteer cheated!"<<endl;
		}
		else if( count == 1)
		{
			cout<< "Case #"<<t<<": " << num << endl;
		}
		else
		{
			cout<< "Case #"<<t<<": Bad magician!" <<endl;
		}
	}
	return 0;
}
