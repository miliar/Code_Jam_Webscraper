#include<iostream>

using namespace std;

inline unsigned int MIN(unsigned int A, unsigned int B) {
  return (A<B)?A:B;
}

unsigned int find_in_row(unsigned int C, unsigned int W) {
  unsigned int res;
  if (W==1)
    res=C;
  else if (W==2)
    res=MIN(((C+1)/2)+1, C);
  else if (W>=(C+1)/2)
    res=MIN(W+1,C);
  else {
    if (C%W==0) 
      res=MIN((C/W)+W-1,C);
    else
      res=MIN((C/W)+W,C);
    //    cout << (C%W) << endl;
  }
  return res;
}

/*{
  if (C%W==0) 
  res=MIN((C/W)+W,C);
  else if (C%W==1)
  res=MIN((C/W)+W,C);
  else 
  res=MIN((C/W)+W,C);
  else
  res=MIN((C/W)+W+1,C);
  }*/

int main() {
  unsigned int T;
  
  cin >> T;

  for (unsigned int t=1; t<=T; ++t) {
    unsigned int R, C, W;
    unsigned int res;
    cin >> R >> C >> W;
    res=find_in_row(C,W);
    cout << "Case #" << t << ": " << res << endl;


  }


  return 0;
  
}
