/*    ironstark    */
#include<bits/stdc++.h>
#define pii pair<int,int>
#define fi first
#define se second
#define mp make_pair
#define vpi vector< pii >
#define pb push_back
#define ll long long int
#define mod 1000000007
#define gcd(a,b) __gcd(a,b)
#define sf(n) scanf("%lld",&(n))
#define pf(n) printf("%lld\n",(n))
#define setbits(n) __builtin_popcount((n))
#define pq priority_queue
using namespace std;
ifstream fin ("A-small-attempt1.in");
ofstream fout ("out1.txt");
int main()
{
	int t;
	fin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		string s;
		fin>>s;
		int l=s.length();
		int fin_ans=0;
		int no_zero=0;
		sort(s.begin(),s.end());
		string arr[]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
		for(int i=0;i<=10000000;i++)
        {
            int k=i;

            string ans;
            while(k>0)
            {
                int r=k%10;
                ans+=arr[r];
                k/=10;
            }
            int l1=ans.length();
            bool flag1=false;
            int co=(l-l1)/4;
            if(l1<l)
            {
                if((l-l1)%4==0)
                {

                    for(int kk=0;kk<co;kk++)
                    {
                        ans+="ZERO";
                        flag1=true;
                    }
                }
            }
            l1=ans.length();
            if(l1==l)
            {
                sort(ans.begin(),ans.end());
                if(ans==s)
                {
                    if(flag1==true)
                    {
                     no_zero=co;
                    }
                    fin_ans=i;
                    break;
                }
            }

        }
        int k=fin_ans;
        int ind=0;
        int arr1[10];
        for(int i=0;i<no_zero;i++)
        {
            arr1[ind++]=0;
        }
        while(k>0)
        {
            int r=k%10;
            arr1[ind++]=r;
            k/=10;
        }
        sort(arr1,arr1+ind);
        fout<<"Case "<<"#"<<tc<<": ";
        for(int i=0;i<ind;i++)
            fout<<arr1[i];
        fout<<"\n";
	}
}
