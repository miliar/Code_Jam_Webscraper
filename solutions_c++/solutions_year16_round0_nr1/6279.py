#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("Counting sheep.txt","w",stdout);
    int t;
    cin>>t;
    for(int i = 1;i <= t; i++){
        set<int>k;
        int n, p, ans, v;
        cin>>n;
        bool c = true;
        for(int j = 1; ; j++){
        p = j*n;
        while(p){
                int s = p%10;
            k.insert(s);
            p /= 10;
        }
        //cout<<p<<" "<<n<<" "<<j<<endl;
        //cout<<n*j<<endl;
        //cout<<k.size()<<endl;
        v = j;
        if(k.size() == 10)break;
        if(j > 200 and k.size() == 0){ c = false;break;}

        }
        if(c == true)
        printf("Case #%i: %i\n", i, n*v);
        else printf("Case #%i: INSOMNIA\n", i);
        k.clear();
    }
}
