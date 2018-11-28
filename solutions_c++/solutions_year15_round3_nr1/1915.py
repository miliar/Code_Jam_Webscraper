#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin>>T;
    int r,c,w,count;
    for(int t=0;t<T;t++)
    {
        cin>>r>>c>>w;
        count=0;
        if(c==w || w==0)
        {
            count=w;
        }
        else if(c>w)
        {
            count=c/w;
            if(c%w!=0)
                count++;
            count=count+w-1;
        }
        cout<<"Case #"<<t+1<<": "<<count<<"\n";
    }
    return 0;
}
