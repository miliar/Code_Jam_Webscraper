#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <cmath>
#define s(a) scanf("%d",&a);
#define s2(a,b) scanf("%d %d",&a,&b);
#define sc(a) cin >> a;
#define sp(b) cout << b << "\n";
#define p(a) printf("%d\n",a);
#define p2(a,b) printf("%d %d",a,b);
#define pm(a) printf("a\n");
#define test(t) while(t>0)
#define sl(a) a.length();
#define f(a,b,c) for(a=b;a<c;a++)
#define v(a,b) vector<a> b;
#define pb(a,b) a.push_back(b);
#define ll long long
#define max(a,b) (abs(a)>abs(b) ? abs(a):abs(b))
#define min(a,b) (abs(a)<abs(b) ? abs(a):abs(b))
#define diff(a,b) abs(a-b);
using namespace std;
ll testing(string s,int length){
    int i,j;
    char current;
    int value=0;
    for(j=length-1;j>=0;j--){
        if(s[j]!='+'){
            break;
        }
    }
    current=s[0];
    for(i=0;i<=j;i++){
        if(s[i]!=current){
            current=s[i];
            value ++;
        }
    }
    if(current=='-'){
        value ++;
    }
    return value;
}
using namespace std;
int main(){
    int t,n,i,j,x,l,count;
    string s;
    ll answer;
    s(x);
    t=x;
    test(t){
        count=0;
        s(n);
        int p=0;
        int array[2*n-1][n];
        vector<int> vec;
        int array2[2501]={0};
        f(i,0,2*n-1){
            f(j,0,n){
                s(array[i][j]);
                array2[array[i][j]]++;
                
            }
        }
         f(i,0,2*n-1){
            f(j,0,n){
                 if(array2[array[i][j]]%2!=0  ){

                    vec.push_back(array[i][j]);
                    p++;
                }
                
            }
        }

        sort(vec.begin(),vec.end());
        unique(vec.begin(),vec.end());


        printf("Case #%d:",x-t+1);
        f(i,0,n){
            printf(" %d",vec[i]);
        }
        printf("\n");
        t--;  
        }
        
    
}
