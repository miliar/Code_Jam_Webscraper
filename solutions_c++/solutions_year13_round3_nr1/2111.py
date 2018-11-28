using namespace std;
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<string>
#include<cstring>
#include<vector>
#include<stack>
#include<sstream>
#include<algorithm>
#include<cctype>
#include<list>
#include<set>
#include<set>
#include<map>
#include<queue>
#include<stack>
#define f(i,n) for(i=0;i<n;i++)
#define fr(i,n,x) for(i=x;i<=n;i++)
#define w(t) while(t--)
#define MAX(A,B) (A)>(B)?(A):(B)
#define MIN(A,B) (A)<(B)?(A):(B)
#define gcd(a,b)  { return (b==0)?a:gcd(b,a%b); }
#define lcm(a,b)  { return a*b/gcd(a,b);  }
#define  sc(a)   scanf("%lld\n",&a)
#define  p(a)   printf("%lld\n",&a)
#define  str(s)   cin>>s
#define  ps(s)     cout<<s<<endl
#define  print(s)  printf("%s\n",s.c_str())
#define lt(v,k) list<int>v[k]
#define ll long long
typedef vector<int> vi;
typedef pair<string,int> ps;
typedef pair<int,int>pi;
typedef vector<pi> vii;
typedef vector<vii> vvii;
//vvii G(2501);
//vi d(1000,100000000);


 long long a[1000001];
 //list<int> l[100001];
 /*
 class abc
 {
 long int v1;
 long int v2;
 string s;
 };
 abc arr[1000001];   */
 //long long  arr[1001][1001];


//int count_substrings(string,int,int,int);
int main()
{int t,n;
    char arr[6]={'a','e','i','o','u'};
freopen("C:\\Users\\dell\\Desktop\\input.txt","r",stdin)   ;
freopen("C:\\Users\\dell\\Desktop\\output.txt","w",stdout);
int p=1;
cin>>t;
w(t)
    
    {
              string s;
        int ans=0,i =0;
      cin>>s;
    
    cin>>n;
       // sc(n);
   
        int len=s.size();
   int k=len-n;
        
        
        
        for(i=0;i<=len;i++)
   {int  v,r,c=0,x=0;
   
    for(v=i;v<=len-n;v++){
        c=0;
		    while((s[v]=='a'||s[v]=='e'||s[v]=='i'||s[v]=='o'||s[v]=='u')&&v<=len-n)
            {
			    v++;		
		}
		c++;
		r=v+1;
		while(r<=v+n-1)
        {
			if(s[r]!='a'&&s[r]!='e'&&s[r]!='i'&& s[r]!='o'&&s[r]!='u')
				c++;
			else
				break;
		r++;
		
        }
	
		if(c==n){
			x++;
			x+=len-r;
			break;
		}
	}
  ans=ans+ x;           
        }
    
    
    
    
    
    
    
        
         cout<<"Case #"<<p<<": "<<ans<<endl;


p++;
        
    }
    return 0;
}

