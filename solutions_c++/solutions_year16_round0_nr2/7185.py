#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <numeric>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
#include <cassert>
#include <iostream>
#include <fstream>
#define MOD 1000000007
#define pi 3.141592653589
#define ii pair<int,int>
#define vii vector<ii>
#define ll  long long int
#define REP(i,a,b) for(ll i=a;i<=b;i++)
#define loop(i,n) for(ll i=0;i<n;i++)
#define ll  long long int
#define loop2(i,n) for(ll i=1;i<=n;i++)
#define MIN(a,b) (a) < (b) ? (a) : (b)
#define MAX(a,b) (a) > (b) ? (a) : (b)
#define ABS(a) (a) > 0 ? (a) : -(a)
using namespace std;

bool check1(char array1[],ll y)
{
    loop(i,y){
        if(array1[i]=='-'){
            return false;
        }
    }
    return true;
}


bool check2(char array1[], ll y)
{
    loop(j, y){
        if(array1[j]=='+'){
            return false;
        }
    }
    return true;
}


int main()
{
    
    ofstream fout("/Users/ashish/Desktop/A-large-practice.out.txt");
    ifstream fin ("/Users/ashish/Desktop/B-large.in.txt");
    
    ll t;
    fin>>t;
    loop2(j, t){
        char array[101];
        fin>>array;
        ll y  =strlen(array);
        if(check1(array, y)==true){
            fout<<"Case #"<<j<<": "<<"0"<<endl;;
        }
        else if (check2(array, y)==true){
            fout<<"Case #"<<j<<": "<<"1"<<endl;
        }
        else{
            ll ans =  0;
            ll ans2  = 0;
            //ans2 for inversions
            // Two cases to be formed here
            
            // First Case
            if(array[0]=='-'){
                ans++;
                
                for(ll j=1;j<y;j++){
                    if(array[j]=='-'&&array[j-1]=='+'){
                        ans2++;
                    }
                }
            
                
                
                
                
            }
            // Second Case
            
            else{
                
                for(ll j=1;j<y;j++){
                    if(array[j]=='-'&&array[j-1]=='+'){
                        ans2++;
                    }
                }
                
                
                
            }
            
            
            
            
            fout<<"Case #"<<j<<": "<<2*ans2+ans<<endl;
        }
    }
    
    
            return 0;
}