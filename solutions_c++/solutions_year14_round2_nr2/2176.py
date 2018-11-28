#include <iostream>

using namespace std;

int main(int argc, char **argv) {
    unsigned int T, A, B, K, a, b, k;
    double y;
    cin>>T;
    for(int c=1; c<=T; c++) {
      cin>>A>>B>>K;
      y=0;
      for(k=0; k<K; k++) {
	for(a=0; a<A; a++) {
	  for(b=0; b<B; b++) {
	    if( k == (a&b) )
	      y++;
	  }
	}
      }
      cout<<"Case #"<<c<<": "<<y<<endl;
    }
    return 0;
}
