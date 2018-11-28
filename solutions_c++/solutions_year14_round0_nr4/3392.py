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
ifstream in("D-large.in");
ofstream out("D-large.out");
#endif
vector<ld> naomi,ken;
set<ld> ken_set;
ld x,y;
int n,k,war1,war2,lken,rken;
int main(){
    cin>>n;
    c(i,1,n){
        war2=0;war1=0;
        cin>>k;
        naomi.clear();
        ken.clear();
        ken_set.clear();
        c(i,1,k) {cin>>x;naomi.pb(x);}
        c(i,1,k) {cin>>x;ken.pb(x);ken_set.insert(x);}
        sort(all(naomi));
        sort(all(ken));
        c(i,0,k-1){
            set<ld>::iterator t=ken_set.upper_bound(naomi[i]);
            if (t==ken_set.end()){
                war1=k-i;
                break;
            }else ken_set.erase(t);
        }
        lken=0;rken=k-1;
        c(i,0,k-1){
            if (naomi[i]<ken[lken]) rken--;
            else{
                war2++;
                lken++;
            }
        }
        cout<<"Case #"<<i<<": "<<war2<<" "<<war1<<endl;
    }
#if MSVIS
    getch();
#endif
}
