#include <fstream>
#include <vector>
#include <iostream>
#include <cstdlib>

using namespace std;

struct game{
  string board[10];
};

int charToPlayer(char input){
  if(input == '.') return 0;
  if(input == 'T') return 1;
  if(input == 'X') return 2;
  if(input == 'O') return 3;
}

int lineEval(string line){
  int player = charToPlayer(line[0]);
  bool noWin = false;

  if(player == 0) return 0;

  for(int i = 1; i < 4; i++){
    int temp = charToPlayer(line[i]);
    if(temp == 0) return 0;

    if(player == 1) player = temp;

    if(noWin == false)
      if(player % temp != 0)
	noWin = true;

  }

  if(noWin == true) return 1;
  else return player;
}

int gameEval(game instance){
  bool allComplete = true;

  for(int i = 0; i < 10; i++){
    int temp = lineEval(instance.board[i]);
    
    if(temp > 1) return temp;
    if(temp == 0) allComplete = false;
  }

  return allComplete;
}

vector<game> getGames(){
  ifstream infile;

  infile.open("A-large.in");

  string s;
  getline(infile, s);

  vector<game> temp;
  temp.resize(atoi(s.c_str()));

  for(int i = 0; i < temp.size(); i++){
    for(int j = 0; j < 4; j++){
      getline(infile, temp[i].board[j]);
    }

    if(i != temp.size()-1) getline(infile, s);

    for(int j = 0; j < 4; j++){
      s = "";
      for(int k = 0; k < 4; k++)
	s += temp[i].board[k][j];
      
      temp[i].board[j+4] = s;
    }

    s = "";
    for(int j = 0; j < 4; j++)
      s += temp[i].board[j][j];
    
    temp[i].board[8] = s;

    s = "";
    for(int j = 0; j < 4; j++)
      s += temp[i].board[3-j][j];
    
    temp[i].board[9] = s;
  }

  infile.close();

  return temp;
}

string output(int input){
  if(input == 0) return ": Game has not completed";
  if(input == 1) return ": Draw";
  if(input == 2) return ": X won";
  if(input == 3) return ": O won";
}

int main(){
  vector<game> gamelist = getGames();

  ofstream outfile;

  outfile.open("output-large.txt");

  for(int i = 0; i < gamelist.size(); i++)
    outfile << "Case #" << i+1 << output(gameEval(gamelist[i])) << endl;

  outfile.close();

  return 0;
}
