#include<iostream>
#include<string>
#include<cmath>
#include<vector>

using namespace std ;

int main()
{
	int t , counter = 0 ;
	cin>>t ;
	while(t--)
	{
		int ans1 , ans2 ;
		cin>>ans1 ;
		int a[4][4] ;
		for(int i = 0 ; i < 4 ; ++i)
			for(int j = 0 ; j < 4 ; ++j)
				cin>>a[i][j] ;
		int temp[4] ;
		for(int i = 0 ; i < 4 ; ++i)
			temp[i] = a[ans1-1][i] ;
		cin>>ans2 ;
		int cnt = 0 ;
		int b[4][4] ;
		int flag ;
		for(int i = 0 ; i < 4 ; ++i)
			for(int j = 0 ; j < 4 ; ++j)
			{
				cin>>b[i][j] ;
				if(i == ans2-1)
				{
					for(int k = 0 ; k < 4 ; ++k)
						if(temp[k] == b[i][j])
						{
							++cnt ;
							flag = temp[k] ;
						}
				}
			}
		++counter ;
		if(cnt == 1)
			cout<<"Case #"<<counter<<": "<<flag<<endl ;
		else if(cnt > 1)
			cout<<"Case #"<<counter<<": Bad magician!"<<endl ;
		else
			cout<<"Case #"<<counter<<": Volunteer cheated!"<<endl ;
	}
	return 0 ;
}
		
