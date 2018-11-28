/***********************

Shubham Singhal

CodeChef - torque
HackerEarth - torque
SPOJ - torque
HackerRank - torquecode
CodeForces - torquecode
***********************/

// If Tyrion dies, I am gonna riot :P


# include <bits/stdc++.h>
using namespace std;

# define MOD         1000000007
# define gc          getchar
# define LL          long long
# define L           long
# define pb          push_back
# define pINF        999999
# define nINF        -999999
# define printi(x)   printf("%d",&x);
# define printli(x)  printf("%ld",&x);
# define printlli(x) printf("%lld",&x);
# define mp          make_pair
# define vi          vector<int>
# define MAXN        150005
# define INF         1e9

template<class T>
void scanint(T &x)
{
    register T c = gc();
    x = 0;
    T neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

 

int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;++t)
	{
	    string s;
	    int a[26]={0},c[10]={0};
		cin>>s;
		int len=s.length();
		for(int i=0;i<len;++i)
		{
			a[s[i]-'A']++;
			if(s[i]=='G')c[8]++;
			if(s[i]=='U')c[4]++;
			if(s[i]=='X')c[6]++;
			if(s[i]=='W')c[2]++;
			if(s[i]=='Z')c[0]++;
			
		}
		c[3]=a['T'-'A']-c[2]-c[8];
		c[7]=a['S'-'A']-c[6];
		c[5]=a['V'-'A']-c[7];
		c[9]=a['I'-'A']-c[8]-c[6]-c[5];
		c[1]=a['O'-'A']-c[2]-c[0]-c[4];
		cout<<"Case #" <<t<<": ";
		for(int i=0;i<10;++i)
		{
		    while(c[i]--)
			{
			    cout<<i;
			}
		}
		cout<<endl;
	}
	return 0;
}

// Can a man still be brave if he's afraid?  That is the only time a man can be brave !!
