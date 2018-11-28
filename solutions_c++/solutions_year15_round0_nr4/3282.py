#include<bits/stdc++.h>

using namespace std;

vector<int> _divisores(int x)
{
    vector<int> divisores(0);
    for(int i = x-1 ; i > 1 ; --i){
        //cout<<x<<" "<<i<<endl;
        if(x % i == 0)divisores.push_back(i);
    }
    return divisores;
}

int main()
{
    freopen("D-small-attempt4.in", "r", stdin);
    freopen("D-small-attempt4.out", "w", stdout);
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);

    int T, x, r, c;
    cin>>T;
    bool posible;
    vector<int>::iterator it;

    for(int tc = 1 ; tc <= T ; ++tc)
    {
        posible = true;
        cin>>x>>r>>c;
        if(r<c){swap(r,c);}

        if(x>r)posible = false;
        if((x+1)/2 >= c && x >= 4)posible = false;

        for(int i = 1 ; i*i-1 <= x ; ++i){
            if((x+1)/2 > r || i > c){
                posible = false;
                break;
            }
        }

        if(r*c % x != 0){
            posible = false;
        }

        printf("Case #%d: %s\n", tc, posible?"GABRIEL":"RICHARD");
    }
    return 0;
}
