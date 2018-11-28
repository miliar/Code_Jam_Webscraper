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
double EPS = 1e-6;
#define MOD 1000000007

void intersect(int a[] , int b [], int t)
{
    int val = -1 , num = 0;
    For(i, 0, 3)
     For(j, 0, 3)
    {
        if(a[i] == b[j])
        {
            num++;
            val = a[i] ;
        }
    }
    if(num == 1)
        printf("Case #%d: %d",t,val);
    if(num > 1)
        printf("Case #%d: Bad magician!",t);
    if(num == 0)
        printf("Case #%d: Volunteer cheated!",t);
    cout<<endl;
    
}

int main()
{
    int T;
    ifstream infile;
    infile.open("/Users/rachitmadan/Desktop/Xcode Projects/Problems/input.txt");
    infile>>T ;
    int t = 0;
    int grid[4][4];
    while (T--) {
        
        t ++ ;
        int a ,b ;
        int set_a[4], set_b[4] ;
        
        infile>>a ;;
        For(i, 0, 3)
        For(j, 0, 3)
        {
            infile>> grid[i][j] ;
        }
        For(j, 0, 3)
        set_a[j] = (grid[a -1][j]);
        
        infile>>b ;;
        For(i, 0, 3)
        For(j, 0, 3)
        {
            infile>> grid[i][j] ;
        }
        For(j, 0, 3)
        set_b[j] = (grid[b -1][j]);
        intersect(set_a,set_b,t);
    }
    
    
    return 0;
    
}





