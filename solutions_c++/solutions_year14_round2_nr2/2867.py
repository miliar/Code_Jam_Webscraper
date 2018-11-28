using namespace std;
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>


int main()
{
    freopen("BB-small-attempt0.in","r",stdin);
    freopen("BBB-small-attempt1.out","w",stdout);
    int test,a,b,c,k,count,iter=1;
    scanf("%d",&test);
    while(test--)
    {

        cin>>a>>b>>k;
        count=0;
        //c = a&b; cout<<c<<endl;

        for(int i=0;i<a;i++)
        {
            for(int j=0;j<b;j++)
            {
                c = i&j;
                if(c<k)
                {
                    count++;
                }
            }
        }

        cout<<"Case #"<<iter<<": "<<count<<endl;
        iter++;

    }

    return 0;

}

