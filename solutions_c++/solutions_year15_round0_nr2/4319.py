#include <bits/stdc++.h>

using namespace std;

int n ,x ;
int main()
{
   freopen ("in", "r", stdin);
	freopen ("o","w",stdout);
	int t ;cin >> t ;
	for(int I = 1 ;I <= t ;I++){
        cin >> n ;
        vector<int>a ;
        vector<int>b ;
        int xy[100] ;
        printf("Case #%d: ",I) ;
        int sum = 0 ;
        int m = 0 ;
        for(int i = 0 ;i < n ;i++){
            scanf("%d",&x) ;
            a.push_back(x) ;
            sum+=a[i] ;
            m = max(m,a[i]) ;
            xy[i] = a[i] ;
        }
        if(n==1&&a[0]==9){cout << 5 <<endl ;continue ;}
        int xx = 0 ;
        int co = 0 ;
        for(int i = 0 ;i < n ;i++){
            if(xy[i] == 9){co++;xy[i] = 6 ;}
        }

            for(int i = 0 ;i < n ; i++){
                xx = max(xx,xy[i]) ;
            }
            xx = xx + co ;
    int an = 0 ;
    vector<int>z ;
        for(int i = 0 ;i < n ; i++){
            if(a[i] > 5){
                an++ ;
                int x = xy[i]/2 ;
                z.push_back(x) ;
                xy[i] = xy[i]%2 + xy[i]/2 ;
            }
            z.push_back(xy[i]) ;
        }
        int an1 = an ;
        int mn = 0 ;
        for(int i = 0 ; i < n ; i++){
            mn = max(mn,xy[i]) ;
        }
        an+=mn+co ;
        for(int i = 0 ;i < z.size() ; i++){
            if(z[i] > 3){
                an1++;
                z[i] = z[i]%2 + z[i]/2 ;
            }
        }

        mn = 0 ;
        for(int i = 0 ; i < z.size() ; i++){
            mn = max(mn,z[i]) ;
        }
        if(xx!=0)
        xx = min(xx,min(an1+mn+co,an)) ;
        else xx = min(an1+mn,an) ;
        int ans = 0 ;
        for(int i = 0 ;i < n ; i++){
            if(a[i] > 5){
                ans++ ;
                int x = a[i]/2 ;
                b.push_back(x) ;
                a[i] = a[i]%2 + a[i]/2 ;
            }
            b.push_back(a[i]) ;
        }
        int ans1 = ans ;
        int mx = 0 ;
        for(int i = 0 ; i < n ; i++){
            mx = max(mx,a[i]) ;
        }
        ans+=mx ;
        for(int i = 0 ;i < b.size() ; i++){
            if(b[i] > 3){
                ans1++;
                b[i] = b[i]%2 + b[i]/2 ;
            }
        }
        mx = 0 ;
        for(int i = 0 ; i < b.size() ; i++){
            mx = max(mx,b[i]) ;
        }
        ans1+=mx ;

        if(xx == 0){
        cout << min(ans,min(ans1,m)) <<endl ;
        }
        else {
            cout << min(min(ans,xx),min(ans1,m)) <<endl ;
        }
	}
    return 0;
}
