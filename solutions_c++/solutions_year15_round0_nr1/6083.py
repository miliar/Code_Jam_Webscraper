#include<bits/stdc++.h>

using namespace std;
typedef long long ll  ;


int main()
{
    freopen("A-large.in","rt",stdin);
    freopen("bin.out","wt",stdout);

    int t , s , cnt = 1 ;
    cin>>t  ;
    string str ;
    while(t--)
    {
        cin>>s>>str ;
        int ans = 0 , cntPersons = 0 ;
        for(int i=0;i<s+1;i++)
        {
            int num = str[i]-'0' ;
            if(i==0)
                cntPersons+=num ;
            else
            {
                if(i>cntPersons)
                {
                    ans+=(i-cntPersons);
                    cntPersons+=(i-cntPersons) ;
                    cntPersons+=num ;
                }
                else
                {
                    cntPersons+=num ;
                }
            }
        }
        printf("Case #%d: %d\n" , cnt , ans) ;
        cnt++ ;
    }

}
