#include<iostream>

using namespace std;

int n, m, t, l1, l2;
int a[16], b[16];

int main()
{
    freopen("B-large.in", "r", stdin);
    //freopen("B-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin>>t;
    int num = 0;    
    double c, f, x;
    while(num < t) {
        ++num;
        cin>>c>>f>>x;
        int n = 0;        
        double ans = x/2, buy = 0, now;
        while(true){                        
            ++n;
            buy += c / (2 + (n-1) * f);            
            if (buy > ans) break;
            now = buy + x / (2 + n * f);            
            if (now < ans) ans = now;
            //else break;
            //cout<<n<<": "<<ans<<' '<<buy<<endl;
        }
        printf("Case #%d: %.9lf\n", num, ans);        
    }    
    return 0;
}
