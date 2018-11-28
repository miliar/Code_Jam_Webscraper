#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>

using namespace std;

#define LL long long
#define LD long double
#define ULL unsigned long long

#define Min(a,b) a=min(a,b)
#define Max(a,b) a=max(a,b)
#define Sz(s) int((s).size())
#define All(s) (s).begin(),(s).end()
#define Fill(s,v) memset(s,v,sizeof(s))


int main(){
    int T;
    cin>>T;
    int _T = T;
    while(T--){
        cout<<"Case #"<<_T-T<<": ";
        int f, s;
        cin>>f;
        int arr1 [4][4], arr2 [4][4];
        set<int> ff, ss;
        for(int i =0; i<4;i++){
                for(int j =0;j<4;j++){
                    cin>>arr1[i][j];
                    if(i==f-1) ff.insert(arr1[i][j]);
                }
        }
        cin>>s;
        for(int i =0; i<4;i++){
                for(int j =0;j<4;j++){
                    cin>>arr2[i][j];
                    if(i==s-1) ss.insert(arr2[i][j]);
                }

        }

//        for(int i = 0;i<4;i++){
//                for(int j=0;j<4;j++){
//                    cout<<arr1[i][j]<<" "<<arr2[i][j]<<endl;
//                }
//        }


        vector<int> result(10);


        auto it = set_intersection(ff.begin(),ff.end(),ss.begin(),ss.end(),result.begin());

        result.resize(it - result.begin());

        //cerr<<"GOOD"<<endl;


        if(result.size()==0){
            cout<<"Volunteer cheated!";
        }else if(result.size()>1){
            cout<<"Bad magician!";
        } else {
            cout<< *(result.begin()) ;
        }



        cout<<endl;
    }
    return 0;
}

