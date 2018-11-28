#include<iostream>
#include<conio.h>
#include<cmath>
#include<string>
#include<sstream>
using namespace std;
int main()
{
    int test,i,j,m;
    long a,b,x,y,pr;
    scanf("%d",&test);
    int co=1;
    while(test--)
    {
        scanf("%ld%ld",&a,&b);
        x=sqrt(a);
        y=sqrt(b); 
        //cout<<"a :"<<a<<"b :"<<b<<endl;
        string str1,str2;
        if(x * x < a)
            x=x+1;
        int count=0,l;
        //cout<<"x :"<<x<<"y :"<<y<<endl;
        for(i=x;i<=y;i++)
        {
            stringstream s1;
            s1.str(" ");
            s1<<i;
            s1>>str2;
            l=str2.length();
            if(l%2==0)
                m=(l/2)-1;
            else
                m=l/2;
            int flag1=0;
            l=l-1;
            for(j=0;j<=m;j++)
            {
                if(str2[j]!=str2[l-j])
                {
                    flag1=1;
                    break;
                }
            }
            pr=i*i;
            stringstream ss;
            ss.str(" ");
            ss<< pr;
            ss>>str1;
            l=str1.length();
            if(l%2==0)
                m=(l/2)-1;
            else
                m=l/2;
            int flag=0;
            l=l-1;
            for(j=0;j<=m;j++)
            {
                if(str1[j]!=str1[l-j])
                {
                    flag=1;
                    break;
                }
            }
            if((flag==0)&(flag1==0))
                count++;
            flag=0;
            flag1=0;
            //cout<<"i: "<<i<<"count :"<<count<<endl;
        }
        cout<<"Case #"<<co<<": "<<count<<endl;
        co++;
        count=0;
    }
    getch();
    return 0;
}
