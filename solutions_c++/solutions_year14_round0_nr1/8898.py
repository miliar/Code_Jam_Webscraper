/* 
 * File:   main.cpp
 * Author: bkak
 *
 * Created on April 12, 2014, 1:14 PM
 */


#include <cstdlib>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <limits.h>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>
#include <sstream>
#include <climits>
#include <cmath>
#include <math.h>
#include <vector>
#include <ctime>
using namespace std;

int docalc(int a, int b, int c, int d, int e, int f, int g, int h){
    int match =0;
    int num;
    int i;
    if (a==e){match++;}
    if (a==f){match++;}
    if (a==g){match++;}
    if (a==h){match++;}
    
    if (b==e){match++;}
    if (b==f){match++;}
    if (b==g){match++;}
    if (b==h){match++;}
    
    if (c==e){match++;}
    if (c==f){match++;}
    if (c==g){match++;}
    if (c==h){match++;}
    
    if (d==e){match++;}
    if (d==f){match++;}
    if (d==g){match++;}
    if (d==h){match++;}
    
    return match;
    
}
int docalc2(int a, int b, int c, int d, int e, int f, int g, int h){
   
    int match =0;
    int num;
    int i;
    if (a==e){match=a;}
    if (a==f){match=a;}
    if (a==g){match=a;}
    if (a==h){match=a;}
    
    if (b==e){match=b;}
    if (b==f){match=b;}
    if (b==g){match=b;}
    if (b==h){match=b;}
    
    if (c==e){match=c;}
    if (c==f){match=c;}
    if (c==g){match=c;}
    if (c==h){match=c;}
    
    if (d==e){match=d;}
    if (d==f){match=d;}
    if (d==g){match=d;}
    if (d==h){match=d;}
    
    return match;
    
}

int main(){
    
   
    string tmp;
    int i=0;
    int j=0;
    int a,b,c,d;
    int e,f,g,h;
    int w,x,y,z;
    
    
    getline(cin,tmp);
    int size = atoi(tmp.c_str());
    
    int row;
    int ans;
    int mat;
    
    while (i<size){
        cin >> row;
        
        while (j<row){
                cin >> a >> b >> c >> d;
                j++;
        }
        while (j<4){
            cin >> w >> x >> y >> z ;
            j++;
        }
        j=0;
        cin >> row;
        while (j<row){
                cin >> e >> f >> g >> h;
                j++;
        }
        while (j<4){
            cin >> w >> x >> y >>z;
            j++;
        }
        j=0;
        //cout << a << b << c << d << e << f << g << h;
        ans = docalc(a,b,c,d,e,f,g,h);
        
        i++;
        
        if (ans == 0){
            cout << "Case #" << i << ": Volunteer cheated!\n";
        } else if (ans == 1){
            mat = docalc2(a,b,c,d,e,f,g,h);
            cout << "Case #" << i << ": " << mat << "\n";
        } else {
            cout << "Case #" << i << ": Bad magician!\n";
        }
        
    }
    
    
     return 0;
}
