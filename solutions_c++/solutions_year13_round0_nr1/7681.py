#include<iostream>
#include<cstdio>
#include<string>
#include<algorithm>
using namespace std ;


int main ( )
{
	int TestCase ;
	cin >> TestCase ;
	string str[10] ;
	for (int test = 1 ; test<=TestCase ; test ++ )
	{
		bool draw =true ;
		cin >> str[0];
		cin >> str[1];
		cin >> str[2];
		cin >> str[3];
		
		for (int i = 0 ; i < 4 ; i++ )
			for (int j = 0 ; j < 4 ; j++ )
				if ( str[i][j]=='.') draw=false;
				
		char winning ,winner;
		bool won = false ;
		
		for (int i = 0 ; i < 4 ; i++ )
		{
			winning = str[i][0];
			if (winning=='T') winning = str[i][1] ;
			if (winning=='.') continue;
			won=true;
			for (int j = 0 ; j < 4 ; j++ )
			{
				if (winning!=str[i][j]&& str[i][j]!='T')
					won=false;
			}
			if ( won==true) {
				winner=winning ;
				break;
			}
		}
		
		if(!won)
		for (int i = 0 ; i < 4 ; i++ )
		{
			winning = str[0][i];
			if (winning=='T') winning = str[1][i] ;
			if (winning=='.') continue;
			won=true;
			for (int j = 0 ; j < 4 ; j++ )
			{
				if (winning!=str[j][i]&& str[j][i]!='T')
					won=false;
			}
			if ( won==true) {
				winner=winning ;
				break;
			}
		}
		if(!won)
		for (int i = 0 ;i < 4 ; i++ )
		{
			won=true;
			winning = str[0][0];
			if (winning=='T') winning = str[1][1] ;
			if (winning=='.') 
			{
				won=false;
				break;
			}
			winner = winning;
			if ( winning!=str[i][i]&& str[i][i]!='T')
			{
				won=false;
			//	cout<<"sdfd  ";
				break;
			}
//			cout<<winner<<" ";
		}
		
		if(!won)
		for (int i = 0 ;i < 4 ; i++ )
		{
			won=true;
			winning = str[0][3];
			if (winning=='T') winning = str[1][2] ;
			if (winning=='.') 
			{
				won=false;
				break;
			}
			winner = winning;
			if ( winning!=str[i][3-i] && str[i][3-i]!='T')
			{
				won=false;
//				cout<<"in this\n";
				break;
			}
		}
				
		if (won)
		{
			cout <<"Case #"<<test<<": "<<winner<<" won\n";
		}
		else
		{
			if (draw)
				cout <<"Case #"<<test<<": Draw\n";
			else
				cout <<"Case #"<<test<<": Game has not completed\n";
		}

	}

	return 0 ;
}
