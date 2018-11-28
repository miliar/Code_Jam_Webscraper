#include<iostream>
#include<math.h>
using namespace std;
int main()
{
    long int num=0;
    long int large=0,l2,ln;
    long int li[500];
    long int i,j,k,n,t,c,p[500];
    cin>>t;
    for(j=0;j<t;j++)
    {
        num=0;
        large=0;
        l2=0;
        cin>>n;
        for(i=0;i<n;i++)
        {
            cin>>p[i];
            num+=p[i];
            if(p[i]>large)
            {
                large=p[i];
                li[0]=i;
            }
        }
        cout<<"Case #"<<j+1<<": ";
        ln=-1;
        while(num>0)
        {
            l2=0;
            ln=-1;
            for(i=0;i<n;i++)
            {
                if(large==p[i])
                {
                    ln++;
                    li[ln]=i;
                }
            }
            for(i=0;i<n;i++)
            {
                if(p[i]<large)
                {
                    if(p[i]>l2)
                    {
                        l2=p[i];
                    }
                }
            }

            if(ln>1)
            {
                while(ln>1)
                {
                for(k=0;k<large-l2;k++)
                {
                    cout<<(char)('A'+li[ln])<<' ';
                    num--;
                    p[li[ln]]--;
                }
                ln--;
                }
            }
            if(ln==1)
            {
                for(k=0;k<large-l2;k++)
                {
                    cout<<(char)('A'+li[ln])<<(char)('A'+li[ln-1])<<' ';
                    num-=2;
                    p[li[ln]]--;
                    p[li[ln-1]]--;
                }
                ln-=2;
            }
            if(ln==0)
            {
                for(k=0;k<large-l2;k++)
                {
                    cout<<(char)('A'+li[ln])<<' ';
                    num--;
                    p[li[ln]]--;
                }
                ln--;
            }
            if(l2==0)
            {
                break;
            }
            large=l2;
            for(i=0;i<n;i++)
            {
                if(large==p[i])
                {
                    ln++;
                    li[ln]=i;
                }
            }
        }
        cout<<"\n";
    }
    return 0;
}
