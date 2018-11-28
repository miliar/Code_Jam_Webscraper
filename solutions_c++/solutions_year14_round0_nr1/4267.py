// magicTrick.cpp : main project file.

#include <set>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{    
	int num;
	set<int> s1;
	set<int> s2;
	set<int> s3;
	
	cin >> num;
	for(int i =0;i < num;i ++)
	{
		s1.clear();
		s2.clear();
		s3.clear();
		int row;
		cin >>row;
		for(int j =1; j <= 16; j ++)
		{
			int tmp;
			cin >> tmp;			
			if(( (j/4 == row-1) && (j%4 != 0)) || ((j/4 == row) && (j%4 == 0)))
			{	
				s1.insert(tmp);
			}
		}
		
		cin >> row;
		for(int j= 1; j <= 16; j ++)
		{
			int tmp;
			cin >> tmp;
			if(( (j/4 == row-1) && (j%4 != 0)) || ((j/4 == row) && (j%4 == 0)))
			{	
				s2.insert(tmp);
			}
		}
		
		set<int>::iterator it = s3.begin();
		set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), inserter(s3, it));
				
		cout<<"Case #"<<i+1<<": ";
		
		if(s3.size() == 0) cout<<"Volunteer cheated!";
		else if(s3.size() == 1) cout<<*s3.begin();
		else cout<<"Bad magician!";
		cout<<endl;		
	}	
    return 0;
}
