#include<iostream>
#include<stdio.h>
#include<map>
#include<queue>
#include<string>
using namespace std;

string flip(string s, int len) {
     int l, r;
     
     l = 0; 
     r = len - 1;
     while (r > l) {
        char temp = s[l];
        s[l] = s[r];
        s[r] = temp;
        l++;
        r--;         
     }      
     
     for (int i = 0; i < len; i++) {
        if (s[i] == '-')
           s[i] = '+';
        else
           s[i] = '-';  
     }   
     return s;
}

int solveSmall(string S) {
     string G = "";
     for (int i = 0; i < S.length(); i++)
         G = G + "+";
     
     queue<string> Q;
     map<string, int> dist;
     
     dist[S] = 0;
     Q.push(S);
     
     while (!Q.empty()) {
        string u = Q.front(); Q.pop();
        
        for (int f = 0; f < u.length(); f++) {
            string v = flip(u, f + 1);
            
            if (dist.find(v) == dist.end()) {
               dist[v] = dist[u] + 1;
               Q.push(v);                 
            }
        }         
     }
     
     return dist[G];
}

int solveLarge(string S) {
    
     int ans = 0;
     while (true) {
           
        int i = 0;
        while (S[i] == '+')
           i++;
        
        if (i == S.length())
           break;
           
        if (i > 0) {
           ans++;   
           S = flip(S, i);   
        }         
        
        i = S.length() - 1;
        while (S[i] == '+') 
           i--;
           
        ans++;
        S = flip(S, i + 1);   
     }
     return ans;
}

int main(void)
{
     freopen("B-large.in","r",stdin);
     freopen("B-large.out","w",stdout);
     
     int T;
     string S;
     
     cin >> T;
     for (int cases = 1; cases <= T; cases++) {
         cin >> S;  
         
         cout << "Case #" << cases << ": " << solveLarge(S) << endl;
     } 
}
