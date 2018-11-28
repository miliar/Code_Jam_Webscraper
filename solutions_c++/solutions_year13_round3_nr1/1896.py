#include<cstdio>
#include<algorithm>
#include<iostream>
#include<string>
using namespace std;
int main()
{
    freopen("C:\\Users\\Utkarsh\\Desktop\\input.in","r",stdin);
    freopen("C:\\Users\\Utkarsh\\Desktop\\out.txt","w",stdout);
    int t,k,i,j,l,f,n,l1,x,y,z,l2,l3;
    string s,s1,s2;
    scanf("%d",&t);
    for(f=1;f<=t;f++)
    {
        cin>>s;
        scanf("%d",&n);
        l=s.length();
        int c=0;
        int flag=0;
        for(i=l;i>=n;i--)
        {
            for(j=0;j<l-i+1;j++)
            {
            s2=s.substr(j,i);
            l1=s2.length();
            for(y=0;y<l1-n+1;y++)
            {
             flag=0;
             for(x=y;x<y+n;x++)
             {
            if(s2[x]=='a'||s2[x]=='e'||s2[x]=='i'||s2[x]=='o'||s2[x]=='u')
                flag=1;
             }
            if(flag==0)
             {c++;
             break;
             }
            }
        }
        }
        printf("Case #%d: %d\n",f,c);
    }
return 0;
}
