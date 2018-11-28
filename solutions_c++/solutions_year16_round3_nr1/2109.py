/*  ------------------------------    header  -------------------------------------- */
#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;
//typedef long int li;
typedef unsigned long long int ulli;
#define ini(a, v)   memset(a, v, sizeof(a))
#define all(x)      (x).begin(), (x).end()
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define test() int t; cin>>t;while(t--)

#define si(x) scanf("%d",&x)
#define slli(x) scanf("%lld",&x)
#define sli(x) scanf("%ld",&x)
#define sd(x) scanf("%d",&x)

#define pfi(x) printf("%d\n",x)
#define pfli(x) printf("%ld\n",x)
#define pflli(x) printf("%lld\n",x)

#define abs(x) ((x)>0?(x):-(x))


#define TRI(a,b,c) mp(mp(a,b),c)

#define INDEX(arr,ind) (lower_bound(all(arr),ind)-arr.begin())
#define LB(a,x) (lower_bound(all(a),x)-a.begin()) //  first element in the range [first,last) which does not compare less than val.
#define UB(a,x) (upper_bound(all(a),x)-a.begin()) //  first element in the range [first,last) which compares greater than val.
#define all(x) x.begin(),x.end()
#define sz size()

#define rep(i,a,b) for(int  i=(a);i<(b);i++)
#define repl(i,a,b) for(lli  i=(a);i<(b);i++)
#define rrep(i,a,b) for(int i=(b);i>=(a);i--)
#define	foreach( gg,itit )	for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )

typedef pair<lli,lli> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;


/*  ------------------------------    header   end  -------------------------------------- */

/********************************************rem********************************/
//sort(child_time.begin(),child_time.end(),greater<int>()); reverse sort
/**********************************************rem end*****************************/

/*---------------------------------------- storage  start ---------------------------------------*/
int dx[]={1,-1,0,0};
int dy[]={0,0,-1,1};
lli  comb[1001][1001];
int vis[1000000];
list<int> li[1000000];
int lcp[5000][5000];
int is_palin[5000][5000];


 /*---------------------------------------- storage  end ---------------------------------------*/
 
 /*------------------------------------------ functions  start ------------------------------------*/
 
 lli gcd(lli a, lli b){ if(b)return gcd(b,a%b); return a;}
 
 inline void add(int &x, int y){x+=y; if(x>=mod)x-=mod; if(x<0)x+=mod;} // (a+b)%mod;
 int bc(int num)
{
 return __builtin_popcountll(num);
}
 
lli mulmod ( lli a , lli b,lli mod_val)  // (a*b)%c for large values of a and b 
{
	lli ret = 0;
	while(b)
	{
		if(b&1)
		{
			ret += a;
			if(ret >= mod_val)
				ret %= mod_val;
		}
		a = a + a;
		if(a >= mod_val) a %= mod_val;
		b >>= 1;
	}
	return ret;
}

/*lli   power(lli   x, lli  y,lli MOD)
{
    lli   temp;
    if( y == 0)
       return 1;
    temp = power(x, y/2);       
    if (y%2 == 0)
        return (temp*temp)%MOD;
    else
    {
        if(y > 0)
            return ((x*temp)%MOD*temp)%MOD;
        else
            return (temp*temp)/x;
    }
    
    
}  */

 long long int read_int()
 {
	char r;
	bool start=false,neg=false;
	long long int ret=0;
	while(true){
		r=getchar();
		if((r-'0'<0 || r-'0'>9) && r!='-' && !start){
			continue;
		}
		if((r-'0'<0 || r-'0'>9) && r!='-' && start){
			break;
		}
		if(start)ret*=10;
		start=true;
		if(r=='-')neg=true;
		else ret+=r-'0';
	}
	if(!neg)
		return ret;
	else
		return -ret;
}

