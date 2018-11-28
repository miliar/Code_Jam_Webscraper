/*
* abeakkas
* Google CodeJam 2015 - Round 2
* Problem A
* Game after game after game...
*/
#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <utility>

typedef long long int ll;

#define pr pair<ll,ll>
#define vpr vector<pair<ll,ll> >

//DEBUGGING
#define _s cout<<
#define _d <<" "<<
#define _e <<endl;

//(int *)calloc(1000000,sizeof(int));
//(int *)malloc(1000000*sizeof(int));

using namespace std; 
ifstream fin ("A.in");
ofstream fout ("A.out");

char arr[100][100];
int R,C;
int access_check(){
    for(int i=0;i<R;i++) for(int j=0;j<C;j++){
        if(arr[i][j]=='.') continue;
        int n=0;
        for(int ii=0;ii<R;ii++) if(arr[ii][j]!='.') n++;
        for(int jj=0;jj<C;jj++) if(arr[i][jj]!='.') n++;
        if(n==2) return 0;
    }
    return 1;
}

int main(){
    int T;
    fin>>T;
    for(int iT=1;iT<=T;iT++){
        fin>>R>>C;
        char ch;
        for(int i=0;i<R;i++) for(int j=0;j<C;j++){
            fin>>arr[i][j];
        }
        if(access_check()==0){
            fout<<"Case #"<<iT<<": IMPOSSIBLE"<<endl;
            continue;
        }
        int n=0;
        for(int i=0;i<R;i++) for(int j=0;j<C;j++){
            int flag=1;
            switch(arr[i][j]){
                case '.':
                    flag=0;
                    break;
                case '^':
                    for(int ii=i-1;ii>=0;ii--) if(arr[ii][j]!='.') flag=0;
                    break;
                case '>':
                    for(int jj=j+1;jj<C;jj++) if(arr[i][jj]!='.') flag=0;
                    break;
                case '<':
                    for(int jj=j-1;jj>=0;jj--) if(arr[i][jj]!='.') flag=0;
                    break;
                case 'v':
                    for(int ii=i+1;ii<R;ii++) if(arr[ii][j]!='.') flag=0;
                    break;
            }
            n+=flag;
        }
        fout<<"Case #"<<iT<<": "<<n<<endl;
    }
	return 0;
}
