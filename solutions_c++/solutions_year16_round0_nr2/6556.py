#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;

typedef vector<int>vi;
typedef pair<int,int>ii;
typedef vector<ii>vii;
#define M 1000000007
const int INF = (int) 1e9;
const int MAX = (int) 1e5 + 10;
map<ll,int>ma ;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("outpu.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int co=1,n;
    string s;
    while(t--)
    {
        stack<char>st,stemp;
        printf("Case #%d: ",co++);
        cin>>s;
        int n =s.size();
        for(int i=s.size()-1;i>=0;i--)
        {
            st.push(s[i]);
        }
        int ans =0;
        while(1)
        {
            int la=0,val;
            while(!st.empty())
            {
                char t= st.top();
                if(t=='+')
                {
                    if(la==0)
                    {
                        val =-1;
                        st.pop();
                    }
                    else
                    {
                        if(val==-1)
                        {
                            st.pop();
                        }
                        else
                        {
                            break;
                        }
                    }
                    la++;
                    stemp.push('-');
                }
                else
                {
                    if(la==0)
                    {
                        val=-2 ;
                        st.pop();
                    }
                    else
                    {
                        if(val==-2)
                        {
                            st.pop();
                        }
                        else
                        {
                            break;
                        }
                    }
                    la++;
                    stemp.push('+');
                }

            }
            if(st.empty())
            {
                if(!stemp.empty() and stemp.top()=='+')ans++;
                break;
            }
            while(!stemp.empty())
            {
                st.push(stemp.top());
                stemp.pop();
            }
            ans++;
        }
        printf("%d\n",ans);

    }
    return 0;
}
