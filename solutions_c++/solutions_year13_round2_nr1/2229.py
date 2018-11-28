#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int getCount(vector<int> mot, int mote);

int main(int argc, char* argv[]){
  int T;
  cin>>T;
  int index=1;
  while(index <= T){
    int mote;
    int n;
    cin>>mote>>n;
    vector<int> mot;
    for(int i=0; i<n; i++){
      int m;
      cin>>m;
      mot.push_back(m);
    }
    sort(mot.begin(), mot.end());
    int ops = getCount(mot, mote);
    cout<<"Case #"<<index<<": "<<ops<<endl;
    index++;
  }
  return 0;
}

int getCount(vector<int> mot, int mote){
  if(mot.size() == 1){
    if(mot[0] < mote)
      return 0;
    else
      return 1;
  }
  if(mote == 1)
    return mot.size();
  int x = mot.front();
  if(x < mote){
    mot.erase(mot.begin());
    return getCount(mot, mote+x);
  }
  else if(x == mote){
    if(mote > 1){
      return 1+getCount(mot, mote+mote-1);
    }
    if(mote == 1){
      return mot.size();
    }
  }
  else {
    int b = 1 + getCount(mot, mote+mote-1);
    mot.erase(mot.begin());
    int t = 1 + getCount(mot, mote);
    if(t < b)
      return t;
    else
      return b;
  }
}
