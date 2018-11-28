#include<iostream>
using namespace std;
int a[300010];
int b[300010];
int abs(int x)
{
    if(x>=0)return x;
    return -x;
}
int si(int x)
{
    if(x>0)return 1;
    return -1;
}
int func(int x,int y)
{
    int xx=abs(x),yy=abs(y);
    if(xx==yy)return -1*si(x*y);
    if(xx==1 || yy==1)return x*y;
    if(xx==2 && yy==3)return 4*si(x*y);
    if(xx==3 && yy==2)return -4*si(x*y);
    if(xx==3 && yy==4)return 2*si(x*y);
    if(xx==4 && yy==3)return -2*si(x*y);
    if(xx==4 && yy==2)return 3*si(x*y);
    if(xx==2 && yy==4)return -3*si(x*y);
}
int main()
{
    string s;
    int i,j,k,l,c;
    long long x;
    int t;
    cin>>t;
    c=1;

    while(t--)
    {
        cin>>l>>x;
        cin>>s;
        j=0;
        bool f1,f2;
        f1=f2=false;
        int total = 1;
        if(x>12)
        {
            x=12+(x%4);
        }
        for(i=0;i<x;i++)
        {
            for(k=0;k<s.size();k++)
            {
                a[j]=(s[k]-'i'+2);
                total = func(total,a[j]);
                b[j]=total;
                if(b[j]==2)f1=true;
                if(f1 && b[j]==4)f2=true;
                j++;
            }
        }
//        for(i=0;i<x*s.size();i++)
//        {
//            cout<<b[i]<<' ';
//        }
//        cout<<endl;
        if(f1 && f2 && total==-1)
        {
            cout<<"Case #"<<c<<": YES\n";
            c++;
        }else
        {
            cout<<"Case #"<<c<<": NO\n";
            c++;
        }


    }
}
/*
2
2 6
ji
*/
