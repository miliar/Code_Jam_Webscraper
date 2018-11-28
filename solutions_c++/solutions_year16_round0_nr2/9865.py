
 #include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>
using namespace std;

int main(){
  freopen("./b2.in.txt", "r", stdin);
  freopen("./b2.out.txt", "w", stdout);
    int N; 
    cin >> N;
    for(int i = 0; i < N; i++){
    string str; 
    cin >> str; 
   int count = 1; 
   for(int i =0;  i < str.length()-1; i++){
       if(str[i]==str[i+1])continue; 
       else count++; 
   }
   if(str[str.length()-1] == '+') count--; 
    printf("Case #%d: %d\n", i+1, count); 
    }
    
    
}