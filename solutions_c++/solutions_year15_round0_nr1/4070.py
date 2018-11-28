#include <bits/stdc++.h>
using namespace std;

#define FOR(p,star,end) for(int p = star ; p<end ; p++)
#define FORR(p,star,end) for(int p = star ; p>=end ; p--)
#define INF 1000000000
#define MOD 1000000007
#define MAX 2097152

#define pii pair<int ,int >
#define vi vector<int>
#define vii vector< pair<int ,int> >
#define pb push_back
#define mp make_pair
#define ll long long


int main()

{

    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    scanf("%d",&t);



    FOR(tc,1,t+1)
    {


        int S;
        string str;
        cin >> S >> str;
        int res= 0 ;
        int sum = str[0]-'0';
        if(str[0]=='0')
            res++;
        else
            res+=(int)(str[0]-'0');

        FOR(i,1,str.size())
        {

            sum +=str[i]-'0';

            if(str[i]>'0')
            {
                if(res<i)
                    res+=abs(i-res);

                res+=(int)(str[i]-'0');

            }



        }

        printf("Case #%d: %d\n",tc,(res-sum) ) ;
    }


    return 0 ;

}
