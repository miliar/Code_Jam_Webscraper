#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen ("in", "r", stdin);
	freopen ("o","w",stdout);
	int t ;cin >> t ;
	for(int I = 1 ;I <= t ;I++){
        printf("Case #%d: ",I) ;
        int s ;cin >> s;
        char a[s+2] ;
        scanf("%s",&a) ;
        int ans = 0 ;
        int h = 0 ;
        for(int i = 0 ;i < strlen(a) ;i++){
            if(i <= h)h+=(a[i]-'0') ;
            else if(i!=0){
                int x = i - h ;
                ans+= i- h ;
                h += ((a[i]-'0')) + x  ;
             }
        }
        cout <<ans <<endl ;

	}
    return 0;
}
