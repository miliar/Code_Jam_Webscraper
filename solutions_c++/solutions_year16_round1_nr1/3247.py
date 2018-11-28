/**
submitted by: prakhar8795
Sleep. Code. Eat. Repeat.
*/

#include<bits/stdc++.h>
using namespace std;


typedef long long int ll ;
typedef unsigned long long int ull ;

void solve()
{
    int test ;
    scanf("%d",&test) ;
    int k=1 ;
    while(test--) {
        string s ;
        cin>> s ;
        string temp="" ;
        temp += s[0] ;
        int len=s.length() ;
        int currLeft = s[0], currRight= s[0] ;
        printf("Case #%d: ",k) ;
        for(int i=1 ; i<len ; i++) {
            if(s[i]<=currRight) {
                temp+=s[i] ;
                currRight=s[i] ;
            }
            else {
                if(s[i]>=currLeft) {
                    temp = s[i] + temp ;
                    currLeft = s[i] ;
                }
                else {
                    temp+= s[i] ;
                    currRight= s[i] ;
                }
            }
        }
        cout << temp  << "\n" ;
        k++ ;
    }
}

int main()
{
    freopen("A-large.in","r",stdin) ;
    freopen("ALargeout.out","w",stdout) ;
    solve() ;
    return 0 ;
}


