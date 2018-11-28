#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{
    int t,i,n,j=1;
    freopen ( "A-large.in", "r", stdin );
    freopen ("output4.txt","w",stdout);
    cin>>t;
    long long int count,total;
    while(t--)
    {
        //scanf("%d",&n);
        cin>>n;
        char s[1005];
        //scanf("%s",s);
        cin>>s;
        i=0;
        count=0;
        total=0;
        //cout<<s<<endl;
        while(s[i]!='\0')
        {
            if((s[i]-48)==0)
            {
                //cout<<"a"<<count<<endl;
                i++;
                continue;
            }
            else if(count>=i)
            {
                count+=(s[i]-48);
               // cout<<"b"<<count;
            }

            else
            {
                total+=(i-count);
                count+=((s[i]-48)+i-count);
               // cout<<"c"<<total<<" "<<count;
            }
            i++;
        }
        //printf("%lld\n",total);
        cout<<"Case #"<<j<<": "<<total<<endl;
            j++;
    }
    return 0;
}
