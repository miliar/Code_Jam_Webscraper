#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <ctime>

#define ull unsigned long long

using namespace std;


int dp [100];
int removals [100];
int a, n;
vector<int>sizes;

void init(){
    for(int i = 0;i<100;i++){
        dp[i] = 0;
    }
    for(int i = n;i>=0;i--){
        removals[i] = n - i;
    }
    sizes.clear();

}

void special_case(int _t){


    cout<<"Case #"<<_t+1<<": "<<n<<endl;

}

int main ()
{
    freopen ("A-small.in","r",stdin);
    freopen ("A-small.out","w",stdout);

    int t; cin>>t;
    for (int _t=0;_t<t;_t++){
        cin>>a>>n;

        init();

        sizes.resize(n);
        for(int i = 0;i<n;i++){
            cin>>sizes[i];
        }

        if(a==1){
            special_case(_t);
            continue;
        }
        sort(sizes.begin(),sizes.end());
        int curr = a;
        int moves = 0;
        for(int i = 0;i<n;i++){
            while (true){
                if(curr> sizes[i]){
                    curr+=sizes[i];
                    dp[i] = moves;
                    break;
                }
                moves++;
                curr= curr*2 - 1;


            }

        }

        int answer = 20000000;

        for(int i = 0;i<n;i++){
            answer = min(answer,dp[i] + removals[i+1]);
        }
        answer = min(answer,n);



        cout<<"Case #"<<_t+1<<": "<<answer<<endl;


    }

    return 0;
}

