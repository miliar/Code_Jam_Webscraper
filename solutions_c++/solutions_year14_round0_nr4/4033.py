#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <limits>
#include <cstring>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int t,c,n,i,j;
    double x;
    vector<double> arr1, arr2;
    cin>>t;
    for(c=1;c<=t;c++){
        arr1.clear(); arr2.clear();
        cin>>n;
        for(i=0;i<n;i++){
            cin>>x;
            arr1.push_back(x);
        }
        for(i=0;i<n;i++){
            cin>>x;
            arr2.push_back(x);
        }
        printf("Case #%d: ",c);
        sort(arr1.begin(),arr1.end());
        sort(arr2.begin(),arr2.end());
        
        int warAnswer = 0;
        j = 0;
        for(i=0;i<n;i++)
        {
            int wins = 0;
            for(;j<n;j++){
                if(arr2[j]>arr1[i]){
                    warAnswer+=wins;
                    wins = 0;
                    j++;
                    break;
                }
                wins++;
            }
            warAnswer += wins;
        }
        
        
        int cheatAnswer = 0;
        i = 0;
        for(j=0;j<n;j++)
        {
            for(;i<n;i++){
                if(arr1[i]>arr2[j]){
                    cheatAnswer++;
                    i++;
                    break;
                }
            }
        }
        cout<<cheatAnswer<<" "<<warAnswer<<endl;
        
        
    }
    return 0;
}
