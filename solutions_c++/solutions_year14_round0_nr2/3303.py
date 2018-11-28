#include <iostream>
#include <ctype.h>
#include <stack>
#include <queue>
#include <limits.h>
#include <fstream>
#include <map>
#include <cmath>
#include <ctime>
#include <cstring>
#include <ctime>
#include <set>

#define rep(i, a) for(int i = 0; i < a; i++)
#define rep1(i, a) for(int i = 1; i <= a; i++)
#define fo(i, a, b) for(int i = a; i < b; i++)
#define defo(i, a, b) for(int i = a; i >= b; i--)
#define ll long long
#define pb push_back
#define mp make_pair
#define sz(a) ((int)(a.size()))
#define x first
#define y second
#define SET(x, a) memset(x, a, sizeof(x));
using namespace std;

int main(){
    FILE *mi;
    mi = fopen("e1.txt","w");
    int test;
    cin>>test;
    int l=0;
    while(test--){
        l++;
        double c,f,x;
        cin>>c>>f>>x;
        int it = 1;
        double m = x/2.0;
        while(1){
            double div = 2.0;
            double d = 0;
            int i;
            for(i=0;i<it;i++){
                d = d + c/div;
                //printf("%7lf\n",c/div);
                div+=f;
            }
            d = d + x/div;
            //printf("%7lf\n",x/div);
            if(d<m){
                m = d;
            }
            else{
                break;
            }
            it++;
        }
        //cout<<"Case #"<<l<<": ";
        fprintf(mi,"Case #%d: ",l);
        fprintf(mi,"%.7lf\n",m);
    }
    return 0;
}
