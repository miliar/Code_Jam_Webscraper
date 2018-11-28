#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include<sstream>
#include<string>
#include<algorithm>

using namespace std;

string xwon = "X won";
string owon = "O won";
string draw = "Draw";
string notfinished = "Game has not completed";

void print_result(int i, string result)
{
	if (i != 1)
		cout << endl;
	cout<<"Case #"<< i<< ": ";
	cout << result;
}

string judge(char c){
  if(c=='X')
	  return xwon;
  if(c=='O')
	  return owon;
}

string judgeGame(vector<string> game){
	char initial = ' ';
	char empty_flag ='F';
	for(int i=0; i<4; i++){
		for(int j=0; j<=4; j++){
			if(j==4)
				return judge(initial);
		    if((j==0||initial=='T')&&game[i][j]!='.'){
				initial = game[i][j];
				continue;
			}
			if(game[i][j]=='T')
				continue;
			if(game[i][j]=='.'){
			    empty_flag = 'T';
				break;
			}
			if(game[i][j]!=initial)
				break;
		}
	}

	for(int j=0; j<4; j++){
		for(int i=0; i<=4; i++){
			if(i==4)
				return judge(initial);
		     if((i==0||initial=='T')&&game[i][j]!='.'){
				initial = game[i][j];
				continue;
			}
			if(game[i][j]=='T')
				continue;
			if(game[i][j]=='.'){
			    empty_flag = 'T';
				break;
			}
			if(game[i][j]!=initial)
				break;
		}
	}

	for(int i=0; i<=4; i++){
		if(i==4) return judge(initial);
		if((i==0||initial=='T')&&game[i][i]!='.'){
		   initial = game[i][i];
		   continue;
		}
		if(game[i][i]=='T')
			continue;
		if(game[i][i]=='.'){
			empty_flag = 'T';
		    break;
		}
		
		if(game[i][i]!=initial)
			break;
	}

	for(int i=0; i<=4; i++){
		if(i==4) return judge(initial);
	    if((i==0||initial=='T')&&game[i][3-i]!='.'){
		   initial = game[i][3-i];
		   continue;
		}
		if(game[i][3-i]=='T')
			continue;
		if(game[i][3-i]=='.'){
			empty_flag = 'T';
		    break;
		}
		if(game[i][3-i]!=initial)
			break;
	}
	if(empty_flag == 'F')
	  return draw;
	else
	  return notfinished;
}

void main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int num_case;
	string str;
	string result;
    cin>>num_case;

	for(int i=1; i <= num_case; i++)
		{ 
	        getline(cin,str); //get to the second line 
	        vector<string> game; 
			for(int j=0; j<4; j++){
	          getline(cin,str);
			  game.push_back(str);
			}
			result = judgeGame(game);
            print_result(i, result);

		}
	fclose (stdin);
	fclose (stdout);
}



