#include<iostream>
#include<vector>
#include<set>

#define FOR(i,a,b) for(int i=a; i<b; i++)

using std::cout;
using std::cin;
using std::vector;
using std::set;

int main(){
  int T;
  cin >> T;
  FOR(t,1,T+1) {
    int first_row, second_row, card;
    vector<vector<int> > first(4,vector<int>(4));
    vector<vector<int> > second(4,vector<int>(4));
    cin >> first_row;
    first_row--;
    FOR(i,0,4){
      FOR(j,0,4){
	cin >> first[i][j];
      }
    }
    cin >> second_row;
    second_row--;
    FOR(i,0,4){
      FOR(j,0,4){
	cin >> second[i][j];
      }
    }
    set<int> poss_cards;
    FOR(i,0,4){
      if(!poss_cards.insert(first[first_row][i]).second) 
	card = first[first_row][i];
      if(!poss_cards.insert(second[second_row][i]).second) 
	card = second[second_row][i];
    }
    if(poss_cards.size() == 7)
      cout << "Case #" << t << ": " << card << "\n";
    else if(poss_cards.size() < 7)
      cout << "Case #" << t << ": Bad magician!" << "\n";
    else 
      cout << "Case #" << t << ": Volunteer cheated!" << "\n";
  }
  return 0;
}