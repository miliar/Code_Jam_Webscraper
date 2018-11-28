//-_- Dpn -_-\\

#include<bits/stdc++.h>

using namespace std;

int game(int x,int r,int c)
{
    if (x == 1)
        return 1;
    if (x == 2)
        if ((min(r,c)==1) && (max(r,c)==2))
            return 1;
    if (x == 4)
        if (min(r,c)==2 && max(r,c)==4)
            return 0;
    if ((r*c) <= x || (r*c)%x != 0)
        return 0;
    return 1;
}

int main(void)
{
    int T, X, R, C, T2;
    cin>>T;
    T2 = T;
    string ans;
    while(T--)
    {
        cin>>X>>R>>C;
        if (game(X,R,C) == 1)
            ans = "GABRIEL";
        else
            ans = "RICHARD";
        cout<<"Case #"<<T2-T<<": "<<ans<<endl;
    }
    return 0;
}
