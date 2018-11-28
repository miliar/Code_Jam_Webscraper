#include<bits/stdc++.h>
using namespace std;

#define p(n) printf("%d\n",n)
#define r(n) scanf("%d",&n)
#define rs(n) scanf("%s",n)
#define ps(n) printf("%s\n",n)
#define P printf
#define R scanf
#define F first
#define S second
#define fr(i,a,b) for(int i=(int)a; i <= (int)b; i++)
#define frr(i,a,b) for(int i=(int)a; i >= (int)b; i--)
#define ll long long int
#define pb push_back
#define vi vector<int>
#define ve(x) vector<x>
#define si set<int>
#define itv vi :: iterator
#define ixv(x) vector<x> :: iterator
#define its si :: iterator
#define ixs(x) set<x> :: iterator
#define fill(s,v) memset(s,v,sizeof(s))
#define all(s) s.begin(),s.end()
#define fs(i,s) for(its i = s.begin(); i != s.end(); i++)
#define fv(i,v) for(itv i = v.begin(); i != v.end(); i++)
#define INF INT_MAX
#define MOD 1000000007
#define ii pair<int,int>
#define mp make_pair

ll ipow(ll base, ll exp)
{
    ll result = 1;
    while (exp)
    {
        if (exp & 1)
            {result *= base;result %= MOD;}
        exp >>= 1;
        base *= base;
        base %= MOD;
    }
    return result;
}
int mx;
int ssp = 0;
int p[1001];
int calc(int diners, int mi , int mask)
{
    if(mi > mx){P("ans = %d\n",mx);return mx;}//{P("%d =  %d\n",mask,mx); return mx;}
    int temp = 1;
    fr(i,1,diners)
    {
        if(p[i] > p[temp]) temp = i;
    }
    int ind = 0;
    fr(i,1,diners)
    {
      if(p[i] == 0) ind = i;
      break;
    }
    if(p[temp] == 0)
        {
            //P("ans = %d\n",mi-1);
            return mi-1;}

    if(ind == 0) ind = diners+1;
    int ans = mx;
   /* fr(i,1,diners)
    {
        P("%d ",p[i]);
    }
    P("\n");*/
    if(p[temp] == 9)
    {
        int ans2 ,ans1;
        p[temp] = 3;
        p[ind] = 6;
        ans1 = calc(max(ind,diners),mi+1,mask|(1<<(mi-1)));
        p[temp] = 5;
        p[ind] = 4;
        ans2 = calc(max(ind,diners),mi+1,mask|(1<<(mi-1)));
        ans = min(ans,ans1);
        ans = min(ans,ans2);
        p[temp] = 9;
    }
    if(p[temp] == 6)
    {
        int ans2 ,ans1;
        p[temp] = 2;
        p[ind] = 4;
        ans1 = calc(max(ind,diners),mi+1,mask|(1<<(mi-1)));
        p[temp] = 3;
        p[ind] = 3;
        ans2 = calc(max(ind,diners),mi+1,mask|(1<<(mi-1)));
        ans = min(ans,ans1);
        ans = min(ans,ans2);
        p[temp] = 6;
    }
    else
    {
        int tt = p[temp];
        p[temp] = p[temp] - p[temp]/2;
        p[ind] = tt;
        ans = calc(max(ind,diners),mi+1,mask|(1<<(mi-1)));
        p[temp] = tt;
    }
    int pp[100];
    bool flag= true;
    fr(i,1,diners)
    {
        if(p[i] > 0)flag = false,p[i] -= 1, pp[i] = 1;
        else pp[i] = 0;
    }
    if(flag) return ans;
    ans = min(ans,calc(diners,mi+1,mask));
    fr(i,1,diners) p[i] += pp[i];
    return ans;
}

