#include <iostream>
#include <vector>

using namespace std;

#define SIZE 4

int findCard(int firstAnswer, int firstCards[SIZE][SIZE], int secondAnswer, int secondCards[SIZE][SIZE])
{
  int firstRow[SIZE]={0}, secondRow[SIZE]={0};
  vector<int> cards;

  for(int i=0; i<SIZE; i++)
    firstRow[i] = firstCards[firstAnswer-1][i];

  for(int i=0; i<SIZE; i++)
    secondRow[i] = secondCards[secondAnswer-1][i];

  for(int i=0; i<SIZE; i++)
  {
    for(int j=0; j<SIZE; j++)
    {
      if(firstRow[i] == secondRow[j])
        cards.push_back(firstRow[i]);
    }
  }
  
  if(cards.size() == 1)
    return cards[0];
  else if(cards.size() > 1)
    return 0;
  else 
    return -1;
}

int main()
{
  int n;
  cin >> n;

  for(int x=0; x<n; x++)
  {
    int firstAnswer, secondAnswer;
    int firstCards[SIZE][SIZE], secondCards[SIZE][SIZE];

    cin >> firstAnswer;

    for(int i=0; i<SIZE; i++)
    {
      for(int j=0; j<SIZE; j++)
        cin >> firstCards[i][j];
    }

    cin >> secondAnswer;

    for(int i=0; i<SIZE; i++)
    {
      for(int j=0; j<SIZE; j++)
        cin >> secondCards[i][j];
    }

    int card = findCard(firstAnswer, firstCards, secondAnswer, secondCards);

    if(card > 0)
      cout << "Case #" << x+1 << ": " << card << endl;
    else if(card == 0)
      cout << "Case #" << x+1 << ": " << "Bad magician!" << endl;
    else if(card == -1)
      cout << "Case #" << x+1 << ": " << "Volunteer cheated!" << endl;

  }

  return 0;
}

