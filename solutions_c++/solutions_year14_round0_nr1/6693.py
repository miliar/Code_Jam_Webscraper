#include<iostream>
#include<iterator>
#include<vector>
#include<set>
#include<algorithm>
#include<cstdio>

using namespace std;

int main() {
  int T;
  cin>>T;
  for(int t=1;t<=T;++t) {
    int g1,g2;
    set<int>s1,s2;
    vector<int>v;

    cin>>g1;
    for(int i=0;i<4;i++) {
      for(int j=0;j<4;j++) {
	int tmp;
	cin>>tmp;
	if(i==g1-1)
	  s1.insert(tmp);
      }
    }

    cin>>g2;
    for(int i=0;i<4;i++) {
      for(int j=0;j<4;j++) {
	int tmp;
	cin>>tmp;
	if(i==g2-1)
	  s2.insert(tmp);
      }
    }

    set_intersection(s1.begin(),s1.end(),s2.begin(),s2.end(),back_inserter(v));

    printf("Case #%d: ",t);

    if(v.size()==1) {
      cout<<v[0]<<endl;
    } else if(v.size()==0) {
      cout<<"Volunteer cheated!\n";
    } else {
      cout<<"Bad magician!\n";
    }
  }
  return 0;
}
