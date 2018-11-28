#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main() {
  int T;
  cin>>T;
  for (int t=1;t<=T;t++){
    int R,C;
    cin>>R>>C;
    vector<string> M(R);
    string in;
    for (int i=0;i<R;i++){
      cin>>M[i];
    }
    int changed=0;
    for (int i=0;i<R;i++) {
      for (int j=0;j<C;j++){
	int ok=0;
	if (M[i][j]!='.') {
	  switch(M[i][j]) {
	  case '<':
	    for (int k=0;k<j;k++) {
	      if (M[i][k]!='.') {
		ok = 1;
		break;
	      }
	    }
	    break;
	  case '>':
	    for (int k=j+1;k<C;k++) {
	      if (M[i][k]!='.') {
		ok = 1;
		break;
	      }
	    }
	    break;
	  case '^':
	    for (int k=0;k<i;k++) {
	      if (M[k][j]!='.') {
		ok = 1;
		break;
	      }
	    }
	    break;
	  case 'v':
	    for (int k=i+1;k<R;k++) {
	      if (M[k][j]!='.') {
		ok = 1;
		break;
	      }
	    }
	    break;
	  }
	  if (!ok) {
	    changed++;
	    for (int k=0;k<R;k++) {
	      if (k!=i) {
		if (M[k][j]!='.') {
		  ok=1;
		  break;
		}
	      }
	    }
	    if (!ok) {
	      for (int k=0;k<C;k++) {
		if (k!=j) {
		  if (M[i][k]!='.') {
		    ok=1;
		    break;
		  }
		}
	      }
	    }
	  }
	  if (!ok) {
	    changed=-1000000000;
	  }
	}
      }
      if (changed<0) break;
    }
    if (changed<0) {
      cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
    } else {
      cout<<"Case #"<<t<<": "<<changed<<endl;
    }
  }
}
