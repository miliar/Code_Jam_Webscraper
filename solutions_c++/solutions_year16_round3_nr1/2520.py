#include <iostream>
#include <map>
#include <vector>
#include <assert.h>
#define mc map<int, vector<char> >


using namespace std;

int main() {
  int T, N;

  cin>>T;



  for (int k = 0; k < T; k++) {
    cin>>N;
    mc d;
    int S = 0;
    for (int i = 0; i < N; i++) {
      char p = i + 'A';
      int q;
      cin>>q;
      d[q].push_back(p);
      S += q;
    }

    cout<<"Case #"<<(k+1)<<": ";
    while (S > 0) {
      //cout<<"\t "<<S<<endl;
      mc::reverse_iterator it = d.rbegin();

      vector<char>::iterator vit;
      int num = it->first;
      assert (it->second.size() > 0);
      if (it->second.size() == 1 || (num == 1 && it->second.size() > 2)) {
        vit = (it->second).begin();
        char v1 = *(vit);
        cout<<*(vit)<<" ";
        if (num > 1) {
          d[--num].push_back(v1);
        }

        if (it->second.size() == 1)
          d.erase(it->first);
        else
          it->second.erase((it->second).begin(), (it->second).begin() + 1);
        S--;
      } else {
        vit = (it->second).begin();
        char v1 = *(vit);
        char v2 = *(++vit);
        cout<<v1<<v2<<" ";
        if (it->second.size() == 2) {
          d.erase(it->first);
        } else {
          it->second.erase((it->second).begin(), (it->second).begin() + 2);
        }

        if (num > 1) {
          num--;
          d[num].push_back(v1);
          d[num].push_back(v2);
        }
        S-=2;
      }

    }
    cout<<endl;
  }

}