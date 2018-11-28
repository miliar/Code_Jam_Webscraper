#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> v1,v2,v3;

int work(vector<int> &v){
    int n ;
    v.clear();
    scanf("%d",&n);
    for (int i = 0 ; i < 4 ; ++i ){
        int a ;
        if ( i + 1 == n ){
            for (int j = 0 ; j < 4 ; ++j ){
                scanf("%d",&a);
                v.push_back(a);
            }
        }else{
            for ( int j = 0 ; j < 4 ; ++j )
                scanf("%d",&a);
        }
    }
    sort(v.begin(),v.end());
}
int main(){
    int t ;
    scanf("%d",&t);
    for (int i = 0 ; i < t ; ++i ){
        v3.clear();
        v3.resize(10);
        work(v1);
        work(v2);
        vector<int>::iterator it = set_intersection
            (v1.begin(),v1.end(),v2.begin(),v2.end(),v3.begin());
        int size = it-v3.begin();
        if ( size == 1 ){
            printf("Case #%d: %d\n",i+1,*(v3.begin()));
        }else if ( size > 0 ){
            printf("Case #%d: Bad magician!\n",i+1);
        }else
            printf("Case #%d: Volunteer cheated!\n",i+1);
    }
}
