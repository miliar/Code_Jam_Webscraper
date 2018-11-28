#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    FILE *file;
    int t,a,b,c,d,m,n,o,p,fin,ans=0;
    file=fopen("test.o","w");
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        int one;
        ans=0;
        cin>>one;
        for(int i=0;i<4;i++)
        {
            cin>>a>>b>>c>>d;
            if(i==one-1)
            {
                m=a;n=b;o=c;p=d;
            }
        }
        int two;
        cin>>two;
        for(int i=0;i<4;i++)
        {
            cin>>a>>b>>c>>d;
            if(i==two-1)
            {
                if(m==a||n==a||o==a||p==a)
                {
                    ans++;
                    fin=a;
                }
                if(m==b||n==b||o==b||p==b)
                {
                    ans++;
                    fin=b;
                }
                if(m==c||n==c||o==c||p==c)
                {
                    ans++;
                    fin=c;
                }
                if(m==d||n==d||o==d||p==d)
                {
                    fin=d;
                    ans++;
                }
            }
        }
        if(ans==1)
        {
            fprintf(file,"Case #");
            fprintf(file,"%d: ",k);
            fprintf(file,"%d\n",fin);
            //cout<<fin<<endl;
        }
        if(ans==0)
        {
            fprintf(file,"Case #");
            fprintf(file,"%d: ",k);
            fprintf(file,"Volunteer cheated!\n");
            //cout<<"v"<<endl;
        }
        if(ans>1)
        {
            fprintf(file,"Case #");
            fprintf(file,"%d: ",k);
            fprintf(file,"Bad magician!\n");
            //cout<<"m"<<endl;
        }
    }

}
