#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<algorithm>
#include<cmath>
#include<climits>
#include<queue>
#include<set>
#include<cstdio>

#define VI vector<int>
#define PII pair<int,int>
#define mp make_pair
#define rep(i,a,b) for(i=(a); i<(b); i++)
#define repI(i,a,b) for(i=(a); i<=(b); i++)

using namespace std;
typedef unsigned long long int ulli;
typedef long long int lli;

ulli T, Smax;
string S;

main()
{
    cin >> T;
    ulli i,j,len,cnt,res,val;
    repI(i,1,T)
    {
    	cin >> Smax;
    	getchar();
    	cin >> S;
    	len = S.size();
    	res = 0;   
        cnt = S[0]-'0';     
    	rep(j,1,len)
    	{
    		val = S[j]-'0';
            if (val > 0 && cnt>=j)
                cnt += val;
            else if(val > 0)
            {
                res += (j-cnt);
                cnt += (j-cnt)+val;
            }
            //cout << val << " " << cnt << " " << res << endl;
    	}
    	cout << "Case #" << i << ": " << res << endl;
    }
}

