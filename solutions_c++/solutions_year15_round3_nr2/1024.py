#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <cstdlib>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <queue>
#include <vector>
#include <stack>
#include <list>
#include <cmath>
#include <ctime>
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<vi> vvi;
typedef long long int lli;

#define wez(n) int (n); scanf("%d",&(n));
#define wez2(n,m) int (n),(m); scanf("%d %d",&(n),&(m));
#define wez3(n,m,k) int (n),(m),(k); scanf("%d %d %d",&(n),&(m),&(k));
#define debug(vari) cout<<#vari<<" = "<<(vari)<<endl;
#define TESTS wez(testow)while(testow--)
#define modfun 1000000007
#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
#define INF 2147483647
#define REP(x,a,b) for(int (x) = (a);(x)<=(b);(x)++)
#define rep(x,n)   for(int (x)=0;(x)<(n);(x)++)
#define all(c) (c).begin(),(c).end()
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (fploind(all(c),x) != (c).end()) 
using namespace std;
int k,l,s;
string letters;
string target;
int maximumBananas;
double sumi=0;
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
int KMPSearch(string pat, string txt)
{
	int total=0;
    int M = pat.length();
    int N = txt.length(); 
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
      	total++;
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
    return total;
}
void solve(int cur,string done)
{
	if(cur==s)
	{
		int te=KMPSearch(target,done);
		sumi+=te;
		maximumBananas=max(te,maximumBananas);
    return;
	}
	for(int i=0;i<k;i++)
	{
		string temp;
		temp=done+letters[i];
		solve(cur+1,temp);
	}
}
int main()
{
  freopen("B-small-attempt0.in","r",stdin);
	int t;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
    sumi=0;
    maximumBananas=0;
		cin>>k>>l>>s;
		cin>>letters;
		cin>>target;
		solve(0,"");
		double tem=pow(k,s);
    // cout<<maximumBananas<<" "<<tem<<" "<<sumi<<endl;
		double te=maximumBananas-(sumi/tem);
		printf("Case #%d: %.6lf\n",test,te);
	}
	return 0;
}