#include <fstream>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

bool isPalindrome(string s){
     string c = s;
     reverse(s.begin(), s.end());
     if(c==s){
              return true;
     }
     return false;
}

int main(){
       ifstream cin("in.txt");
       ofstream cout("out.txt");
       int arr2[10001];
       bool arr[10001];
       memset(arr,false,sizeof(arr));
       memset(arr2,0,sizeof(arr));
       bool b= true;
       int cont = 0;
       for(int i = 1; i < 10001; i++){
               if(b){
                   stringstream ss;
                   string s1, s2;
                   int p = pow((double)i,2);
                   if(p > 10000){
                        b=false;
                   }
                   ss << i;
                   s1 = ss.str();
                   stringstream ss2;
                   ss2 << p;
                   s2 = ss2.str();
                   if(isPalindrome(s1) && isPalindrome(s2) && b){
                                 arr[p] = true; 
                   }
               }
               if(arr[i]){
                          cont++;
               }
               arr2[i]=cont;       
       }
       int n;
       cin >> n;
       for(int i = 0; i < n; i++){
               int a, b;
               cin >> a >> b;
               cout << "Case #" << i+1 << ": " << (arr2[b] - arr2[a-1]) << endl;
       }
}
