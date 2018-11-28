#include<bits/stdc++.h>
using namespace std;
string flip(string str,int no)
{
    for(int i=0;i<no+1;i++)
    {
        if(str[i]=='-')
            str[i]='+';
        else
            str[i]='-';
    }
    return str;
}

int main() {

    freopen("largeinputC2.txt","r",stdin);
    freopen("largeoutputC2.out","w",stdout);
    int t,j,i,n,cnt;
    string s;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cnt=0;
        cin>>s;
        for(j=s.length()-1;j>=0;j--)
        {
            if(s[j]=='-')
            {
                cnt++;
                s=flip(s,j);
            }
            //cout<<abc<<endl;
        }
        cout<<"Case #"<<i<<": "<<cnt<<endl;
    }
    return 0;
}

