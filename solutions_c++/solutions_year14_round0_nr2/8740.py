#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int te;
    cin>>te;
    double c, f, x ;
    for(int t =  1 ; t<= te; t++ )
    {
        cin>>c>>f>>x;
        double cnt = 0.0 ;
        double low = x/2.0 , current = x/2.0 ;
        double i = 2.0 ;
        while(current <= low )
        {

            current = cnt + x/i ;

            if(current<low)
                low = current;
            cnt += c/i;
            i += f;


        }
        printf("Case #%d: %.7lf\n" , t , low + 1e-8);
    }


    return 0;
}