/*inline void printint( long n)
{
	if(n == 0)
	{
		putchar_unlocked('0');
		putchar_unlocked('\n');
	}
	else if(n == -1)
	{
		putchar_unlocked('-');
		putchar_unlocked('1');
		putchar_unlocked('\n');
	}
	else
	{
		char buf[11];
		buf[10] = '\n';
		int i = 9;
		while(n)
		{
			buf[i--] = n % 10 + '0';
			n /= 10;
		}
		while(buf[i] != '\n')
			putchar_unlocked(buf[++i]);
	}
}	*/
 
 
 lli combination()
  {
  
  	for(int i = 0; i < 1000; i++) {
        comb[i][0] = 1;
        for(int j = 1; j <= i; j++)
            comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % mod;
    }
  
  }
  
  #define pp pair<pair<int,int>,int> 
bool compare(pp p1,pp p2)
 {
 	 if(p1.first.first<p2.first.first)return true;
 	 else if(p1.first.first>p2.first.first) return false;
 	 else
 	 {
 	 	 if(p1.first.second>p2.first.second) return true;
 	 	 else return false;
	  }
 	 
 }
int dfs(int index)
{
	 stack<int> s; s.push(index);  vis[index]=1;
	 while(!s.empty())
	  {
	  	 int index=s.top(); s.pop();
	  
	  	 list<int> :: iterator it;
	  	 for(it=li[index].begin();it!=li[index].end();it++)
	  	  {
	  	  	 if(!vis[*it] )
	  	  	  {
	  	  	  	 vis[*it]=1; s.push(*it);
			  }
		}
	  }	
}


lli lcm(lli a,lli b)
 {
 	 //cout<<" call "<<a<<" "<<b<<endl;
 	 map<int,int> v1,v2;
 	  int aa=a,bb=b;
 	  for(int i=2;i<=aa;i++)
 	   {
 	   	 int c=0;
 	   	  while(a%i==0)
 	   	   {
 	   	   	  c++;
 	   	   	  a/=i;
			   }
			   
			   if(c!=0)
			   v1[i]=c;
			   if(a==1) break;
		}
		
		
		for(int i=2;i<=bb;i++)
 	   {
 	   	 int c=0;
 	   	  while(b%i==0)
 	   	   {
 	   	   	 //cout<<"fact of "<<i<<endl;
 	   	   	  c++;
 	   	   	  b/=i;
			   }
			   
			   if(c!=0)
			   v2[i]=c;
			   if(b==1) break;
		}
		lli ret=1;
		map<int,int>::iterator it;
		for(it=v1.begin();it!=v1.end();it++)
		 {
		 	  int num=it->first;
		 	  int fact1=it->second;
		 	  int fact2=v2[num];
		 	  ret=ret*pow(num,max(fact1,fact2));
		 }
		//  cout<<ret<<endl;
		 	for(it=v2.begin();it!=v2.end();it++)
		 {
		 	  int num=it->first;
		 	   //cout<<"num"<<num<<endl;
		 	  int fact1=it->second;
		 	  int fact2=v1[num];
		 	  if(fact2==0)
		 	  ret=ret*pow(num,max(fact1,fact2));
		 }
		 // cout<<" re6 "<<ret<<endl;
		 return ret;
 }

int lcp_cal(string s1,string s2,int lcp[5000][5000])
 {
 	 int len1=s1.length();
 	 int len2=s2.length();
 	 
 	 for(int i=len1-1;i>=0;i--)
 	  {
 	  	 for (int j=len2-1;j>=0;j--)
 	  	  {
 	  	  	if(s1[i]==s2[j])
 	  	  	 {
 	  	  	 	 lcp[i][j]=lcp[i+1][j+1]+1;
				  }
				  else
				  {
				  	 lcp[i][j]=0;
				  }
			 }
	   }
 	   
 }

 
 lli  plaindrome (int start,int end,string s)
 {
 
 	  if(is_palin[start][end]!=-1) return is_palin[start][end];
 	  if(start>end) return -1;
 	  else
 	  {
 	  	
 	  	   if(s[start]==s[end])
 	  	    {
 	  	    	// cout<<" inside call "<<endl;
 	  	    	 
 	  	    	is_palin[start][end]=plaindrome(start+1,end-1,s);
 	  	    	 //cout<<
			   }
			   else 
			   is_palin[start][end]=-1;
			   return is_palin[start][end];
			   
	   }
	   
	   /* from main method  pest  this code
	   int len=s.length();
	  for(int i=0;i<len;i++) is_palin[i][i]=1;
	  for(int i=0;i<len-1;i++) if(s[i]==s[i+1]) is_palin[i][i+1]=1;
	  
	 
	  
	   for(int i=0;i<len;i++)
	   {
	   	 for(int j=i;j<len;j++)
	   	  {
	   	  	is_palin[i][j]=solve(i,j);
			 }
			
	   }*/
 }
  /*------------------------------------------ functions  end ------------------------------------*/
 
 /*

exponential power()
 {
}
void bfs()
{
 	
}
mst 
seg tree

 */
 /*---------------------------------------- main ------------------------------------*/

