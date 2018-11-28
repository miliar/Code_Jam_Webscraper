#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("A-large (2).in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t,f,l,i,iner,len;
    string str,str1;
    char a[50000];
    cin>>t;
    for(iner=1;iner<=t;iner++)
    {
        printf("Case #%d: ",iner);
        f=l=1015;
        str1="";
        cin>>str;
        a[f]=str[0];
        l++;
        len=str.size();
        for(i=1;i<len;i++)
        {

            if(str[i]>=a[f])
                {
                    f--;
                    a[f]=str[i];
                }
            else
            {
                a[l]=str[i];
                l++;
            }
        }
        for(i=f;i<l;i++)
            cout<<a[i];
        cout<<endl;
    }
}
