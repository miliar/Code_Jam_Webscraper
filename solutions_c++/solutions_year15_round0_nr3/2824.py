
#include<iostream>

using namespace std;

int s1,s2,s3=1,t,i,j,l,n,k,x,ans;
char c1,c2,c3,s[10000];
void mx(char c1,char c2)
{
    if(c1=='1')
    {
        c3=c2;
       // s3=s2;
        return;
    }
    if(c2=='1')
    {
        c3=c1;
      //  s3=s1;
        return;
    }
   // s3=s3*s1*s2;
    if(c1==c2)
    {
        c3='1';
        s3 = s3*-1;
        return;
    }
    if(c1=='i' && c2=='j')
    {
    c3='k';
    return;
    }
    if(c1=='j'&& c2=='i')
    {
    c3='k';
    s3=s3*(-1);
    return;
    }
    if(c1=='j' && c2=='k')
    {
    c3='i';
    return;
    }
    if(c1=='k'&& c2=='j')
    {
    c3='i';
    s3=s3*(-1);
    return;
    }
    if(c1=='k' && c2=='i')
    {
    c3='j';
    return;
    }
    if(c1=='i'&& c2=='k')
    {
    c3='j';
    s3=s3*(-1);
    return;
    }
}
int main()
{
    cin>>t;
    char nc,mc,oc='1';
    int sx;
    int store;
    for(k=1;k<=t;k++)
    {
        s3=sx=1;
        oc='1';
        store=0;
        cin>>l>>x>>s;
        mc=s[0];

        for(i=0;i<x;i++)
        {
            for(j=0;j<l;j++)
            {
           // cout<<s3<<" "<<oc<<" [*] "<<s[j]<<" = ";
            //    if(i==0 && j==0) continue;
            //    if((l-j)!=1)
             //   {
                    mx(oc,s[j]);
                    oc = c3;
               // }
            //   cout<<s3<<" "<<oc<<endl;
            if(oc=='i'&&s3==1&&store==0) {
            store = 1;
 //           s3=1;
   //         oc='1';
            }
            if(oc=='k'&&s3==1&&store==1) {
            store = 2;
     //       s3=1;
      //      oc='1';
            }
            if(oc=='1'&&s3==(-1)&&store==2) {
            store = 3;

            }
            }
        }
        if(oc=='1'&&s3==(-1)&&store==3)
        cout<<"Case #"<<k<<": YES\n";
        else cout<<"Case #"<<k<<": NO\n";
    }
}
