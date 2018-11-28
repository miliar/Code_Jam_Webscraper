#include <vector>
#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

int log2(int n) {
  int a=n;
  if(n==1)
    return 1;
  int cpt=0;
  while(a>1) {

    if(a%2==1) 
      return -1;
    a/=2;
    cpt++;
  }
  return cpt;
}

int find(int n) {
  int i=1;
  int cpt=0;
  while(2*i<n) {
    cpt++;
    i*=2;
  }
  return cpt;
}


int main() {
  int nb_cas;
  int cas;
  int l2;
  int ans;
  int p,q;
  cin >> nb_cas;
  for(cas=1;cas<=nb_cas;cas++) {
    //    cin >> p >> q;
    scanf("%d/%d",&p,&q);
    //    cout <<  p << " " << q << endl;
    l2=log2(q);
    if(l2<0 ||l2>40) {
      ans=-1;
    }
    else {
      ans=l2-find(p);
    }
    //    cout << "l2 " << l2 << " findp " << find(p) << endl;
    cout << "Case #" << cas << ": ";
    if(ans==-1)
      cout << "impossible"<< endl;
    else
      cout << ans << endl;
  }
  

  return 0;
}
