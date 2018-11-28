#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
using namespace std;
#define VISITED 2
#define EXPLORED 1
#define UN_VISISTED 0

typedef unsigned long long ull;
typedef unsigned long ul;
typedef vector<long> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

int main(){
    freopen("in.txt","rt",stdin);
    freopen("out.txt","wt",stdout);
    int T,tcase=1;
    cin>>T;
    while(T--){
       int X,R,C;
       cin>>X>>R>>C;
        printf("Case #%d: ",tcase++);
       if( ((X-1) > R || (X-1)>C)|| (( R*C % X )!=0)){
        cout<<"RICHARD"<<endl;
       }else {
        cout<<"GABRIEL"<<endl;
       }
    }
    return 0;
}