#include <bits/stdc++.h>
using namespace std;
int main() {
    int t;
    int a[5000];
 
    int n,i,k ,j,max,min,sum;
    freopen("B2.in","r",stdin);
    cin>>t;
 
    for(k=0;k<t;k++)
	 {
        cin>>n;
        max = 0;
        for(i = 0 ; i < n ; i++) 
		{
           cin>>a[i];
            if (a[i] > max)
                max = a[i];
        }
 
        min = max;
 
        for(i = 1 ; i <= max ; i++) 
		{
            sum = i ;
            for(j = 0 ; j < n ; j++) {
                if( a[j] > i ) {
                    if( a[j]%i == 0 )
                        sum += (a[j]/i-1) ;
                    else
                        sum += (a[j]/i) ;
                }
            }
            if (sum < min)
                min = sum;
        }
        cout<<"Case #"<<k + 1<<": "<<min<<endl;
    }
    return 0 ;
}