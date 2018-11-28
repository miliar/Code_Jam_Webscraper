#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int t,n1,n2,a[4][4],b[4][4],c[100],check,t1=0,n;
    freopen("input.in","rt",stdin);
    freopen("output_final.txt","wt",stdout);
    cout<<"No of cases:";
    cin>>t;
    while(t1<t)
    {
        cout<<"case #"<<t1+1<<":";
        check=0;
        cout<<"first answer:";
        cin>>n1;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            cin>>a[i][j];
            cout<<"second answer:";
        cin>>n2;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            cin>>b[i][j];
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                if(a[n1-1][i]==b[n2-1][j])
            {
                check++;
                n=a[n1-1][i];
            }
            }
           if(check==1)
            c[t1]=10*n;
            else if(!check)
                c[t1]=3;
            else
                c[t1]=2;
            t1++;
    }
    for(int i=0;i<t;i++)
    switch(c[i])
    {
        case 2:
    cout<<"\nCase #"<<i+1<<": Bad magician!";
    break;
    case 3:
        cout<<"\nCase #"<<i+1<<": Volunteer cheated!";
        break;
    default:
        cout<<"\nCase #"<<i+1<<": "<<c[i]/10;
        break;
    }
    return 0;

}
