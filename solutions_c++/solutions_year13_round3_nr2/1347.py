#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<map>
#define max(a,b) {a>b?a:b}
#define min(a,b) {a>b?b:a}
using namespace std;


int main()
{int t,test=1;
cin>>t;
while(t--)
{       int x,y;
        cin>>x>>y;
        cout<<"Case #"<<test++<<": ";
        if(x<0 && y>0){
            x=abs(x);
            while(x--){
                cout<<"EW";
            }
            while(y--){
                cout<<"SN";
            }
        }
        else if(x<0 && y<0){
            x=abs(x);
            while(x--){
                cout<<"EW";
            }
            y=abs(y);
            while(y--){
                cout<<"NS";
            }
        }
        else if(x>0 && y<0){
            while(x--){
                cout<<"WE";
            }
            y=abs(y);
            while(y--){
                cout<<"NS";
            }
        }
        else{
            while(x--){
                cout<<"WE";
            }
            while(y--){
                cout<<"SN";
            }
        }
      cout<<"\n"; 
     }
//getch();
return 0;
}
