//never give up  try to code every time
#include<bits/stdc++.h>
#define s(a) scanf("%d",&a)
#define S(a)  scanf("%lld",&a)
#define p(a) puts("a")
#define loop(a) for(int i=0;i<a;i++)
#define mx(x,y) x>y?x:y
#define mn(x,y) x>y?y:x
#define lld long long
#define ld long
#define mod 1000000007
#define max 100005
#define pb(a)  push_back(a)
#define pp(a) pop_back(a)
#define code_lover int main
#define FOR(i,N) for(int i=0;i<(N);i++)
using namespace std;
lld base_ctr(string s,lld b)
{   lld sum=0;
	reverse(s.begin(),s.end());
	for(lld i=0;i<s.size();i++)
	  sum+=(s[i]-'0')*((lld)pow(b,i));
	for(int i=2;i<sqrt(sum);i++)
	   {
	   	if(sum%i==0)
	   	  return i;
	   }
	
}
lld base_c(string s,lld b)
{   lld sum=0;
	reverse(s.begin(),s.end());
	for(lld i=0;i<s.size();i++)
	  sum+=(s[i]-'0')*((lld)pow(b,i));
	return sum;
	
}
lld base(string s)
{ //lld sum=0;
	//reverse(s.begin(),s.end());
	
	//cout<<sum<<endl;
	lld ct;
	for(int j=2;j<=2;j++)
	{ct=0;
		lld sum=base_c(s,j);
	for(lld i=2;i<sqrt(sum);i++)
	  {
		 if(sum%i==0)
	        ct++;
       	        
	  }
	    if(ct==0) 
	     break;
	    }
	if(ct==0)
	  return 0;
	  else
	  return 1;	
}
int j;
vector<string>v;
inline void printall(char arr[], char temp[], int i, int k, int n) {
	if(i == k) {string s="";
		int ct=0;
		     for(int i=0;i<k;i++)
		     {  s+=temp[i];
		           
		           }
		           temp[i]='\0';
		           if(s[0]=='1'&&temp[s.size()-1]=='1')
		           {
		           	  if(base(s)==1)
		           	  {
		           	  	 // if(v.size()<j)
		           	  	   v.push_back(s);
						 }
		           	  
		           	  
				   }
 
		return;
	}
 
	FOR(p, n) {
		temp[i] = arr[p];
		printall(arr, temp, i+1, k, n);
	}
}
inline void solve(char arr[], int n, int k) {
 
	char temp[k];
	printall(arr, temp, 0, k, n);
}

code_lover()
{  freopen("C-small-attempt0.txt","r",stdin);
  //fclose (stdin);
 	freopen("3rdka.txt","w",stdout);
	int n,t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{   j=0;
	    cin>>n>>j;
	    char arr[] = {'0','1'};
	     int n1 = sizeof(arr)/sizeof(arr[0]);
		  solve(arr, n1,n);
		  printf("Case #%d:\n",i);
	    for(int i=0;i<100;i++)
	       cout<<v[i]<<" "<<base_ctr(v[i],2)<<" "<<base_ctr(v[i],3)<<" "<<base_ctr(v[i],4)<<" "<<base_ctr(v[i],5)<<" "<<base_ctr(v[i],6)<<" "<<base_ctr(v[i],7)<<" "<<base_ctr(v[i],8)<<" "<<base_ctr(v[i],9)<<" "<<base_ctr(v[i],10)<<endl;
	    v.clear();
	}
	
	
return 0;
}

