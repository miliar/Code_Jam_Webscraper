#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<cstring>
#include<vector>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<set>
#include<utility>
#include<algorithm>
#include<map>
#include<numeric>

using namespace std;

template <typename T, size_t N>
T* begin(T(&arr)[N]) { return &arr[0]; }
template <typename T, size_t N>
T* end(T(&arr)[N]) { return &arr[0]+N; }

typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<vector<int> > VVI;

#define IFOR(i, a, b) for(int i = (a); i < (b); ++i)
#define EFOR(i, a, b) for(int i = (a); i <= (b); ++i)
#define RESET(a, b) memset(a, b, sizeof(a))
#define ALL(a) (a).begin(), (a).end()
#define PB push_back
#define MP make_pair

struct cards{
  int row;
  int arr[4][4];
};

int main(){
  int T;
  cin>>T;
  IFOR(t, 0, T){
    // get inputs
    cards pool[2];
    IFOR(i,0,2){
      cin>>pool[i].row;
      IFOR(j,0,4){
        IFOR(k,0,4){
          cin>>pool[i].arr[j][k];
        }
      }
    } 
    // solution
    int row0 = pool[0].row-1;
    int row1 = pool[1].row-1;
    VI match;
    IFOR(i, 0, 4){
      IFOR(j, 0, 4){
        //cout<< "Check: "<<pool[0].arr[row0][i]<< " " << pool[1].arr[row1][j]<< endl;
        if(pool[0].arr[row0][i]==pool[1].arr[row1][j]){
          match.PB(pool[0].arr[row0][i]);
        }
      }
    }
    // print answers
    if(match.size()==0){
      cout<< "Case #"<<t+1<<": Volunteer cheated!\n";
    }else if(match.size()==1){
      cout<< "Case #"<<t+1<<": "<< match[0]<< "\n";
    }else{
      cout<< "Case #"<<t+1<<": Bad magician!\n";
    }
  }


  return 0;
}
