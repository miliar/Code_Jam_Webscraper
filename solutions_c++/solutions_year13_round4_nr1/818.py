    #include <iostream>
    #include <vector>
    #include <algorithm>
    #include <cstdio>
    #include <string>
    #include <sstream>
    #include <cmath>
   #include <map>
    using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int T = 0;
    cin >> T;
    long long const mod = 1000002013LL;
    for (int step = 1; step <= T; ++step)
    {
        long long n = 0;
        int m = 0;
        cin >> n >> m;
        vector<pair<long long , long long > > arr(2*m);
        long long ans = 0LL;
        for (int i = 0; i < m; ++i)
        {
            long long s,f,p;
            cin >> s >> f >> p;
            arr[2*i].first = s;
            arr[2*i].second = -p;
            arr[2*i+1].first = f;
            arr[2*i+1].second = p;
            long long l = f-s;
            ans += ((l*(2*n-l+1)/2)%mod)*(long long)p;
            ans %= mod;
        }
        sort(arr.begin(),arr.end());

        long long cur = 0;
        vector<pair<long long, long long> > a(2*m);
        for (int i = 0; i < 2*m; ++i)
        {
            cur -= arr[i].second;
            a[i].first = arr[i].first;
            a[i].second = cur;
        }

        for (int i = 0; i < 2*m;)
        {
            long long c = a[i].second;
            for (int j = i; j < 2*m; ++j)
            {
                if (a[j].second == 0)
                {
                    if (j == i)
                        ++i;
                    for (int k = i; k < j; ++k)
                        a[k].second -= c;
                    c%=mod;
                 //   cout << a[i].first <<" "<<a[j].first << " "<< c << " "<<ans <<endl;
                    long long l = a[j].first - a[i].first;
                    ans -= c*((l*(2*n-l+1)/2)%mod);
                    if (ans < 0)
                        ans += (ans/mod + 1)*mod;
                    ans %= mod;
                }
                c = min(c , a[j].second);
            }
        }
        cout << "Case #"<<step<<": "<< ans <<"\n";
    }


    return 0;
}


