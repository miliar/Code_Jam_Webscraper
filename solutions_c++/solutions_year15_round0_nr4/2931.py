#include<iostream>
#include<cstring>
#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t,x,r,c,i,ans;
    ifstream in("input.txt");
    ofstream out("output.txt");
    in>>t;
    i=1;
    while(i<=t)
    {
        in>>x>>r>>c;
        if(x==1)
            ans=2;
        else if(x==2)
        {
            if(r%2==0||c%2==0)
                ans=2;
            else
                ans=0;
        }
        else if (x==3)
        {
            if(r>=2&&c>=2&&(r*c)%3==0)
                ans=2;
            else
                ans=0;
        }
        else if(x==4)
        {
            if(r>=3&&c>=3&&(r*c)%4==0)
                ans=2;
            else
                ans=0;
        }
        else if(x==5)
        {
            if(r*c>=20&&(r*c)%5==0)
                ans=2;
            else
                ans=0;
        }
        else if(x==6)
        {
            if((r*c)>=30&&(r*c)%6==0)
                ans=2;
            else
                ans=0;
        }
        else
            ans=0;
        if(ans==0)
            out<<"Case #"<<i<<": RICHARD"<<endl;
        else
            out<<"Case #"<<i<<": GABRIEL"<<endl;
        i++;
    }
    in.close();
    out.close();
    return 0;
}
