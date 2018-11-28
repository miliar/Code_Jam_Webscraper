#include <iostream>
#include <vector>
#include <cmath>
#define  N 4
#define  rep(i,n) for(int i=0;i<(n);++i)
using namespace std;

typedef vector<int> Vi;
typedef vector<Vi> VVi;

int main(){
  int n; cin>>n;
  rep(i,n){
    int b_ans=(1<<16)-1;
    rep(t,2){
      int volunteer_answer; cin>>volunteer_answer; 
      VVi cell(N,Vi(N));
      rep(i,N) rep(j,N) cin>>cell[i][j];

      int tmp_ans=0;
      rep(i,N)
        tmp_ans |= (1<<(cell[volunteer_answer-1][i]-1));

      b_ans &= tmp_ans;
    }
    
    int bit=__builtin_popcount(b_ans);
    cout<<"Case #"<<(i+1)<<": ";
    if(bit==1) cout << log2(b_ans)+1;
    else if(bit>1) cout << "Bad magician!";
    else cout << "Volunteer cheated!";
    cout << endl;    
  }
}