/*                    error check
1->varible range over flow 
2-> typecasting
3-> set  operation overflow
*/
#include<bits/stdc++.h>
using namespace std;

#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define ll long long int
#define pp pair<int,int> 
#define ve vector
#define mod 1000000007
#define debug 0
/************************************CODE BEGINS HERE************************/
int a[30];
int main()
{
            freopen("abc.txt","r",stdin);
            freopen("out1.txt","w",stdout);
              int tt=0;
			  int t;
			  cin>>t;
			  while(t--)
			  {
			  	if(debug)
			  	 {
			  	 	 cout<<" ok here ";
				   }
			  	   tt++;
			  	   int n;
			  	   cin>>n;
			  	   	if(debug)
			  	 {
			  	 	 cout<<" ok here ";
				   }
			  	   memset(a,0,sizeof(a));
			  	   for(int i=0;i<n;i++)
			  	   {
			  	   		if(debug)
			  	 {
			  	 	 cout<<" ok here ";
				   }
			  	   	  cin>>a[i];
			  	   	  
				   }
				   vector<string> res;
				while(1)
				{
						if(debug)
			  	 {
			  	 	 cout<<" ok here ";
				   }
					    int sum=0;
					     priority_queue<pair<int,int> > pq;
					    for(int i=0;i<n;i++)
					    {
					    		if(debug)
			  	 {
			  	 	 cout<<" ok here ";
				   }
					           sum+=a[i];	 
						}
					//	cout<<"sum "<<sum<<endl;
						if(sum==0)
						break;
						int mx=0;
							if(debug)
			  	 {
			  	 	 cout<<" ok here ";
				   }
						int pos1=-1;
						int pos2=-1;
							if(debug)
			  	 {
			  	 	 cout<<" ok here ";
				   }
						string temp="";
						for(int i=0;i<n;i++)
						{
								if(debug)
			  	 {
			  	 	 cout<<" ok here ";
				   }
						   	   if(a[i]>mx)
								  {
								  		if(debug)
			  	 {
			  	 	 cout<<" ok here ";
				   }
								  	 mx=a[i];
								  	 pos1=i;
								   } 
						}
						mx=0;
						for(int i=0;i<n;i++)
						{ 
						          if(i!=pos1 && a[i]>mx)
						          {
						          		if(debug)
			  	 {
			  	 	 cout<<" ok here ";
				   }
						          	  mx=a[i];
						          	  pos2=i;
								  }
						}
						a[pos1]--;
						a[pos2]--;
						mx=0;
						int tsum=0;
					//	cout<<"pos1 "<<pos1<<" "<<pos2<<endl;
						for(int i=0;i<n;i++)
						{
							if(debug)
			  	 {
			  	 	 cout<<" ok here ";
				   }
							
							   if(a[i]>mx)
							   mx=a[i];
							   tsum+=a[i];
							   if(debug)
			  	 {
			  	 	 cout<<" ok here ";
				   }
						}
						
					
					//	cout<<"left sum "<<tsum<<" "<<mx<<endl;
						
						if(mx>=(tsum/2)+1)
						{
					//		cout<<"haan "<<endl;
							    temp+=char('A'+pos1);
							    a[pos2]++;
							    res.pb(temp);
						}
						else
						{
							if(debug)
			  	 {
			  	 	 cout<<" ok here ";
				   }
							   temp+=char('A'+pos1);
							   temp+=char('A'+pos2);
							   res.pb(temp);
						}
				}
				cout<<"Case #"<<tt<<": ";
				int l=res.size();
				for(int i=0;i<l;i++)
				cout<<res[i]<<" ";
				cout<<endl;
			}	
			return 0;
}
