#include <iostream>
#include <stdio.h>
#include <vector>
#include <set>
#include <algorithm>

//#include <conio.h>

#define HOME
#define max (a>b)?a:b
#define pb push_back
#define min (a<b)?a:b
#define ll long long int
using namespace std;

ll gcd(ll u, ll v) {
return (v != 0)?gcd(v, u%v):u;
}
   
int main(){
    
    #ifdef HOME
	 	freopen("in.txt", "r", stdin);
   	freopen("output.txt", "w", stdout);
    #else
	//freopen(".in", "r", stdin);
	//freopen(".out", "w", stdout);
   #endif
   int t;
   scanf("%d",&t);
   
   for(int i = 0; i<t ; ++i){
           
           ll a,b;
           
           char c;
           cin >> a >> c >> b;
           
           ll g = gcd(a,b);
           a = a/g;
           b= b/g;
          ll temp = b;
          int flag = 1;
          while(temp>1){
                     if(temp%2 != 0)
                     {
                              // cout << temp << endl;
                            flag  = 0;
                            break;
                     }
                     temp = temp / 2;
           }
           int score = 0;  
           while(flag && a < b)
           {
                   a = a*2;
                   score ++;
                   }
                   cout << "Case #" << (i+1) << ": ";
            if(flag)
            cout << score << endl;
            else
            cout << "impossible" << endl;  
            }     
   
    //getchar();
    return 0;
    }
