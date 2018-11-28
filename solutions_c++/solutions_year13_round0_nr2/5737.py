#include <cstdlib>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <map>

#define forn(i,n) for(int i = 0; i < (int)n; i++)
#define mymax(a,b) (((a)>(b))?(a):(b))
#define mymin(a,b) (((a)<(b))?(a):(b))

using namespace std;

int t, n, m;
int a[100][100];
int rowmin[100];
int colmin[100];
int rowmax[100];
int colmax[100];

int minrow(int r){
    int mmin = 200;
    forn(j, m) {
        if(a[r][j] < mmin){
            mmin = a[r][j];
        }
    }
    return mmin;
}

int mincol(int c){
    int mmin = 200;
    forn(i, n) {
        if(a[i][c] < mmin){
            mmin = a[i][c];
        }
    }
    return mmin;
}


int maxrow(int r){
    int mmax = 0;
    forn(j, m) {
        if(a[r][j] > mmax){
            mmax = a[r][j];
        }
    }
    return mmax;
}

int maxcol(int c){
    int mmax = 0;
    forn(i, n) {
        if(a[i][c] > mmax){
            mmax = a[i][c];
        }
    }
    return mmax;
}

bool solution(){
    forn(i, n) {
        rowmin[i] = minrow(i);
        rowmax[i] = maxrow(i);
    }
    forn(j, m) {
        colmin[j] = mincol(j);
        colmax[j] = maxcol(j);
    }
    
    forn(i,n) forn(j,m){
        if(a[i][j] < mymin(rowmax[i], colmax[j])){
            return false;
        }
    }
    return true;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
       
    cin>>t;
    forn(_case, t){
        cin>>n>>m;
        
        forn(i, n) forn(j, m) {
            cin>>a[i][j];
        }
        
        printf("Case #%d: ", _case+1);
        if(solution()){
            cout<<"YES";
        } else {
            cout<<"NO";
        }
        cout<<'\n';
    }
    
    return 0;
}