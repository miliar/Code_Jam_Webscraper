#include<bits/stdc++.h>
using namespace std;

int T;
int L,X;
char xros[4][4] = { { 1,  2,  3,   4 },
		    { 2, -1,  4,  -3 },
		    { 3, -4, -1,   2 },
		    { 4,  3, -2,  -1 } };

int A[21111];
int Ra[21111];
int Rb[21111];
int main(){

  cin >> T;
  for(int ttt=1;ttt<=T;ttt++){
    cin >> L >> X;
    string s="",b;
    cin >> b;

    memset(A,0,sizeof(A));
    memset(Ra,0,sizeof(Ra));
    memset(Rb,0,sizeof(Rb));

    for(int i=0;i<X;i++) s+=b;
    for(int i=0;i<(int)s.size();i++){
      if( s[i] == 'i' ) A[i] = 2;
      if( s[i] == 'j' ) A[i] = 3;
      if( s[i] == 'k' ) A[i] = 4;
    }
    Ra[0] = A[0];
    Rb[L*X] = 1;
    for(int i=1;i<L*X;i++)
      Ra[i] = xros[abs(Ra[i-1])-1][abs(A[i])-1] * (Ra[i-1]<0?-1:1);
    for(int i=L*X-1;i>-1;i--)
      Rb[i] = xros[abs(A[i])-1][abs(Rb[i+1])-1] * (Rb[i+1]<0?-1:1);
    
    bool f = false;
    for(int i=0;i<L*X;i++){
      //      cout << "i = " << i << "  Ra = " << Ra[i] << endl;
      if( Ra[i] == 2 ){
	int np = 1;
	for(int j=i+1;j<L*X;j++){
	  //  cout << "xros [ " << abs(np) -1 << " ] [ " << abs(A[j])-1 << " ] " << endl; 
	  np = xros[abs(np)-1][abs(A[j])-1] * (np<0?-1:1);	
	  // cout << " j = " << j << " np = " << np << endl;
	  if( np == 3 ) {
	    //cout << "Rb = " << Rb[j+1] << endl;
	    if( Rb[j+1] == 4 ) {
	      f = true;
	      break;
	    }
	  }
	}
      }
    }

    cout << "Case #" << ttt << ": " << (f?"YES":"NO") << endl;

    /*
    for(int i=0;i<(int)s.size();i++){
      now = xros[abs(now)-1][abs(A[i])-1] * (now<0?-1:1);
      if( fr == 0 && now == 2 ){
	fr++;
	now = 1;
      }
      if( fr == 1 && now == 3 ){
	fr++;
	now = 1;
      }
    }
    if( fr == 1 ){
      
    }
    */
  }
}
