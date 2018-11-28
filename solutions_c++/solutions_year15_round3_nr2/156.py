#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<vector>
#include<cstring>
#include<cstdlib>
#include<queue>
#include <iomanip>
#define ll long long int
#define mk make_pair
#define pb push_back
#define mod 1000000007
using namespace std;

struct comp
{
    bool operator() (const pair<int ,int > &p1 , const pair<int , int > &p2) const
    {
        if(p1.first<p2.first)
            return true;
        if(p1.first==p2.first&&p1.second<p2.second)
            return true;
        return false;
    }
};

void computeLPSArray(string pat, int M, int *lps);

int KMPSearch(string pat, string txt)
{
    int ans=0;
    int M = pat.length();
    int N = txt.length();

    // create lps[] that will hold the longest prefix suffix values for pattern
    int *lps = (int *)malloc(sizeof(int)*M);
    int j  = 0;  // index for pat[]

    // Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps);

    int i = 0;  // index for txt[]
    while (i < N)
    {
      if (pat[j] == txt[i])
      {
        j++;
        i++;
      }

      if (j == M)
      {
        ans++;
        j = lps[j-1];
      }

      // mismatch after j matches
      else if (i < N && pat[j] != txt[i])
      {
        // Do not match lps[0..lps[j-1]] characters,
        // they will match anyway
        if (j != 0)
         j = lps[j-1];
        else
         i = i+1;
      }
    }
    free(lps); // to avoid memory leak
    return ans;
}

void computeLPSArray(string pat, int M, int *lps)
{
    int len = 0;  // lenght of the previous longest prefix suffix
    int i;

    lps[0] = 0; // lps[0] is always 0
    i = 1;

    // the loop calculates lps[i] for i = 1 to M-1
    while (i < M)
    {
       if (pat[i] == pat[len])
       {
         len++;
         lps[i] = len;
         i++;
       }
       else // (pat[i] != pat[len])
       {
         if (len != 0)
         {
           // This is tricky. Consider the example AAACAAAA and i = 7.
           len = lps[len-1];

           // Also, note that we do not increment i here
         }
         else // if (len == 0)
         {
           lps[i] = 0;
           i++;
         }
       }
    }
}


int main()
{
    int t,w=1,n;
    freopen("input.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        ll i,j,k,l,r,c,n,m,o;
        string s,a;
        cin>>n>>m>>o;
        cin>>s>>a;
        queue<string> q;
        vector<string> vec;
        q.push("");
        while(!q.empty())
        {
            string p=q.front();
            if(p.length()==o)
                break;
            q.pop();
            for(i=0;i<n;i++)
                q.push(p+s[i]);
        }
        while(!q.empty())
        {
            string p=q.front();
            q.pop();
            vec.pb(p);
        }
        l=vec.size();
        double ans=0;
        int ma=0;
        for(i=0;i<l;i++)
        {
            int temp=KMPSearch(a,vec[i]);
            ans+=temp;
            ma=max(ma,temp);
        }
        ans=ma-(ans*1.0000)/l;
        cout<<"Case #"<<w<<": ";
        cout<<std::fixed;
        cout<<std::setprecision(9);
        cout<<ans<<"\n";
        w++;
        n++;
    }
    return 0;
}
