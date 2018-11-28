#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<utility>
#define MP make_pair
using namespace std;
typedef long long ll ;
const int MAX = 105;
int ma[MAX][MAX];
int n,m;
bool major(int x , int y){
     bool up = 0,rg = 0;
     for(int i = 0 ; i < n ;i++)
             if( ma[i][y] > ma[x][y] )
                 up = true;
     for(int j = 0 ; j < m ;j++)
             if( ma[x][j] > ma[x][y] )
                 rg = true;
     return up & rg;
}
int main(){
    freopen("input", "r", stdin);
    freopen("output" ,"w",stdout);
    int t, test = 1;; 
    cin>>t ; 
    while( t -- ){
           cin >> n>>m ;
           for(int i = 0 ; i < n ;i++)
                   for(int j = 0 ; j < m ; j++)
                           cin>>ma[i][j];
           bool ans = true;
           for(int i = 0 ; i < n ; i++)
                   for(int j = 0 ; j <m ; j++)
                           if(major(i,j))
                              ans = false;
           if( ans )
               printf("Case #%d: YES\n",test);
           else
               printf("Case #%d: NO\n",test);
           test++;       
    }
    return 0 ;     
}
