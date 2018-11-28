#include <cstdio>
#include <set>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int tc;
    scanf("%d",&tc);
    for ( int _case = 1 ; _case <= tc ; _case ++ ) {
        int a[11][11],b[11][11],first,second;
        memset(a,0,sizeof a);
        memset(b,0,sizeof b);
        scanf("%d",&first);
        for ( int i = 1 ; i < 5 ; i++ ) 
            for ( int j = 1;  j < 5; j++ ) 
                scanf("%d",&a[i][j]);
        scanf("%d",&second);
        for ( int i = 1 ; i < 5; i++ ) 
            for ( int j = 1;  j < 5 ; j++ ) 
                scanf("%d",&b[i][j]);
        vector<int> possible;
        for ( int i = 1 ; i < 5 ; i++ ) 
            possible.push_back(a[first][i]);
        set<int> st;
        for ( int i = 1 ; i < 5 ; i++ ) 
            for ( int j = 0 ; j < possible.size() ; j++ ) 
                if ( b[second][i] == possible[j] ) 
                    st.insert(b[second][i]);
        if ( (int)st.size() == 0 ) printf("Case #%d: Volunteer cheated!\n",_case);
        else if ( (int)st.size() == 1 ) printf("Case #%d: %d\n",_case,*st.begin());
        else printf("Case #%d: Bad magician!\n",_case);
    }
    return 0;
}
