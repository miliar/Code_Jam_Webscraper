#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <list>
#include <math.h>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define pb(VALUE) push_back(VALUE)
#define pob() pop_back()
#define mp(FST,SEC) make_pair(FST,SEC)
#define len(STR) STR.length()
#define F first
#define S second

#define refresh(ARRAY,TARGET,VALUE) frdn(DEFINED_I,0,TARGET)ARRAY[DEFINED_I]=VALUE
#define watch(VALUE) {cout<<#VALUE;printf("=");cout<<VALUE;printf("\n");}
#define stop exit(0)

using namespace std;


int n,k,ans,t;
char a[10][10];
bool u;

int main(){ 
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
      scanf("%d\n",&t);
       for (int p=0;p<t;p++)
        {   
           k=0;
           u=0;
           ans=0;
           for (int i=0;i<4;i++)
            {
            for (int j=0;j<4;j++)
                {
                     scanf("%c",&a[i][j]);
                     if (a[i][j]=='.') u=1;
                }
            scanf("\n");
            } 
            scanf("\n");           
           
            
           for (int i=0;i<4;i++)
           {
            k=0;
            for (int j=0;j<4;j++)
             {
                if (a[i][j]=='X'||a[i][j]=='T') k++;
             }
            if (k==4) {ans=1;break;}
           }
         if (ans)
                 {
                  cout << "Case #" << p+1 << ": X won"<< endl;
                  continue; 
                 }
         for (int j=0;j<4;j++)
           {
            k=0;
            for (int i=0;i<4;i++)
             {
                if (a[i][j]=='X'||a[i][j]=='T') k++;
             }
            if (k==4) {ans=1;break;}
           }
         if (ans)
                 {
                  cout << "Case #" << p+1 << ": X won"<< endl;
                  continue; 
                 }
         for (int i=0;i<4;i++)
           {
            k=0;
            for (int j=0;j<4;j++)
             {
                if (a[i][j]=='O'||a[i][j]=='T') k++;
             }
            if (k==4) {ans=1;break;}
           }
         if (ans)
                 {
                  cout << "Case #" << p+1 << ": O won"<< endl;
                  continue; 
                 }
         for (int j=0;j<4;j++)
           {
            k=0;
            for (int i=0;i<4;i++)
             {
                if (a[i][j]=='O'||a[i][j]=='T') k++;
             }
            if (k==4) {ans=1;break;}
           }
         if (ans)
                 {
                  cout << "Case #" << p+1 << ": O won"<< endl;
                  continue; 
                 }
         k=0;
         for (int i=0;i<4;i++)
           if (a[i][i]=='X'||a[i][i]=='T') k++;
         if (k==4)
                 {
                  cout << "Case #" << p+1 << ": X won"<< endl;
                  continue; 
                 }
         k=0;
         for (int i=0;i<4;i++)
           if (a[i][i]=='O'||a[i][i]=='T') k++;
         if (k==4)
                 {
                  cout << "Case #" << p+1 << ": O won"<< endl;
                  continue; 
                 }
         k=0;
         for (int i=0;i<4;i++)
           if (a[i][3-i]=='X'||a[i][3-i]=='T') k++;
         if (k==4)
                 {
                  cout << "Case #" << p+1 << ": X won"<< endl;
                  continue; 
                 }
         k=0;
         for (int i=0;i<4;i++)
           if (a[i][3-i]=='O'||a[i][3-i]=='T') k++;
         if (k==4)
                 {
                  cout << "Case #" << p+1 << ": O won"<< endl;
                  continue; 
                 }     
         if  (u) {
                  cout << "Case #" << p+1 << ": Game has not completed" << endl;
                 } else
                 {
                  cout << "Case #" << p+1 << ": Draw" << endl;
                 }
        }        
return 0;
}
