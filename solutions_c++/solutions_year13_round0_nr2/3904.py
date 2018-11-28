#include <iostream>
#include <cstdio>
#include <map>
#include <algorithm>
#include <cstring>  //for C++
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <sstream>
//#include <string> for C

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
#define foreach(itr, cont) for (typeof(cont.begin()) itr = cont.begin(); itr != cont.end(); itr++)

using namespace std;

int a[100][100];

int findMin(int row){
    
}

bool checkPossible(int N, int M){
    int i,j,k;
    
    REP(i,N){
        bool allequal = true;
        int max = a[i][0];
        int colume;
        REP(j,M){
            if(a[i][j]>max){
                max = a[i][j];
                allequal = false;
            }
            else if(a[i][j]<max)
                allequal = false;
        }
        if(!allequal){
            REP(j,M){
                if(a[i][j]!=max){
                    REP(k,N){
                        if(a[k][j]>a[i][j])
                            return false;
                    }
                }
            }
        }
    }
    
    return true;
}

int main()
{
    int T, N, M, i, j, k;
    cin>>T;
    REP(k,T){
        cin>>N>>M;
        REP(i,N){
            REP(j,M){
                cin>>a[i][j];
            }
        }
        cout<<"Case #"<<k+1<<": ";
        if(checkPossible(N,M))
            cout<<"YES";
        else
            cout<<"NO";
        
        cout<<endl;
    }
}
