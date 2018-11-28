#include<bits/stdc++.h>
using namespace std;

int main()
{
     freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int z=1;
    while(t--)
    {
        int n;
        scanf("%d",&n);
        char a[n+1];
        scanf("%s",a);
    //    cout<<a<<endl;
        long long int count=0,track=0;
        track+= ((int)a[0])-48;
     //   cout<<track<<endl;
        for(int i=1;i<=n;i++)
        {
            if(track<i)
            {
                count+= i-track;
                track+= (i-track);
            }
            track+= ((int)a[i])-48;
        }
        cout<<"Case #"<<z<<": "<<count<<endl;
        z++;

    }



    return 0;
}
