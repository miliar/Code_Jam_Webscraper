# include<bits/stdc++.h>
using namespace std;

int main()
{
    int t,x,r,c,j,p;
    cin>>t;
    for(j=1;j<=t;j++)
    {
        cin>>x>>r>>c;
        p=r*c;
        if( x==1 )
        {
               cout<<"Case #"<<j<<": "<<"GABRIEL\n"; 
        }
        else if ( x==2 )
        {
            if( p%2==0 )
              cout<<"Case #"<<j<<": "<<"GABRIEL\n";
            else
              cout<<"Case #"<<j<<": "<<"RICHARD\n";
        }
        else if ( x==3 )
        {
            if(p>4 && p!=8 && p!=16)
              cout<<"Case #"<<j<<": "<<"GABRIEL\n";
            else
              cout<<"Case #"<<j<<": "<<"RICHARD\n";
        }
        else if ( x==4 )
        {
             if( p==12 || p==16)
               cout<<"Case #"<<j<<": "<<"GABRIEL\n";
             else 
               cout<<"Case #"<<j<<": "<<"RICHARD\n";
        }
    } 
return 0;
}   
