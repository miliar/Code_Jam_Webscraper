#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<map>
using namespace std;
int T;
int a[10];
void solve(long long s, int &count){
    //cout << s << " " << count << endl;
    while(s){
        int n_mod = s % 10;
        if (a[n_mod] == 0){
            a[n_mod] = 1;
            count++;
        }
        s = s / 10;
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>T;
    int t = 0;
    while(t < T)
    {
        t++;
        memset(a, 0, sizeof(a));
        long long n;
        cin >> n;
        if (n != 0){
            int count = 0;
            long long sum = 0;
            while(count < 10){
                sum += n;
                solve(sum, count);
            }
            printf("Case #%d: %lld\n",t, sum);
        }
        else
            printf("Case #%d: INSOMNIA\n", t);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
