#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

vector<int> row1, row2;

void get_input(){
  int row,t;
  row1.resize(0);
  row2.resize(0);
  scanf("%d",&row);
  for(int i=0;i<4;i++)
    for(int j=0;j<4;++j){
      scanf("%d",&t);
      if(row == i+1)
	row1.push_back(t);
    }
  scanf("%d",&row);
  for(int i=0;i<4;i++)
    for(int j=0;j<4;++j){
      scanf("%d",&t);
      if(i+1==row)
	row2.push_back(t);
    }
}

//  - bad magician
// positive number - answer
// 0 - Volunteer cheated
int solve(){
  vector<int> intersect(3);
  vector<int>::iterator it;
  sort(row1.begin(),row1.end());
  sort(row2.begin(),row2.end());

  it = set_intersection(row1.begin(),row1.end(), row2.begin(), row2.end(),intersect.begin());
  intersect.resize(it-intersect.begin());
  
  if(intersect.size() == 0) //volunteer cheated
    return 0; 
  else if( intersect.size()==1) // good, get a answer
    return intersect[0];
  else        //bad magician
    return -1;
}

int main(){
  int T;
  int caseNum = 1;
  scanf("%d",&T);
  while(T--){
    get_input();
    int ret = solve();

    cout<<"Case #"<<caseNum++<<": ";
    if( ret == -1 )
      cout<<"Bad magician!"<<endl;
    else if( ret>0 )
      cout<<ret<<endl;
    else if( ret==0)
      cout<<"Volunteer cheated!"<<endl;
  }
  return 0;
}
