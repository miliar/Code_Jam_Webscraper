#include<iostream>

using namespace std;

char A[10] = {'0','1','2','3','4','5','6','7','8','9'};

int Conv(char c){
   for(int i = 0; i < 10; i++){
      if(c == A[i])
	 return i;
   }
   return -1;
}

int main(){
   int T;
   cin >> T;
   int c = 1;
   while(T--){
      int Smax;
      cin >> Smax;
      int have = 0;
      int need =0;
      for(int i = 0; i <= Smax; i++){
	 char c;
	 cin >> c;
	 int v = Conv(c);
	 if(v > 0 and i > have){
	    need += i-have;
	    have = i;
	 }
	 have += v;
      }
      cout << "Case #" << c++ << ": " << need << endl;
   }
   return 0;
}
