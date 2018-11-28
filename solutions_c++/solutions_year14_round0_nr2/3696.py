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


int main()
{
    int T;
    cout.precision(8);
    ifstream infile;
    infile.open("/Users/rachitmadan/Desktop/Xcode Projects/Problems/input.txt");
    infile>>T ;
    int t = 0;
    while (T --) {
        t++ ;
 
        double R = 2;
        double C,F,X;
        infile>>C>>F>>X ;
        double Tp = 0 ;
        while (true) {
            if ( X - EPS < C)
            {
                Tp = (X)/R ;
                break ;
                
            }
            else
            {
                Tp += C / R ;
            }
            if((X - C)*(R+F) >= EPS + (X*R))
            {
                 R += F;
                
               
            }
            else
            {
                Tp += (X - C) / R ;
                break ;
            }
            
        }
        
        cout<<"Case #"<<t<<": ";
        cout<<fixed<<setprecision(7)<< Tp << endl ;
        
        
    }
    
    
    
    return 0;
    
}





