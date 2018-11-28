#include<bits/stdc++.h>
using namespace std;

char s[10010],s1[10010];

int main()
{
    freopen("C-small-attempt3.in","r",stdin);
    freopen("ans3.txt","w",stdout);

    int i,t,n,ans,j,k,x,l,p,J,r,flag;
    int m[8][8]={{1,2,3,4,5,6,7,8},{2,5,4,7,6,1,8,3},{3,8,5,2,7,4,1,6},{4,3,6,5,8,7,2,1},{5,6,7,8,1,2,3,4},{6,1,8,3,2,5,4,7},{7,4,1,6,3,8,5,2},{8,7,2,1,4,3,6,5}};

    cin>>t;
    for(int J=1;J<=t;J++)
    {
        cin>>l>>x;
        cin>>s1;
        strcpy(s,s1);
        for(i=1;i<x;i++)
            strcat(s,s1);
//        if(J==28)
//            cout<<l<<" "<<x<<" "<<s1<<endl;
        l=l*x;

        flag=0;
        ans=-1;
        if(l>2)
        {
            k=s[0]-103;
            i=0;
            while(k!=2 && i<l-1)
            {
                i++;
//                cout<<i<<" "<<k<<endl;
                p=s[i]-103;
                k=m[k-1][p-1];
//                cout<<p<<" "<<k<<endl;
            }
            if(k==2)
                flag=1;
            if(flag==1)
            {
                i++;
                k=s[i]-103;

                while(k!=3 && i<l-1)
                {
                    i++;
//                    cout<<i<<" "<<k<<endl;
                    p=s[i]-103;
                    k=m[k-1][p-1];
                }
                if(k==3)
                    flag=2;
            }
            if(flag==2)
            {
                i++;
                k=s[i]-103;

                while(i<l-1)
                {
                    i++;
//                    cout<<i<<" "<<k<<endl;
                    p=s[i]-103;
                    k=m[k-1][p-1];

                }
                if(k==4)
                    flag=3;
            }
            if(flag==3)
                ans=1;
        }

        if(ans==-1)
            cout<<"Case #"<<J<<": NO"<<endl;
        else
            cout<<"Case #"<<J<<": YES"<<endl;
    }
    return 0;
}
