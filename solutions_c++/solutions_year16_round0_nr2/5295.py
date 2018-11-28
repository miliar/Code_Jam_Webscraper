#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B4.in","r",stdin);
    //freopen("out6.txt","w",stdout);
    int t,i,j,x,y,z,n,l;
    string s,b;
    scanf("%d",&t);z=1;
    while(t--)
    {
        cin>>s;//b.assign(s);
        n=s.size();x=0;y=0;
        for(i=0;i<n;i++)
        {
            l=0;
            if(s[i]=='+')
            {
                x++;
            }
            else if(x==0)
            {
                while(s[i]=='-')
                {
                  i++;l++;
                }
                y++;
                if(l>0)
                    i--;
                break;
            }
            else
            {
                while(s[i]=='-')
                {
                  i++;l++;
                }
                if(l>0)
                    i--;
                y+=2;break;
            }
        }
        //cout<<y<<" "<<n<<endl;
        j=i;
        for(i=j+1;i<n;i++)
        {
            l=0;
            if(s[i]=='+')
                continue;
            else
                {
            while(s[i]=='-')
                {
                  i++;l++;
                }
             if(l>0)
                    i--;
            y+=2;

        }
        }
        printf("Case #%d: %d\n",z,y);
        z++;s.clear();
    }
    return 0;
}
