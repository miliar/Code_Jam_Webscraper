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
ifstream in("A-small-attempt0.in");
ofstream out("A-small-attempt0.out");
#endif
void read_case(vector<int> &d){
    int ans,x;
    cin>>ans;
    c(i,1,4) c(j,1,4) {cin>>x;if (i==ans) d.pb(x);}
}
int main(){
    vector<int> a,b;
    int n,k,z;
    cin>>n;
    c(i,1,n){
        a.clear();
        b.clear();
        read_case(a);
        read_case(b);
        sort(all(a));
        sort(all(b));
        k=0;
        c(i,0,3) c(j,0,3) if (a[i]==b[j]) k++,z=a[i];
        cout<<"Case #"<<i<<": ";
        if (k==0) cout<<"Volunteer cheated!";
        else if (k==1) cout<<z;
        else if (k>1) cout<<"Bad magician!";
        cout<<endl;
    }
#if MSVIS
    getch();
#endif
}
