#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <fstream>
#include <stack>
#include <algorithm>
#include <stdio.h>

using namespace std;

#define forn(i,n) for(int i=0;i<(n);i++ )
#define forsn(i,s,n) for(int i=s;i<(n);i++ )

    

string solve(string s, int last){
   if(last < 0) return "";
   if(last == 0) {
//           cout<<"entro "<<""+s[0]<<endl;
           return s.substr(0,1);
}
   char mx = s[last];
   int idx = last;
   //if(mx == 'Z') return 'Z'+solve(s,last-1);
   for(int i=last;i>=0;i--){
       if(s[i] > mx){
           mx = s[i];
           idx = i;            
       }        
   }
  // cout<< mx <<" "<< solve(s, idx-1) <<" "<< s.substr(idx+1,last-idx)<< " " <<last <<" " << idx<<endl;
   return mx + solve(s, idx-1) + s.substr(idx+1,last-idx);                  
}

int main(){
    freopen("a.in", "a+",stdin);
    freopen("a.out", "w+",stdout);
    

    
    int cases;
    cin >> cases;
   
    for(int i=0;i<cases;i++){
        
        string str;
        cin >> str;
        
        int last = str.length()-1;
        
 
        string sol = solve(str,str.length()-1);
     
        cout << "Case #" << (i+1)<<": "<<sol<<endl;                            
    } 
    
    
    
}
