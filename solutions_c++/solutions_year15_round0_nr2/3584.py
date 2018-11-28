#include<bits/stdc++.h>

using namespace std; 

const int MX = 1005; 

int t[MX]; 

int main () { 
    int q; 
    scanf("%d",&q); 
    for ( int x = 1; x <= q; x++ ) { 
        int n; 
        scanf("%d",&n);
        int result = 0; 
        for ( int i = 0; i < n; i++ ) { 
            scanf("%d",&t[i]);
            result=max(result,t[i]); 
        }
        int maks = result; 
        for ( int i = 1; i < maks+1; i++  ) { 
            int wyn = i; 
            for ( int j = 0; j < n; j++  ) { 
                if ( t[j]%i == 0 ) 
                    wyn--;     
                wyn+=(t[j]/i); 

            }
            result=min(wyn,result); 
        }
        printf("Case #%d: %d\n",x,result); 
    }
}
