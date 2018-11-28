#include <iostream>
#include <fstream>
using namespace std;

struct PQ{
int p;
int q;
};
int ans;
int res;
int i;
bool doit(PQ pq)
{
    pq.q /= 2;
    if(ans > 40){return false;}
    if(pq.q == 1|| pq.p == pq.q){if(ans < res)res = ans;return true;}
    if(pq.q % 2){return false;}
    if(pq.p > pq.q){
        pq.p -= pq.q;
        if(ans < res)
        res = ans;
        ans++;
        if(doit(pq)){
            return true;
        }
        else{
            return false;
        }
    }
    ans++;
    if(doit(pq))return true;
    else return false;
}
int main()
{
    int t;
    PQ pq;
    fstream fs1,fs2;
    fs1.open("C:\\A-small-attempt0.in");
    fs2.open("C:\\A-small-attempt0.out");
    fs1 >> t;
    //cin>>t;
    char c;
    for(i = 1; i <= t ; i++)
    {
        fs1 >> pq.p;
        fs1 >> c;
        fs1 >> pq.q;

        if(pq.q % 2 != 0){fs2 << "Case #" << i << ": impossible"<<endl;}
        else{
            ans = 1;
            res = 45;
            if(doit(pq))fs2 <<"Case #" << i << ": " << res <<endl;
            else fs2 << "Case #" <<i << ": impossible\n";
        }

    }

    return 0;
}
