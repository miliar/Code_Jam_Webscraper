#include <iostream>
#include <stdint.h>
using namespace std;
 
 int tabliczka(char x, char z){
 char B;
   if (x=='i'){
        if(z=='1') {B='i';}
        if(z=='i') {B='N';}
        if(z=='j') {B='k';}
        if(z=='k') {B='J';}
        if(z=='N') {B='I';}
        if(z=='I') {B='1';}
        if(z=='J') {B='K';}
        if(z=='K') {B='j';}  
        return B;
   }
        if (x=='j'){
        if(z=='1') {B='j';}
        if(z=='i') {B='K';}
        if(z=='j') {B='N';}
        if(z=='k') {B='i';}
        if(z=='N') {B='J';}
        if(z=='I') {B='k';}
        if(z=='J') {B='1';}
        if(z=='K') {B='I';}
        return B;
   }
        if (x=='k'){
        if(z=='1') {B='k';}
        if(z=='i') {B='j';}
        if(z=='j') {B='I';}
        if(z=='k') {B='N';}
        if(z=='N') {B='K';}
        if(z=='I') {B='J';}
        if(z=='J') {B='i';}
        if(z=='K') {B='1';}
        return B;
   }
        if (x=='1' ){
        if(z=='1') {B='1';}
        if(z=='i') {B='i';}
        if(z=='j') {B='j';}
        if(z=='k') {B='k';}
        if(z=='N') {B='N';}
        if(z=='I') {B='I';}
        if(z=='J') {B='J';}
        if(z=='K') {B='K';}
        return B;
   }
      if (x=='I'){
        if(z=='1') {B='I';}
        if(z=='i') {B='1';}
        if(z=='j') {B='K';}
        if(z=='k') {B='j';}
        if(z=='N') {B='i';}
        if(z=='I') {B='N';}
        if(z=='J') {B='k';}
        if(z=='K') {B='J';}  
        return B;
   }
        if (x=='J'){
        if(z=='1') {B='J';}
        if(z=='i') {B='k';}
        if(z=='j') {B='1';}
        if(z=='k') {B='I';}
        if(z=='N') {B='j';}
        if(z=='I') {B='K';}
        if(z=='J') {B='N';}
        if(z=='K') {B='i';}
        return B;
   }
        if (x=='K'){
        if(z=='1') {B='K';}
        if(z=='i') {B='J';}
        if(z=='j') {B='i';}
        if(z=='k') {B='1';}
        if(z=='N') {B='k';}
        if(z=='I') {B='j';}
        if(z=='J') {B='I';}
        if(z=='K') {B='N';}
        return B;
   }
        if (x=='N'){
        if(z=='1') {B='N';}
        if(z=='i') {B='I';}
        if(z=='j') {B='J';}
        if(z=='k') {B='K';}
        if(z=='N') {B='1';}
        if(z=='I') {B='i';}
        if(z=='J') {B='j';}
        if(z=='K') {B='k';}
        return B;
   }
 }
 
int main() {
 
  ios_base::sync_with_stdio(false);
 
  int T, L;
  int64_t X;
  char t[10001];
  char A;
 
  cin >> T;
  for (int i = 0; i < T; i++) {
   
    cin >> L;
    cin >> X;
   
    if (X > 12) {
      X = 12 + (X % 4);
    }
   
    for (int j=0; j<L; j++) {
      cin >> t[j];
    }
   
    A = 1;
    for (int k=0; k<X; k++) {
      for (int j=0; j<L; j++) {
        A = tabliczka(A , t[j]);
      }
    }
   
    if(L*X<3) {
      cout << "Case #" << i+1 << ": NO" << '\n';
    } else {
      if (A != 'N') {
        cout << "Case #" << i+1 << ": NO" << '\n';
      } else {
        A = 1;
        int k, j;
        for(k=0; k<X; k++) {
          for(j=0; j<L; j++) {
            A=tabliczka(A , t[j]);
            if (A=='i') break;
          }
          if (A=='i') break;
        }
        A = 1;
        int a, b=j+1;
        for (a=k; a<X; a++) {
          for (; b<L; b++){
            A=tabliczka(A, t[b]);
            if (A=='j') break;
          }
          if (A=='j') break;
          b=0;
        }
        if (A=='j') {
          cout << "Case #" << i+1 << ": YES" << '\n';
        } else {
          cout << "Case #" << i+1 << ": NO" << '\n';
        }  
      }
    }
  }
 
 
  return 0;
}
