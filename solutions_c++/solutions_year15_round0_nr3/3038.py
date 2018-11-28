#include <bits/stdc++.h>
#define For(i,l,r) for (int i=l;i<=r;i++)
#define Rep(i,n) for(int i=0,n__=n;i<n__;i++)
using namespace std;
const int muld[4][4]=
{
{1,2,3,4},
{2,-1,4,-3},
{3,-4,-1,2},
{4,3,-2,-1},
};
int mul(int a,int b)
{
    int k=muld[abs(a)-1][abs(b)-1];
    return (a>0?1:-1)*(b>0?1:-1)*k;
}
int ijk(char c)
{
    if (c=='i')
        return 2;
    else if (c=='j')
        return 3;
    else
        return 4;

}
string s;
int calc(int l,int r)
{
    int now=1;
    For(i,l,r)
        now=mul(now,ijk(s[i]));
    return now;
}

int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    int ta;
    cin>>ta;
    For(tz,1,ta)
    {
        int L,X;
        cin>>L>>X;
        string sk;
        cin>>sk;
        s=' ';
        For(i,1,X)
            Rep(j,sk.size())
                s+=sk[j];
        int n=L*X;
        string ans="NO";
        if (calc(1,n)==-1)
        For(i,1,n)
        {
            if (calc(1,i)==2)
            {
                int now=1;
                For(j,i+1,n)
                {

                    now=mul(now,ijk(s[j]));
                    if (now==3)
                    {
                        ans="YES";
                        break;
                    }
                }
            }
//            For(j,i+1,n)
//            {
//                if (calc(1,i)==2 && calc(i+1,j)==3 && calc(j+1,n)==4)
//                    ans="YES";
//            }
        }
        printf("Case #%d: ",tz);
        cout<<ans<<endl;
    }
}
