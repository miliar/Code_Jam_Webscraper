// User :: lovelotus ( Prem Kamal )

//#include<bits/stdc++.h>
//#define _ ios_base::sync_with_stdio(0);cin.tie(0);

#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<climits>
#include<cassert>
#include<iostream>
#include<algorithm>
#include<string>
#include<utility>
#include<cctype>
#include<stack>
#include<queue>
#include<vector>
#include<map>
#include<set>
#include<deque>

#define lli long long int
#define ulli unsigned long long int
#define F first
#define S second
#define pii pair<int,int>
#define pip pair<int,pii>
#define pis pair<int,string>
#define pll pair<lli,lli>

using namespace std;

int myMin(int a, int b)
{
    return (a<b?a:b);
}

int myMax(int a, int b)
{
    return (a>b?a:b);
}
typedef std::multiset<int>::iterator mIt;
int  recDepth=0;
int findAns(multiset<int>s)
{
    recDepth++;
    if(recDepth>=9)
	{
		recDepth--;
		return 9;
	}
    int i;
    multiset<int>::iterator it;
    it=s.end();
    it--;
    int x=(*it);
    if(x<=3)
    {
        recDepth--;
        return x;
    }
    int ans=x;
    for(i=2;i<=x/2;i++)
    {
    	//printf("Entering loop\n");
    	//for(it=s.begin();it!=s.end();it++) printf("%d ",(*it)); printf("\n");
    	//scanf("%*d");
        it=s.end();
		it--;
		int x=(*it);
		int p=x;
        pair<mIt,mIt> pit = s.equal_range(p);
        int cnt1=distance( pit.first, pit.second );
        s.erase(p);
        //printf("%d %d\n",cnt1,s.size());
        int k=0;
        while(k<cnt1-1)
		{
			k++;
			s.insert(p);
		}
        s.insert(i);
        s.insert(x-i);
        //printf("%d ent : ",recDepth);
        //for(it=s.begin();it!=s.end();it++) printf("%d ",(*it)); printf("\n");
        int val= findAns(s);
        ans=myMin(ans,val+1);

		//printf("%d ret : ",recDepth);
        //for(it=s.begin();it!=s.end();it++) printf("%d ",(*it)); printf("\n");

        pit = s.equal_range(i);
        cnt1=distance( pit.first, pit.second );
        //printf("2. <> %d %d\n",(*it),cnt1);
        s.erase(i);
        //printf("after erasing : %d\n",s.size());
        k=0;
        while(k<cnt1-1)
		{
			k++;
			s.insert(i);
		}

        pit = s.equal_range(x-i);
        cnt1=distance( pit.first, pit.second );
        //printf("3. <> %d %d\n",(*it),cnt1);
        s.erase(x-i);
        //printf("after erasing : %d\n",s.size());
        k=0;
        while(k<cnt1-1)
		{
			k++;
			s.insert(x-i);
		}
        s.insert(p);
        //printf("Exiting loop\n");
        //for(it=s.begin();it!=s.end();it++) printf("%d ",(*it)); printf("\n");
        //printf("--%d\n",s.size());
    }
    recDepth--;
    return ans;
}

int main()
{
    freopen("C:\\Users\\lovelotus\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\lovelotus\\Desktop\\output.txt","w",stdout);
    int i,j,t,x,n;
    multiset<int>st;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        st.clear();
        scanf("%d",&n);
        for(j=0;j<n;j++)
        {
            scanf("%d",&x);
            st.insert(x);
        }
        printf("Case #%d: %d\n",i,findAns(st));
    }
    return 0;
}