int solve2(int ps[100],int diners,int prex)
{
    int pre = 0;
    int pt[100];
    int di = diners;
    int ans = mx;
    if(prex >= mx) return 0;

    fr(i,1,diners)
    {
        P("%d ",ps[i]);
    }
    ps("");
    while(pre+prex <= mx)
    {
        pre++;
        int temp = 1;
        fr(i,1,di)
        {
            if(ps[i] > ps[temp]) temp = i;
        }
        fr(i,1,di)
        {
                pt[i] = ps[i];
        }
        if(ps[temp] == 9)
        {
            fr(i,1,di)
            {
                pt[i] = ps[i];
            }
            int ans2 ,ans1;
            pt[temp] = 4;
            pt[di+1] = 5;
            ans1 = solve2(pt,di+1,pre+prex);
            pt[temp] = 3;
            pt[di+1] = 6;
            ans2 = solve2(pt,di+1,pre+prex);
            ans = min(ans,ans1+pre);
            ans = min(ans,ans2+pre);
        }
        else if(ps[temp] == 6)
        {
            fr(i,1,di)
            {
                pt[i] = ps[i];
            }
            int ans2 ,ans1;
            pt[temp] = 2;
            pt[di+1] = 4;
            ans1 = solve2(pt,di+1,pre+prex);
            pt[temp] = 3;
            pt[di+1] = 3;
            ans2 = solve2(pt,di+1,pre+prex);
            ans = min(ans,ans1+pre);
            ans = min(ans,ans2+pre);
        }
        else
        {
            int ans1 = pre + ps[temp] - 1;
            ps[di+1] = ps[temp]/2;
            ps[temp] -= ps[di+1];
            int mxi = 1;
            fr(i,1,di+1)
            {
                if(ps[i] > ps[mxi]) mxi = i;
            }

            int ans2 = pre + ps[mxi] ;
            if(ans1 < ans2)
            {
                P("%d  %d   ",ans1,ans2);
                P("returning  %d  %d\n",min(ans,ans1),prex);
                return min(ans,ans1);
            }

            ans = min(ans,ans2);
        }
        di++;
    }
   // P("retun2  %d\n",ans);
    return ans;
}
int solve(int d)
{
    int pre = 0;
    int cnt[1001];
    int ans = mx;
    fill(cnt,0);
    fr(i,1,d) cnt[p[i]]++;
    int maxi = 1000;
    int maxi2 = 0;
    while(pre <= mx)
    {
        maxi2 = 0;
        int temp = 0;
        frr(i,maxi,1)
        {
            if(cnt[i] > 0)
            {
                temp = i;
                break;
            }
        }
        if(temp == 0) return ans;
        maxi  = temp;
        frr(i,maxi-1,1)
        {
            if(cnt[i] > 0)
            {
                maxi2 = i;
                break;
            }
        }
        int tempx;
        int val = maxi - maxi/2;
        tempx = val;
        if(tempx < maxi2) tempx = maxi2;
        if(maxi == 9 )
        {
            int ans1,ans2,a1,b1;
            tempx = max(3,maxi2);
            a1 = cnt[maxi]*2;
            b1 = cnt[maxi]*3;
            ans1 =pre+tempx+a1;
            tempx = max(val,maxi2);
            ans2  = pre+tempx + cnt[maxi];
            if(ans1 < ans2)
            {
                pre+= a1;
                cnt[3] += b1;
                ans = min(ans1,ans);
                cnt[maxi] = 0;
            }
            else
            {
                pre += cnt[maxi];
                cnt[maxi/2] += cnt[maxi];
                cnt[val] += cnt[maxi];
                ans = min(ans,ans2);
                cnt[maxi] = 0;
            }

            continue;
        }
        else if(maxi == 6)
        {
            int ans1,ans2;
            int a1,a2,b1,b2;
            tempx = max(2,maxi2);
            a1 = cnt[maxi]*2;
            b1 = cnt[maxi]*3;

            ans1 = min(ans,pre+tempx+a1);
            tempx = max(3,maxi2);
            a2 = cnt[maxi];
            b2 = cnt[maxi]*2;

            ans2 = min(ans,pre+tempx+a2);
            if(ans1 < ans2)
            {
                pre+= a1;
                cnt[2] += b1;
                ans = min(ans,ans1);
            }
            else
            {
                pre+= a2;
                cnt[3] += b2;
                ans = min(ans,ans2);
            }
            cnt[maxi] = 0;
            continue;
        }



        if(cnt[maxi] >= maxi - val)
            return ans;
        ans = min(ans,pre+tempx + cnt[maxi]);
        pre += cnt[maxi];
        cnt[maxi/2] += cnt[maxi];
        cnt[val] += cnt[maxi];
        cnt[maxi] = 0;
        /*int ans1 = pre+maxi;

        int ans2 = pre+cnt[maxi]+ tempx;
        pre += cnt[maxi];
        cnt[maxi/2] += cnt[maxi];
        cnt[val] += cnt[maxi];
        cnt[maxi] = 0;*/
       // P("pre = %d  %d  %d  %d  %d\n",pre,maxi,maxi2, ans1,ans2);
    }
    return ans;
}
main()
{
    int t, d;
    r(t);
    int k = 1;
    while(t--)
    {
        r(d);
        mx = 0;
        fr(i,1,d)
        {
            r(p[i]);
            if(mx < p[i]) mx = p[i];
        }
        int ans2 =solve2(p,d,0);
       //int ans = calc(d,1,0);

        P("Case #%d: %d\n",k,ans2);
        k++;
    }
    return 0;
}
