/* In the Name of God */
#include <iostream>
#include <set>
#include <iomanip>
#include <cstring>
#include <algorithm>
#include <string>
#include <fstream>
#include <cmath>
#include <deque>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include<cstdio>
#define lch(r) (2*(r)+1)
#define rch(r) (2*(r)+2) 
#define inf (1<<30)
#define F first
#define S second
#define mod 1000000007
using namespace std;
typedef long long ll;
typedef pair<int ,int > pii;
typedef long double ld;
const int MAXN = 100000+10;
ifstream fin("A-small-attempt0.in");
ofstream fout("ans.out");
int main()
{
   ios_base::sync_with_stdio(false);          
       int t;
    fin>>t;
    
                    for(int tt=1;tt<=t;tt++)
                    {
                        int a,b,arr1[11][11],arr2[11][11];
                        fin>>a;
                        
                        for(int i = 1 ; i <= 4 ; i++)
                            for(int j = 1 ; j <= 4 ; j++) 
                            fin>>arr1[i][j];
                            
                                  fin>>b;
                                  
                        for(int i = 1 ; i <= 4 ; i++)
                            for(int j = 1 ; j <= 4 ; j++) 
                                fin>>arr2[i][j];
                                
                        int ans = 0;
                        int p;
  
                        for(int i = 1 ; i <= 4 ; i++)
                            for(int j = 1 ; j <= 4 ; j++) if(arr1[a][i] == arr2[b][j]) ans++,p = arr1[a][i];
                            
                        if(ans == 1) fout<<"Case #"<<tt<<": "<<p<<endl;
                        if(ans == 0) fout<<"Case #"<<tt<<": "<<"Volunteer cheated!"<<endl;
                        if(ans >1) fout<<"Case #"<<tt<<": "<<"Bad magician!"<<endl;
                       
                    }
                
}
