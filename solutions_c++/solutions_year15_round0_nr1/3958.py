//Author : pakhandi
//
using namespace std;

#include<bits/stdc++.h>

#define wl(n) while(n--)
#define fl(i,a,b) for(i=a; i<b; i++)
#define rev(i,a,b) for(i=a; i>=b; i--)
#define scan(n) scanf("%d", &n)
#define scans(s) scanf("%s", s)
#define scanc(c) scanf("%c", &c)
#define scanp(f) scanf("%f", &f)
#define print(n) printf("%d\n", n)
#define prints(s) printf("%s\n", s)
#define printc(c) printf("%c\n", c)
#define printp(f) printf("%f\n", f)
#define nline printf("\n")
#define mclr(strn) strn.clear()
#define ignr cin.ignore()
#define MOD 1000000007
#define ll long long int
#define u64 unsigned long long int

#define PB push_back
#define SZ size
#define MP make_pair

int arr[1000006];

int main()
{
	freopen("input1.txt","r",stdin);
    freopen("output1.txt","w",stdout);
	int i, j, k;
	int n;
	string str1;
	int cases;
	cin>>cases;
	 k=1;

	while(cases--)
	{
		cin>>n>>str1;
		fl(i,0,n+1)
		{
			arr[i]=str1[i]-'0';
			//cout<<arr[i]<<" ";
		}

		int curr=0, ans=0;

		fl(i,0,n+1)
		{
			if(curr<i)
			{
				//curr+=arr[i];
				ans+=(i-curr);
				curr+=(i-curr);
				curr+=arr[i];
			}
			else
			{
				curr+=arr[i];
			}
		}
		cout<<"Case #"<<k++<<": "; 
		cout<<ans;
		nline;
	}
	return 0;
}