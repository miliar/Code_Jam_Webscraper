#include <iostream>
#include <stdio.h>
using namespace std;
bool isEmpty(int p , int a[100])
{
	int i ;
	for(i = 0 ; i < p ; i++)
		if(a[i] != 0)
			return false;
	return true;
}
void evacuate(int p , int parties[100])
{
	int max1, i , p1 , p2 , no_of_max1  , t;
	max1 = 0;
	i = 0;
	p1 = 0;
	p2 = 0;
	no_of_max1 = 0;
	while(!(isEmpty(p , parties)))
	{
		max1 = 0;
		no_of_max1 = 0;
		p1 = 0;
		p2 = 0;
		for(i = 0 ; i < p ; i++)
		{
			//cout<<max1 << parties[i]<<endl;
			if(max1 < parties[i])
			{
			//	cout<<"in 1"<<endl;
				no_of_max1 = 1;
				max1 = parties[i];
				p1 = i;
			}else if(max1 == parties[i])
			{
			//	cout<<"in 2"<<endl;
				no_of_max1++;
				p2 = i;
			}
			//cin>>t;
		}
			if(no_of_max1 == 2)
			{
				printf("%c%c ",p1 +65 , p2 + 65);
				parties[p1]--;
				parties[p2]--;
			}
			else
			{
				printf("%c "  , p1 + 65);
				parties[p1]--;
			}
	}
}

int main()
{
	int T , i , parties[100] , j , p;
	cin >> T;
	i = 0;
	while(i != T)
	{
		cin >> p;
		j = 0;
		cout<<"Case #"<<i+1<<": ";
		
		while(j != p)
		{	
			cin>> parties[j];
			j++;
		}

		evacuate(p , parties);
		cout<<endl;
		i++;
	}
}