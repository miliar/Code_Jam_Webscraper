//
//  main.cpp
//  Codejam
//
//  Created by Sorawit Paiboonrattanakorn on 4/13/56 BE.
//  Copyright (c) 2556 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <string>
#define n 4

using namespace std;

int main ()
{
    int T,t,i,j;
    string a[5];
    cin >> T;
    for(t=1;t<=T;t++){
        cout << "Case #" << t << ": " ;
        for(i=0;i<n;i++){
            cin >> a[i] ;
            if(a[i]=="") i--;
        }
        /*
        cout << a[0] << endl;
        cout << a[1] << endl;
        cout << a[2] << endl;
        cout << a[3] << endl;
         */
        bool b = false;
        int x,o,d,tt;
        int xx,oo;
        x = o = d = tt = 0;
        for(i=0;i<n;i++){
            xx = oo = 0;
            for(j=0;j<n;j++){
                if(a[i][j]=='X'){ x++; xx++; }
                else if(a[i][j]=='O'){ o++; oo++; }
                else if(a[i][j]=='.'){ d++; }
                else if(a[i][j] == 'T'){ tt++; xx++; oo++; }
            }
            if(xx==4){ b = true; cout << "X won" << endl; break;}
            if(oo==4){ b = true; cout << "O won" << endl; break;}
        }
        if(b) continue;
        for(j=0;j<n;j++){
            xx = oo = 0;
            for(i=0;i<n;i++){
                if(a[i][j]=='X'){ xx++; }
                else if(a[i][j]=='O'){ oo++; }
                else if(a[i][j] == 'T'){ xx++; oo++; }
            }
            if(xx==4){ b = true; cout << "X won" << endl; break;}
            if(oo==4){ b = true; cout << "O won" << endl; break;}
        }
        if(b) continue;
        xx = oo = 0;
        for(i=0;i<n;i++){
            if(a[i][i]=='X'){ xx++; }
            else if(a[i][i]=='O'){ oo++; }
            else if(a[i][i] == 'T'){ xx++; oo++; }
        }
        if(xx==4){ cout << "X won" << endl; continue;}
        if(oo==4){ cout << "O won" << endl; continue;}
        
        xx = oo = 0;
        for(i=0;i<n;i++){
            if(a[n-i-1][i]=='X'){ xx++; }
            else if(a[n-i-1][i]=='O'){ oo++; }
            else if(a[n-i-1][i] == 'T'){ xx++; oo++; }
        }
        if(xx==4){ cout << "X won" << endl; continue;}
        if(oo==4){ cout << "O won" << endl; continue;}
     //cout << x << " " << o << endl;
        if(d==0){
            if(x>o && tt) o++;
            else if(o>x && tt) x++;
            if(x>o) cout << "X won" << endl;
            else if(o>x) cout << "O won" << endl;
            else cout << "Draw" << endl;
            continue;
        }
        else cout << "Game has not completed" << endl;
    }
    return 0;
}

