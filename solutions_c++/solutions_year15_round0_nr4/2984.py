#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<map>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int i=0; i<t; i++) {
    string ans="";
    int x, r, c;
    cin >> x >> r >> c;

    if ((x>r && x>c) || (r*c)%x!=0)
      ans = "RICHARD";
    else {
      switch(r) {
      case 1: switch(c) {
	case 1: if(x==1) ans="GABRIEL";
	  else ans="RICHARD";
	  break;
	case 2: if (x==1||x==2) ans = "GABRIEL";
	  else ans = "RICHARD";
	  break;
	case 3: if (x==1||x==2) ans = "GABRIEL";
	  else ans = "RICHARD";
	  break;
	case 4:if (x==1||x==2) ans = "GABRIEL";
	  else ans = "RICHARD";
	  break;
	}
	break;
      case 2: switch(c) {
	case 1:if (x==1||x==2) ans = "GABRIEL";
	  else ans = "RICHARD";
	  break;
	case 2:if (x==1||x==2) ans = "GABRIEL";
	  else ans = "RICHARD";
	  break;
	case 3:if (x==1||x==2 || x==3) ans = "GABRIEL";
	  else ans = "RICHARD";
	  break;
	case 4:if (x==1||x==2) ans = "GABRIEL";
	  else ans = "RICHARD";
	  break;
	}
	break;
      case 3:switch(c) {
	case 1:if (x==1) ans = "GABRIEL";
	  else ans = "RICHARD";
	  break;
	case 2:if (x==1||x==2 || x==3) ans = "GABRIEL";
	  else ans = "RICHARD";
	  break;
	case 3:if (x==1||x==3) ans = "GABRIEL";
	  else ans = "RICHARD";
	  break;
	case 4:if (x==1||x==2 || x==3 || x==4) ans = "GABRIEL";
	  else ans = "RICHARD";
	  break;
	}
	break;
      case 4:switch(c) {
	case 1:if (x==1||x==2) ans = "GABRIEL";
	  else ans = "RICHARD";
	  break;
	case 2:if (x==1||x==2) ans = "GABRIEL";
	  else ans = "RICHARD";
	  break;
	case 3:if (x==1||x==2 || x==3 || x==4) ans = "GABRIEL";
	  else ans = "RICHARD";
	  break;
	case 4:if (x==1||x==2 || x==4) ans = "GABRIEL";
	  else ans = "RICHARD";
	  break;
	}
	break;
      }
    }
    cout << "case #" << i+1 << ": " << ans << endl;
  }
  return 0;
}
