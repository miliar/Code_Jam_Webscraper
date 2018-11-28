#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
bool digit[11];
bool makeD(int answer) {
   while(1) {
      digit[answer%10] = true;
      answer/= 10;
      if (answer == 0)
         break;
   }
}
bool checkD() {
   for(int i = 0; i < 10; i++){
      if(!digit[i])
         return false;
   }
   return true;
}
int main() {
   int T, N, c, answer;
   cin>> T;
   int cnt = 1;
   bool flag;
   while (T--) {
      cin >> N;
      memset(digit, false, sizeof(digit));
      c = answer = 0;
      flag = false;
      while(1) {
         c++;

         if (c == 101)
            break;
         answer += N;
         makeD(answer);
         if (checkD()) {
            flag = true;
            break;
         }
      }
      if (flag)
         cout << "Case #"<< cnt++ <<": "<< answer<<endl;
      else
         cout << "Case #"<< cnt++ <<": INSOMNIA"<<endl;
   }
   return 0;
}
