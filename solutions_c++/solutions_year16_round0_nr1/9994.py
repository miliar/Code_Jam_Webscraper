#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );
    long long t,n,i,j,k,ans=0;
    set<int> s;
    cin >> t;
    for(i=1;i<=t;i++){
        cin >> n;
        s.clear();
        printf("Case #%d: ",i);
        if(n==0)
            printf("INSOMNIA\n");
        else{
            j=1;
            while(s.size()!=10)
            {
                k=n*j;
                ans=k;
                while(k){
                    s.insert(k%10);
                    k/=10;
                }
                j++;
            }
            printf("%d\n",ans);
        }

    }
}
