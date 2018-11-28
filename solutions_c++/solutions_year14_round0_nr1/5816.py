#include <iostream>
#include <fstream>
#include <set>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{

  ifstream infile(argv[1]);
  int numCases, answer, temp;
  set<int> possible;
  vector<int> board;

  infile >> numCases;

  for (int i = 0; i < numCases; i++)
  {
    int numSame = 0;
    int card;
    infile >> answer;
    for (int j = 0; j < 16; j++)
    {
      infile >> temp;
      board.push_back(temp);
    }
    answer = answer * 4 - 4;
    for (int k = answer; k < answer + 4; k++)
    {
      possible.insert(board[k]);
    }
    infile >> answer;
    board.clear();
    for (int j = 0; j < 16; j++)
    {
      infile >> temp;
      board.push_back(temp);
    }
    answer = answer * 4 - 4;
    for (int k = answer; k < answer + 4; k++)
    {
      if (!possible.insert(board[k]).second)
      {
        card = board[k];
        numSame++;
      }
    }
    cout << "Case #" << i + 1 << ": ";
    if (!numSame)
      cout << "Volunteer cheated!" << endl;
    else if (numSame > 1)
      cout << "Bad magician!" << endl;
    else 
      cout << card << endl;

    board.clear();
    possible.clear();
  }

  return 0;

}
