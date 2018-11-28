#include <iostream>
#include <math.h>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string.h>
#include <fstream>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <tuple>
#include <iomanip>
#define ull unsigned long long
#define ll long long
#define inf 1000000000000
#define bil 1000000000

using namespace std;

ifstream input;
ofstream output;



int main(int argc, char *argv[]) {
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    input.sync_with_stdio(false);
    output.sync_with_stdio(false);
    input.open("/users/jihan/Algorithmic Programming/CodeForces/B261/B261/B261.in.txt");
    output.open("/users/jihan/Algorithmic Programming/CodeForces/B261/B261/B261.out.txt");
    ll cases;
    ll x, y, n, hold1, hold2;
    ll ans1, ans2;
    
    
    input>>cases;
    for (int c=0;c<cases;c++){
        output<<"Case #"<<c+1<<": ";
        input>>x>>y>>n;
        ans1 = ans2 = hold1 = hold2 = 0;
        if (min(x, y) == 1){
            //c1
            hold2 += (max(x, y)) / 2;
            hold1 += max(x, y)-hold2;
            
            if (hold2 < n){
                if (max(x, y) % 2 == 1){
                    hold2 += 1;
                    ans2 += 1;
                    if (hold2 < n){
                        ans2 += 1;
                        hold2+=1;
                    }
                    if (hold2 < n){
                        ans2 += (n-hold2) * 2;
                    }
                }
                else{
                    hold2+=1;
                    ans2+=1;
                    if (hold2 < n){
                        ans2 += (n-hold2)*2;
                    }
                }
            }
            if (hold1 < n){
                if (max(x, y) % 2 == 1){
                    ans1 += (n-hold1) * 2;
                }
                else{
                    hold1+=1;
                    ans1+=1;
                    if (hold1 < n){
                        ans1 += (n-hold1) * 2;
                    }
                }
            }
            
            
            
            
            
        }
        else if (min(x, y) == 2){
            ans2 = inf;
            hold1 = (x * y) / 2;
            if (hold1 < n){
                hold1 += 1;
                ans1 += 2;
                if (hold1 < n){
                    hold1 += 1;
                    ans1 += 2;
                }
            }
            
            if (hold1 < n){
                ans1 += (n-hold1) * 3;
            }
        }
        else{
            if (x % 2 == 1 && y % 2 == 1){
                hold1 = (x*y)/2;
                hold1++;
            }
            else{
                hold1 = (x*y)/2;
            }
            hold2 = (x*y) - hold1;
            
            ll corners=0,edges=0;
            
            
            if (hold1 < n){
                if (x % 2 == 0 && y % 2 == 0){
                    corners = 2;
                    edges += 2*((x/2)-1);
                    edges += 2*((y/2)-1);
                }
                else if (x % 2 == 0){ //y%2==1
                    corners += 2;
                    edges += ((y/2)-1)+(y/2);
                    edges += 2*((x/2)-1);
                }
                else if (x % 2 == 1 && y%2 == 0){ //x%2 == 1
                    corners = 2;
                    edges += 2*((y/2)-1);
                    edges += ((x/2)-1)+(x/2);
                }
                else{
                    corners = 0;
                    edges += 2*((x/2));
                    edges += 2*((y/2));
                }
                for (int i=0;i<corners && hold1<n;i++){
                    hold1++;
                    ans1 += 2;
                }
                for (int i=0;i<edges && hold1<n;i++){
                    hold1++;
                    ans1 += 3;
                }
                if (hold1 < n){
                    ans1 += (n-hold1) * 4;
                }
            }
            corners = edges = 0;
            if (hold2 < n){
                if (x % 2 == 0 && y % 2 == 0){
                    corners += 2;
                    edges += 2*((x/2)-1);
                    edges += 2*((y/2)-1);
                }
                else if (x % 2 == 0){
                    corners = 2;
                    edges += ((y/2)-1)+(y/2);
                    edges += 2*((x/2)-1);
                }
                else if (x % 2 == 1 && y%2==0){
                    corners = 2;
                    edges += ((x/2)-1)+(x/2);
                    edges += 2*((y/2)-1);
                }
                else{
                    corners = 4;
                    edges += 2*((x/2)-1);
                    edges += 2*((y/2)-1);
                }
                for (int i=0;i<corners && hold2<n;i++){
                    hold2++;
                    ans2 += 2;
                }
                for (int i=0;i<edges && hold2<n;i++){
                    hold2++;
                    ans2 += 3;
                }
                if (hold2 < n){
                    ans2 += (n-hold2) * 4;
                }
            }
        }
        output<<min(ans1, ans2)<<"\n";
    }
    
    
    return 0;
}
