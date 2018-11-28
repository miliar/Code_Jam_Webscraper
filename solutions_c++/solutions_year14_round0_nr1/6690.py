#include <iostream>

using namespace std;

int find_card(int card, int row[4]){
  if(row[0] == card)
    return 0;
  else if(row[1] == card)
    return 1;
  else if(row[2] == card)
    return 2;
  else if(row[3] == card)
    return 3;
  else
    return -1;
}

void trick(int icase){
  int ans1;
  cin >> ans1;
  int row1[4];
  for(int r = 1; r <= 4; ++r){
    for(int c = 1; c <= 4; ++c){
      int card;
      cin >> card;
      if(ans1 == r)
        row1[c - 1] = card;
    }
  }

  int ans2;
  cin >> ans2;
  int nfound = 0;
  int result;
  for(int r = 1; r <= 4; ++r)
    for(int c = 1; c <= 4; ++c){
      int card;
      cin >> card;
      if(r == ans2){
        if(find_card(card, row1) != -1){
          nfound++;
          result = card;
        }
      }
    }

  cout << "Case #" << icase << ": ";
  switch(nfound){
  case 0:
    cout << "Volunteer cheated!";
    break;
  case 1:
    cout << result;
    break;
  default:
    cout << "Bad magician!";

  }

  cout << endl;
}

int main(int argc, char* argv[])
{
  int ncase;
  cin >> ncase;
  for(int icase = 0; icase < ncase; ++icase)
    trick(icase + 1);

	return 0;
}

