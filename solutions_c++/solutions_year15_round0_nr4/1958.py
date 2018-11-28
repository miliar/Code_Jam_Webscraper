#include <iostream>
#include <cstdio>

using namespace std;

#define iFor(i,n) for(int i=0;i<=n;i++)
#define iFor2(i,n,m) for(int i=n;i<=m;i++)
#define iForDec(i,n,m) for(int i=n;i>m;i--)

int N;
//string s;
#define SMALL
//#define LARGE

int main(){
    freopen("a.txt","rt",stdin);
#ifdef SMALL
	freopen("D-small-attempt1.in","rt",stdin);
	freopen("D-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("B-large-practice.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif
    cin>>N;
    int X,R,C;
    iFor2(i,1,N){
        printf("Case #%d: ",i);
        cin>>X>>R>>C;
        switch(X){
        case 1:
            cout<<"GABRIEL\n";
        break;
        case 2:
            if(R*C==1 || R*C==3 || R*C==9){
                cout<<"RICHARD\n";

            }else{
                cout<<"GABRIEL\n";
            }
            break;
        case 3:
            if(R*C==6 || R*C==9 || R*C==12){
                cout<<"GABRIEL\n";
            }else{
                cout<<"RICHARD\n";
            }
            break;
        case 4:
            if(R*C==16 || R*C==12){
                cout<<"GABRIEL\n";
            }else{
                cout<<"RICHARD\n";
            }
            break;
        }
    }
    return 0;
}
