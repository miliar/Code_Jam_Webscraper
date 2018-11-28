# include <iostream>
# include <cstring>
# include <string>
# include <stack>
# include <vector>
# include <queue>
using namespace std;
# define endl '\n'
# define ll long long
# define mod 1000000007
ll int t,tt,len,firstminus,top,count;
string inp;
void flip(int start)
{
    char a;
    int i,j;
    for(i=start,j=len-1;i<j;++i,--j)
    {
        a = inp[j];
        inp[j] = inp[i];
        inp[i] = a;
        if(inp[i]=='+')
            inp[i] = '-';
        else
            inp[i] = '+';
        if(inp[j]=='+')
            inp[j] = '-';
        else
            inp[j] = '+';
    }
    if(i==j)
    {
        if(inp[i]=='+')
            inp[i] = '-';
        else
            inp[i] = '+';
    }
}
int main ()
{
    cin>>t;
    for(tt=0;tt<t;++tt)
    {
        cin>>inp;
        int i,j;
        char a;
        len = inp.length();
        for(i=0,j=len-1;i<j;++i,--j)
        {
            a = inp[j];
            inp[j]=inp[i];
            inp[i]=a;
        }
        count=0;
        for(i=0;i<len;++i)
            if(inp[i]=='-')break;
        firstminus = i;
        top = len-1;
        while(firstminus!=len)
        {
            if(inp[top]=='-')
            {
                flip(firstminus);
                count++;
                //recalculate firstminus
                while(inp[firstminus]=='+')firstminus++;
            }
            else
            {
                for(i=top;inp[i]=='+';--i)
                    inp[i]='-';
                count++;
            }
        }
        cout<<"Case #"<<tt+1<<": "<<count<<endl;
    }
    return 0;
}
