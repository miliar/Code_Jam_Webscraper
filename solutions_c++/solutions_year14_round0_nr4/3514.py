#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <vector>
#include <math.h>
#include <map>
#include <sstream>
#include <numeric>
#include <bitset>
#include <limits.h>
#include <iomanip>
#include <math.h>
#include <string.h>
#include <queue>
#include <set>
using namespace std;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector< pair<int,int> > vii;
typedef long long ll;
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define For(i,a,b) for(int i=a;i<=b;i++)
#define present(c,x) ((c).find(x) != (c).end())      // for set/map
#define cpresent(c,x) (find(all(c),x) != (c).end())  //for vector
#define PI 3.141592658979323433
double EPS = 1e-9;
#define MOD 1000000007

int War(vd& naomi , vd& ken , int n)
{
    int a = 0;
    
    while (n --) {
        
        if (*(naomi.begin()) > *(ken.end() - 1) ) {
            a ++ ;
            naomi.erase(naomi.begin());
            ken.erase(ken.begin());
        }
        else
        {
            
            vd :: iterator up ;
            up = upper_bound(all(ken),*(naomi.begin()));
            naomi.erase(naomi.begin());
            ken.erase(up);
        }
    }
  
    return a ;
}

int DeceitWar(vd& naomi , vd& ken , int n)
{
    int b = 0 ;
    
    while (n -- ) {
        
    
        if(*(naomi.begin()) > *(ken.begin()))
        {
            b ++ ;
            naomi.erase(naomi.begin());
            ken.erase(ken.begin());
            
        }
        else
        {
            naomi.erase(naomi.begin());
            ken.erase(ken.end() - 1);
        }
    
                 }
    return b;
}


int main()
{
    int T;
   
    ifstream infile;
    infile.open("/Users/rachitmadan/Desktop/Xcode Projects/Problems/input.txt");
    infile>>T ;
    int t = 0;
    vector<double> naomi,naomi1 ;
    vector<double> ken,ken1;
    while (T--) {
        
        t ++ ;
        int n ;
        infile>> n;
        For(i, 0, n-1)
        {
            double d;
            infile>>d ;
            naomi.pb(d) ;
        }
        For(i, 0, n-1)
        {
            double d;
            infile >> d;
            ken.pb(d) ;
        }
        sort(all(naomi));
        sort(all(ken));
        naomi1 = naomi;
        ken1 = ken ;
        
       int a = War(naomi1,ken1,n);
       int b = DeceitWar(naomi,ken,n);
        
        cout<<"Case #"<<t<<": "<<b<<" "<<a;
        cout<<endl;
        
    }
    
    return 0;
    
}





