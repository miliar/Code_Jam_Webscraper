# include<iostream>
using namespace std;
int main()
{
        int t;
        cin>>t;int ans[t],j=0,i=0,x;string y;
        while(t--)
        {
            int g=0,g1=0;
            cin>>x;cin>>y;
            for(int i=0;i<x;i++)
            {
                g=g+y[i]-48;
                //ut<<g<<endl;
                if(g<i+1)
                {g1=g1+i+1-(g);g=i+1;//ut<<"\t"<<g1<<endl;
                }
            }
            ans[j++]=g1;
        }

    for(int y=0;y<j;y++)
       cout<<"Case #"<<y+1<<": "<<ans[y]<<endl;
    return 0;
}
