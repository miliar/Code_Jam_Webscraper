//Ya rab ya hady, hat el Accepted el ne7yady
#include <map>
#include <cmath>
#include <deque>
#include <stack>
#include <queue>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std ;

//#define sz size()
#define eps 1e-9
#define inf 1 << 28
#define pb push_back
#define del( a ) memset( a , 0 , sizeof ( a ) )

int main ()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);

    int tc;
    cin>>tc;
    int inc=0;
    while(tc--){

    int r1,r2;
    int arr1[5][5];
    int arr2[5][5];
        cin>>r1;
        for(int i=0;i<4;++i){
            for(int j=0;j<4;++j){
                cin>>arr1[i][j];
            }
        }
        cin>>r2;

        for(int i=0;i<4;++i){
            for(int j=0;j<4;++j){
                cin>>arr2[i][j];
            }
        }

        int ans,occ;
        occ=0;
        ans=0;
        for(int i=0;i<4;++i){
            for(int j=0;j<4;++j){
                if(arr1[r1-1][i]==arr2[r2-1][j]){

                    ans=arr1[r1-1][i];
                    occ++;
                }
            }
        }
        if(occ==1){
            cout<<"Case #"<<++inc<<": "<<ans<<endl;
        }else if(occ>1){
            cout<<"Case #"<<++inc<<": Bad magician!"<<endl;
        }else{
            cout<<"Case #"<<++inc<<": Volunteer cheated!"<<endl;
        }
    }

    return 0;
}

