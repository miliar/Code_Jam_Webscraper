#include <iostream>
#include <vector>
#include <string>

using namespace std;

int T,x,a1,a2,i,j;
vector<int> m1(4), m2(4);
string line;

void ignoreLines(int n)
{
  for(i=0;i<n;i++){
    getline(cin,line);
  }
}

int main()
{
  cin >> T;
  x=1;
  while(x<=T){
    cin >> a1;
    ignoreLines(a1);
    for(i=0;i<4;i++){
      cin >> m1[i];
    }
    ignoreLines((4-a1)+1);

    cin >> a2;
    ignoreLines(a2);
    for(i=0;i<4;i++){
      cin >> m2[i];
    }
    ignoreLines((4-a2)+1);

    vector<int> eq;
    for(i=0;i<4;i++){
      for(j=0;j<4;j++){
	if(m2[j] == m1[i]){
	  eq.push_back(m1[i]);
	}
      }
    }
    
    if(eq.size()==0){
      cout << "Case #" << x << ": Volunteer cheated!" << endl;
    } else if(eq.size()==1){
      cout << "Case #" << x << ": " << eq[0] << endl;
    } else if(eq.size()>1) {
      cout << "Case #" << x << ": Bad magician!" << endl;
    }
    x++;
  }
  
  return 0;
}
