#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B2.txt","r",stdin);
    freopen("out_B2.txt","w",stdout);
    int t,c,i,j,count;
    string st;
    cin>>t;
    for(c=1;c<=t;c++)
    {
        cin>>st;
        count=0;
        j=st.length();
        for(i=1;i<j;i++)
            if(st[i]!=st[i-1])
                count++;
        if(st[j-1]=='-')
            count++;
        cout<<"Case #"<<c<<": "<<count<<endl;
    }
return 0;
}
