#include<bits/stdc++.h>

using namespace std;
typedef long long ll  ;


int main()
{
    freopen("D-small-attempt5.in","rt",stdin);
    freopen("bin1.out","wt",stdout);
    int t , x , r , c , cnt = 1 ;
    cin>>t ;
    while(t--)
    {
        cin>>x>>r>>c ;
        bool flag = 1 ;
        int prod = r*c ;
        if(prod<x)flag = 0 ;
        if(prod>x)
        {
            if( (prod%x) >=1 )flag = 0 ;
        }
        if(x==3 && (r==1 || c==1) )
        {
            flag = 0 ;
        }
        else if(x==4 && (r<=2 || c<=2) )
        {
            flag = 0 ;
        }
        if(flag)
        {
            printf("Case #%d: GABRIEL\n", cnt) ;
        }
        else
        {
            printf("Case #%d: RICHARD\n", cnt) ;
        }
        cnt++ ;
    }
}
