#include <iostream>
using namespace std;


int mat[5][5] =  { {0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
int n;

bool process(string t, int start, int curr)
{
     //if ( curr == 4 && start == n)
       // return true;
     if (curr == 4){
          int val = t[start] - '0';
         int mult = 1;
         int i ;
         for ( i = start+1; i < n; i++) {
             if ( val < 0)
                mult = -1;
             else
                 mult = 1;
                 
             val = mat[abs(val)][t[i] - '0'];
             val *= mult;
            
             }   
            if (val == 4){
                    return true;
            } else {
                   return false;       
            }
             
     }
        
     
     int val = t[start] - '0';
     int mult = 1;
     int i ;
     for ( i = start+1; i < n; i++) {
          if ( val == curr)
            return process(t, i,curr+1);
         if ( val < 0)
            mult = -1;
         else
             mult = 1;
             
         val = mat[abs(val)][t[i] - '0'];
         val *= mult;
        
         }
         return false;
}
     
int main(){    
   freopen("vats.txt", "r", stdin);
    freopen("op.txt", "w", stdout);
    
    int test;
    cin>>test;
    int cc = 1;
    while (test--){
        int l, x;
        string s;
        
        cin>>l>>x;
        cin>>s;
        int temp;
        for ( int i = 0 ; i < s.length(); i++) {
            if (s[i] == 'i')
               s[i] = '2';
            else if ( s[i] == 'j')
                 s[i] = '3';
            else
                s[i] = '4';
                }
            
        string t = "";
        while (x--){
              t += s;
        }
        n = t.size();
        //cout<<t<<"\n";    
        cout<<"Case #"<<cc<<": ";
        cc++;
        cout <<( process(t,0,2) ? "YES" : "NO") << "\n";
    }
    return 0;
}
