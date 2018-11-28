#include<iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include<cstdlib>
#include<climits>
#define pi acos(-1.0)
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	char arr[4][4];
	string str;
	scanf("%d",&test);
	for (int CASE = 1; CASE <= test; CASE++)
	{
		for (int i =0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin>>arr[i][j];
			}
		}
		bool win=true;
		bool dot=false;
		for (int i = 0; i < 4; i++)
		{
			if(arr[0][i]=='.'){
				dot=true;
				break;
			}
		}
		char player='.',current;
		if(!dot){
			if(arr[0][0]!='T')
				current=arr[0][0];
			else
				current =arr[0][1];
			for (int i = 1; i < 4; i++)
			{
				if(arr[0][i]!='T'){
					if(arr[0][i]!=current)
					{
						win=false;
						break;
					}}
			}
		}
		if(win && !dot)player=current;
		dot=false;
		for (int i = 0; i < 4; i++)
		{
			if(arr[1][i]=='.'){
				dot=true;
				break;
			}
		}
		if(!dot && player=='.'){
			win=true,player='.';
			if(arr[1][0]!='T')
				current=arr[1][0];
			else
				current =arr[1][1];
			for (int i =1; i < 4; i++){
				if(arr[1][i]!='T'){
					if(arr[1][i]!=current)
					{
						win=false;
						break;
					}}
			}
			if(win && !dot)player=current;
		}
		dot=false;
		for (int i = 0; i < 4; i++)
		{
			if(arr[2][i]=='.'){
				dot=true;
				break;
			}
		}
		if(!dot && player=='.'){
			win=true,player='.';
			if(arr[1][0]!='T')
				current=arr[2][0];
			else
				current =arr[2][1];
			for (int i =1; i < 4; i++){
				if(arr[2][i]!='T'){
					if(arr[2][i]!=current)
					{
						win=false;
						break;
					}}
			}
			if(win && !dot)player=current;
		}
		dot=false;
		for (int i = 0; i < 4; i++)
		{
			if(arr[3][i]=='.'){
				dot=true;
				break;
			}
		}
		if(!dot && player=='.'){
			win=true,player='.';
			if(arr[3][0]!='T')
				current=arr[3][0];
			else
				current =arr[3][1];
			for (int i =1; i < 4; i++){
				if(arr[3][i]!='T'){
					if(arr[3][i]!=current)
					{
						win=false;
						break;
					}}
			}
			if(win && !dot)player=current;
		}
		dot=false;
		for (int i = 0; i < 4; i++)
		{
			if(arr[i][0]=='.'){
				dot=true;
				break;
			}
		}
		if(!dot && player=='.'){
			win=true,player='.';
			if(arr[0][0]!='T')
				current=arr[0][0];
			else
				current =arr[1][0];
			for (int i =1; i < 4; i++){
				if(arr[i][0]!='T'){

					if(arr[i][0]!=current)
					{
						win=false;
						break;
					}}
			}
			if(win && !dot)player=current;
		}
		dot=false;
		for (int i = 0; i < 4; i++)
		{
			if(arr[i][1]=='.'){
				dot=true;
				break;
			}
		}
		if(!dot && player=='.'){
			win=true,player='.';
			if(arr[0][1]!='T')
				current=arr[0][1];
			else
				current =arr[1][1];
			for (int i =1; i < 4; i++){
				if(arr[i][1]!='T'){

					if(arr[i][1]!=current)
					{
						win=false;
						break;
					}}
			}
			if(win && !dot)player=current;
		}
		dot=false;
		for (int i = 0; i < 4; i++)
		{
			if(arr[i][2]=='.'){
				dot=true;
				break;
			}
		}
		if(!dot && player=='.'){
			win=true,player='.';
			if(arr[0][2]!='T')
				current=arr[0][2];
			else
				current =arr[1][2];
			for (int i =1; i < 4; i++){
				if(arr[i][2]!='T'){

					if(arr[i][2]!=current)
					{
						win=false;
						break;
					}}
			}
			if(win && !dot)player=current;
		}
		dot=false;
		for (int i = 0; i < 4; i++)
		{
			if(arr[i][3]=='.'){
				dot=true;
				break;
			}
		}
		if(!dot && player=='.'){
			win=true,player='.';
			if(arr[0][3]!='T')
				current=arr[0][3];
			else
				current =arr[1][3];
			for (int i =1; i < 4; i++){
				if(arr[i][3]!='T'){
					if(arr[i][3]!=current)
					{
						win=false;
						break;
					}}
			}
			if(win && !dot)player=current;
		}
		dot=false;
		for (int i = 0,x=3; i < 4,x>=0; i++,x--)
		{
			if(arr[i][x]=='.'){
				dot=true;
				break;
			}
		}
		if(!dot && player=='.'){
			win=true,player='.';
			if(arr[0][3]!='T')
				current=arr[0][3];
			else
				current =arr[1][2];
			for (int i =1,x=2; i < 4,x>=0; i++,x--){
				if(arr[i][x]!='T' && arr[i][x]!=current ){
					win=false;
					break;
				}
			}
			if(win && !dot)player=current;
		}
		dot=false;
		for (int i = 0,x=0; i < 4,x<4; i++,x++)
		{
			if(arr[i][x]=='.'){
				dot=true;
				break;
			}
		}
		if(!dot && player=='.'){
			win=true,player='.';
			if(arr[0][0]!='T')
				current=arr[0][0];
			else
				current =arr[1][1];
			for (int i =1,x=1; i < 4,x<4; i++,x++){
				if(arr[i][x]!='T' & arr[i][x]!=current){
					win=false;
					break;
				}
			}
			if(win)player= current;
		}
		cin.ignore();
		getline(cin,str);
		if(player!='X' && player!='O')
			win=false;
		if(win){
			printf("Case #%d: %c won\n",CASE,player);
			continue;
		}
		if(dot)
			printf("Case #%d: Game has not completed\n",CASE);
		else
			printf("Case #%d: Draw\n",CASE);
	}
	return 0;
}