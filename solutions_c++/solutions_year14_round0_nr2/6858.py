#include <bits/stdc++.h>

using namespace std;

main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin>>T;
    for(int z=0;z<T;z++)
    {
        cout<<"Case #"<<z+1<<": ";
        double c,f,x;
        cin>>c>>f>>x;
        double t=0,cur=2;
        while(x/cur>c/cur+(x/(cur+f)))
            t+=c/cur,
            cur+=f;
        t+=x/cur;
        cout<<setprecision(7)<<fixed<<t<<"\n";
    }
}
