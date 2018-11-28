#include<cstdio>
#include<string>
#include<vector>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<cstdlib>
#include<cctype>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<fstream>
#include<numeric>
#include<map>
#include<sstream>
#include<iterator>
#define M 100
using namespace std;
typedef long long  ll;
bool test(string s, ll k)
{
    ll i,j,l=0;
    for(i=0;i<s.length();i++)
    {
        if(s.at(i)!='a'&&s.at(i)!='e'&&s.at(i)!='i'&&s.at(i)!='o'&&s.at(i)!='u')
        {
            l++;
        }
        else l=0;
        if(l==k) return true;
    }
    return false;
}
int main()
{
	freopen("D:\\in.txt","r",stdin);
	freopen("D:\\out.txt","w",stdout);
	string S,s,d,f;
	ll i,j,k,l,o,m,c=1;
	cin >> l;
	while(l--)
    {
        o=0;
        cin >>s >> m;
        k=m;
        for(i=0;i<=s.length()-k;i++)
        {
            j= k;
            while(k<=s.length()-i)
            {
                S.clear();

                S.insert(0,s,i,k);
             //   cout << S<<endl;
                if(test(S,m))o++;
                k++;
            }
            k=j;
        }
        printf("Case #%lld: %lld\n",c++,o);

    }
	return 0;
}
