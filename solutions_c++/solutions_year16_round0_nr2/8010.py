#include <bits/stdc++.h>

using namespace std;

int t, sz, pos, ans;
char ch;
string str;

bool isHappy()
{
    for(int i=0;i<sz;i++)
        if(str[i]=='-')
            return false;
    return true;
}

void flip(int beg, int end)
{
    while(beg<=end)
    {
        ch = str[beg];
        str[beg] = str[end]=='+'?'-':'+';
        str[end] = ch=='+'?'-':'+';
        beg++;
        end--;
    }
}


int main()
{
    ios_base::sync_with_stdio(0);
    cin>>t;
    for(int ca=1;ca<=t;ca++)
    {
        ans = 0;
        cin>>str;
        sz = str.size();
        //cout<<str<<endl;
        while(!isHappy())
        {
            //cout<<str<<endl;
            for(pos=1;pos<=sz;pos++)
            {
                if(str[pos]!=str[pos-1])
                    break;
            }
            if(pos!=sz || str[pos-1]=='-')
            {
                flip(0, pos-1);
                ans++;
            }
        }
        cout<<"Case #"<<ca<<": "<<ans<<endl;
    }
    return 0;
}
