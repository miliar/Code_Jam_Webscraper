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


bool rsort(ll a, ll b){
    return a > b;
}

int main(int argc, char *argv[]) {
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    input.sync_with_stdio(false);
    output.sync_with_stdio(false);
    input.open("/users/jihan/Algorithmic Programming/CodeForces/B261/B261/B261.in.txt");
    output.open("/users/jihan/Algorithmic Programming/CodeForces/B261/B261/B261.out.txt");
    
    ll cases, answer;
    ll n, limx, limy;
    
    input>>cases;
    for (int i=0;i<cases;i++){
        output<<"Case #"<<i+1<<": ";
        input>>n>>limx>>limy;
       /* if (n > limx * limy) output<<"RICHARD\n";
        else if ((limx * limy) % n != 0) output<<"RICHARD\n";
        else if (n > max(limx, limy)) output<<"RICHARD\n";
        else if (n/2 > min(limx, limy)) output<<"RICHARD\n";
        else if (limx == 1 || limy == 1) output<<"GABRIEL\n";
        else if (2 * min(limx, limy) <= n) output<<"RICHARD\n";
        else output<<"GABRIEL\n";*/
        if (n == 1) output<<"GABRIEL\n";
        else if (n == 2){
            if ((limx * limy)%n != 0) output<<"RICHARD\n";
            else output<<"GABRIEL\n";
        }
        else if (n == 3){
            if ((limx * limy)%n != 0 || min(limx, limy) == 1) output<<"RICHARD\n";
            else output<<"GABRIEL\n";
        }
        else if (n == 4){
            if ((limx * limy)%n != 0 || limx * limy < n || min(limx, limy) <= 2) output<<"RICHARD\n";
            else output<<"GABRIEL\n";
        }
        
        
    //    output<<answer<<"\n";
    }
    
    
    
    return 0;
}
