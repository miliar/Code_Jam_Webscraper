#include <bits/stdc++.h>
#include <vector>
#include <algorithm>

using namespace std;

#define ll unsigned long long
#define vv vector< vector<int> >
#define v vector<int>
#define compare(x,y) (((x)<(y))?-1:((x)==(y))?0:1)

int min(int x, int y)
{
    if(x<y)
        return x;
    else
        return y;
}

int main()
{
    int t, u, i, j, len, k;
    
    
    freopen("AL.in", "r", stdin);
    freopen("AL.out", "wt", stdout);
    
    cin>>t;
    
    u=1;
    while(u<=t)
    {
        char str[1005]="\0", str2[1005]="\0";
        cin>>str;
        len=strlen(str);
        
        //c=str;
        str2[0]=str[0];
        i=0;
        //c++;
        k=1;
        while(k<len)
        {
            if(str[k]<str2[0])
            {   i++;
                str2[i]=str[k];
            }
            else
            {
                for(j=i;j>=0;j--)
                    str2[j+1]=str2[j];
                str2[0]=str[k];
                i++;
            }
            k++;
        }
        
        cout<<"Case #"<<u<<": "<<str2<<endl;
        u++;
    }
}

/* */