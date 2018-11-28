#include<bits/stdc++.h>

using namespace std;
int c=0;
 int vis[11];
void cnt(int n)
{
   int a;
   while(n) {
    a=n%10;
    if(vis[a]!=1)
    {
        vis[a]=1;
        c++;

    }
    n=n/10;
}
}

int main()
{
    int t;
    cin>>t;
    for(int tt=1; tt<=t; ++tt)
    {
        c=0;
         long long ans;
     for(int i =0; i <11;i++)
                 vis[i] = 0;
        int n;
        cin>>n;
        if(n==0)
        {

        cout<<"Case #"<<tt<<":"<<" "<<"INSOMNIA"<<endl;
            continue;
        }
         int i=1;
        while(1)
        {

            if(c!=10)
            {


        ans=n*i;
                cnt(n*i);
                i++;

            }
            else{
            break;

            }
        }

cout<<"Case #"<<tt<<":"<<" "<<ans<<endl;

    }


    return 0;
}
