#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
  int T;
  cin >> T;
  int tcase=1;
  while(T--){
    int r1;
    cin >> r1;
    vector< vector<int> > arrangement1, arrangement2;
    for(int i = 0; i < 4; ++i){
      vector<int> inner;
      for(int j = 0; j < 4; ++j){
	int tmp;
	cin >> tmp;
	inner.push_back(tmp);
      }
      arrangement1.push_back(inner);
    }
    int r2;
    cin >> r2;
    for(int i = 0; i < 4; ++i){
      vector<int> inner;
      for(int j = 0; j < 4; ++j){
	int tmp;
	cin >> tmp;
	inner.push_back(tmp);
      }
      arrangement2.push_back(inner);
    }
    vector<int> magicCard;
    vector<int> magicRow(arrangement1[r1-1].begin(), arrangement1[r1-1].end()), myRow(arrangement2[r2-1].begin(), arrangement2[r2-1].end());
    sort(magicRow.begin(),magicRow.end());
    sort(myRow.begin(), myRow.end());
    vector<int>::iterator it1 = magicRow.begin();
    for(vector<int>::iterator it2 = myRow.begin(); it1 != magicRow.end() && it2 != myRow.end(); ){
      if(*it1 < *it2)
	++it1;
      else if(*it1 > *it2)
	++it2;
      else{
	magicCard.push_back(*it1);
	++it1; ++it2;
      }
    }
    cout << "Case #" << tcase++ << ": ";
    if(magicCard.size() == 1){
      cout << magicCard[0] << endl;
    }
    else if(magicCard.size() > 1){
      cout << "Bad magician!" << endl;
    }
    else{
      cout << "Volunteer cheated!" << endl;
    }
  }
  return 0;
}
