#include <iostream>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int t;
int n, r, p , s;


string so(string s) {
    if (s.length() == 1) 
        return s;

    string s1 = s.substr(0, s.length()/2);
    string s2 = s.substr(s.length()/2, s.length()/2);
        
    s1 = so(s1);
    s2 = so(s2);

    if (s1 < s2) 
        return s1 + s2;
    return s2 + s1;   

}
 
        char u[5][20][100000];


int main() {
    cin >> t;

    for (int i = 1; i <= t; i++) {
        cin >> n >> r >> p >> s;
         
               for (int l = 0; l < 3; l++)
        for (int j = 0; j < 16; j++)
            for (int k = 0; k < 10000; k++)
                u[l][j][k] = 'U';
        
        u[0][0][0] = 'R';
        u[1][0][0] = 'S';
        u[2][0][0] = 'P';
        //cout << "foo"<<endl;
        for (int l = 0; l < 3; l++) {
        for (int j = 1; j <= n; j++)
            for (int k=0; k < (1<<(j-1)); k++) {
          //      cout << l << j << k << endl;        
        
                if (u[l][j-1][k] == 'P') {
                    u[l][j][2*k] ='P';
                    u[l][j][2*k+1] = 'R';
                } if (u[l][j-1][k] == 'R') {
                    u[l][j][2*k] ='R';
                    u[l][j][2*k+1] = 'S';
                } if (u[l][j-1][k] == 'S') {
                    u[l][j][2*k] ='P';
                    u[l][j][2*k+1] = 'S';
                }
            }
        }
            //cout << "as"<<endl; 
        for (int l = 0; l < 3; l++) {
            int rr = 0, pp = 0, ss = 0;
            for (int j = 0; j < (1<<(n)); j++)
                if (u[l][n][j] == 'R')      
                    rr++;
                else  if (u[l][n][j] == 'S')      
                    ss++;
                else  if (u[l][n][j] == 'P')      
                    pp++;
            
            if (ss==s && pp==p && rr==r) {
                //bingo
                 cout << "Case #"<<i<<": ";
                
                string s;

                for (int j =0; j < (1<<(n));j++)
                 s += u[l][n][j];
                
               s = so(s);
                
                cout << s<<endl;
                goto end;
            }
                    
        }

        cout << "Case #"<<i<<": IMPOSSIBLE";
               cout << endl;

        end:;
    }

    return 0;
}
