#include<iostream>
#include<cmath>
#include<sstream>
using namespace std;
string itos(int);
bool palindrome(string);
int main(void)
{
   int i,j,sqrti;
   int T,A,B,count;
   bool table[1001];
   string s;
   for(i=1;i<=1000;i++){
      sqrti=(int)sqrt((double)i);
      if(i==sqrti*sqrti){
         s=itos(i);
         if(palindrome(s)){
            s=itos(sqrti);
            if(palindrome(s))
               table[i]=true;
            else
               table[i]=false;
         }
         else
            table[i]=false;
      }
      else
         table[i]=false;
   }
   cin >> T;
   for(i=1;i<=T;i++){
      cin >> A >> B;
      count=0;
      for(j=A;j<=B;j++){
         if(table[j])
            count++;
      }
      cout << "Case #" << i << ": " << count << endl;
   }
   return 0;
}
string itos(int i)
{
   stringstream ss("");
   string s;
   ss << i;
   ss >> s;
   return s;
}
bool palindrome(string s)
{
   int L=s.length();
   for(int i=0;i<L/2;i++){
      if(s[i]!=s[L-i-1])
         return 0;
   }
   return 1;
}
