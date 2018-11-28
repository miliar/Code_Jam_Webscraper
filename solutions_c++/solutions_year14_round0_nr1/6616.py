#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

typedef struct magic{
  int data[4][4];
  int row;
}magic;



int main(){
  //number of magic in file
  fstream file("A-small-attempt4.in", std::ios_base::in);
  int N;
  file >> N;

  vector<magic> magics;
  
  for(int i = 0; i < 2*N; i++){
    magic m;
    int tmp;

    file >> m.row;
    for(int j = 0; j < 4; j++){
      for(int k = 0; k < 4; k++)
	file >> m.data[j][k];
    }
    //    cout << m.data[3][3] << endl;
    magics.push_back(m);
  }
  file.close();

  ofstream result("result.txt");

  for(int i = 0; i < N; i++){
    magic m1 = magics[2*i];
    magic m2 = magics[2*i+1];

    int *row1 = m1.data[m1.row-1];
    int *row2 = m2.data[m2.row-1];

    vector<int> r1, r2;
    r1.assign(row1, row1 + 4);
    r2.assign(row2, row2 + 4);

    //cout << magics.size() << 
    //cout << r1[0] << endl;
    sort(r1.begin(), r1.end());
    sort(r2.begin(), r2.end());
    
    vector<int> intersection;
    
    set_intersection(r1.begin(), r1.end(), r2.begin(), r2.end(), back_inserter(intersection));
    if(intersection.size() == 1)
      result << "Case #"<<i+1<<": " <<intersection[0] << endl;
    else if(intersection.size() == 0)
      result << "Case #"<<i+1<<": " <<"Volunteer cheated!" << endl;
    else
      result << "Case #"<<i+1<<": " <<"Bad magician!" << endl;
  }
  
}









