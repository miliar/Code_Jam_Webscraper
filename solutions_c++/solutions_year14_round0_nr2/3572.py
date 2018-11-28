//
#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <iomanip>
#include <iterator>
#include <climits>
//#include <conio.h>
#include <cstring>
using namespace std;
#define c(i,s,f) for(int i=s;i<=f;i++)
#define cr(i,s,f) for(int i=s;i>=f;i--)
#define pb push_back
#define mp make_pair
#define all(c) c.begin(),c.end()
#define FILEIN 0
#define MSVIS 0
#define SQR(x) ((x)*(x))
typedef unsigned long long int ull;
typedef long long int ll;
typedef long double ld;
const ld eps=1e-9;
const int inf=LONG_MAX;
struct pt {int x,y;};
#if FILEIN
ifstream in("B-large.in");
ofstream out("B-large.out");
#endif
int n,k;
ld c,f,x,globalbest,mej,localbest;
ld cnt(ld BIG,ld NUM){
    return BIG/(2+(NUM)*f);
}
int main(){
    cin>>n;
    c(i,1,n){
        cin>>c>>f>>x;
        k=0;
        globalbest=x/2.0;
        mej=0;
        while(1){
            localbest=cnt(x,k+1)+mej+cnt(c,k);
            if (localbest<globalbest){
                mej+=cnt(c,k);
                k++;
                globalbest=localbest;
            }else break;
        }
        cout<<setprecision(15)<<"Case #"<<i<<": "<<globalbest<<endl;
    }
#if MSVIS
    getch();
#endif
}
