#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;

int main(){
  int T;
  cin>>T;
  for (int i=0;i<T;i++){
    int A,B;
    int sum=0;
    cin>>A>>B;
    for (int k=A;k<=B;k++){
      ostringstream ostr;
      ostr<<k;
      string s = ostr.str();
      int len = s.size();
      bool flag1=true;
      bool flag2=true;
      for (int j=0; j!=len/2; j++){
	if (flag1){
	  if (s[j]!=s[len-j-1]){
	    flag1 = false;
	  }
	  else{break;}
	}
      }
	if (flag1){
	  int sqt = sqrt(k);
	  if (sqt*sqt == k){
	    ostringstream ostr1;
	    ostr1<<sqt;
	    string s1 = ostr1.str();
	    int len1 = s1.size();
	    for (int j=0; j!=len1/2; j++){
	      if (flag2){
		if (s1[j]!=s1[len1-j-1]){
		  flag2 = false;
		}
		else{break;}
	      }
	    }
	  }
	  else{ flag2 = false;}
	}
      if (flag1&&flag2){ sum++;}
    }
    cout<<"Case #"<<i+1<<": "<<sum<<endl;
  }
}
	
