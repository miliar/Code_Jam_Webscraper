#include <iostream>
#include <string>
#include <stdio.h>
#include <conio.h>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <numeric>


using namespace std;

int main()
{
ifstream cin("D-small-attempt0.in");
ofstream cout("out.txt");
int X,R,C,T;
cin >> T;

for(int i = 0; i < T; i++)
{

	cin >> X>> R >> C;
	int total = R*C;
	
	switch(X){
		case 1:
			{
				cout <<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
				break;
			}
		case 2:
			{
				if(((total)% 2)==0)
				{	cout <<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
				break; }
				else
				{cout <<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
				break;}

			}
		case 3:
			{
				if((total)<3)
				{	cout <<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
				break; }
				else if(((total)%3)!=0)
				{	cout <<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
				break;}
				else if((total)==3)
				{cout <<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
				break;}
				else if((total==6)|(total==9)|(total==12))
				{cout <<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
				break;}
						
			}
		case 4:
			{
				if((total)<4)
				{	cout <<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
				break;}
				else if(((total)%4)!=0)
				{	cout <<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
				break;}
				else if((total==4)|(total==8))
				{cout <<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
				break;}
				else if((total==12)|(total==16))
				{	cout <<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
				break;}
			}

	}


}
}