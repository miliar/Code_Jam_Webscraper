#include <bits/stdc++.h>
 using namespace std;
#define pb push_back
#define m_p make_pair
#define F first
#define S second
#define For(i,a,b) for(long long int i=a;i<b;i++)
#define Fore(i,a,b) for(long long int i=a;i<=b;i++)
#define rFor(i,a,b) for(long long int i=a;i>b;i--)
#define rFore(i,a,b) for(long long int i=a;i>=b;i--)
#define tr(it,a) for(__typeof((a).begin()) it=(a).begin();it!=(a).end();it++)
#define all(a) a.begin(),a.end()
#define mem(a,b) memset(a,b,sizeof(a))
typedef long long int lli;
typedef pair<int,int> pii;
typedef pair<int,pii> pi3;
typedef pair<pii,pii> pi4;
typedef vector<int> vi;
typedef vector<pii> vpii;
void sc(int& a){scanf("%d",&a);}
void sc(lli& a){scanf("%lld",&a);}
void sc(int& a,int& b){sc(a);sc(b);}
void sc(lli& a,lli& b){sc(a);sc(b);}
void sc(int& a,int& b,int& c){sc(a,b);sc(c);}
void sc(lli& a,lli& b,lli& c){sc(a,b);sc(c);}
void prl(int a){printf("%d\n",a);}
void prl(lli a){printf("%lld\n",a);}
void prl(){printf("\n");}
void prs( int a){printf("%d ",a);}
void prs(lli a){printf("%lld ",a);}
void prl(lli a, lli b){cout<<a<<" "<<b<<" "<<endl;}
void prl(lli a, lli b, lli c){cout<<a<<" "<<b<<" "<<c<<" "<<endl;}
void prl(lli a, lli b, lli c, lli d){cout<<a<<" "<<b<<" "<<c<<" "<<d<<endl;}
void prl(lli a, lli b, lli c, lli d, lli e){cout<<a<<" "<<b<<" "<<c<<" "<<d<<" "<<e<<endl;}
void prl(lli a, lli b, lli c, lli d, lli e, lli f){cout<<a<<" "<<b<<" "<<c<<" "<<d<<" "<<e<<" "<<f<<endl;}
long long int mod =1000000007;
lli modpow(lli a, lli b, lli mod){lli res=1;while(b>0){if(b&1)res=(res*a)%mod;a=(a*a)%mod;b=b/2;}return res%mod;}
lli pow(lli a, lli b){lli res=1;while(b>0){if(b&1)res=(res*a);a=(a*a);b=b/2;}return res;}
#define inf INT_MAX
#define linf LLONG_MAX
const long long int MAX = 65536;
long long int a[MAX];
typedef struct 
{
  char ss[17];
  long long int a[9];
}dataholder;

long long int indd  = 2;
bool IsPrime(long long int number)
{ // Given:   num an integer > 1
  // Returns: true if num is prime
  //      false otherwise.
  
  long long int i;
  long long int k =sqrt(number);
  k=k+5;
  for (i=2; i < k; i++)
  {
    if (number % i == 0)
    {
      indd = i;
      return false;
    }
  }
  
  return true;  
}
 int main() {
  long long int t;
  sc(t);
  char s[17];
  long long int k,n,l,p;
  long long int no,found,j;
  k=0;
  dataholder temp,final[500];
  while(t--){
    k++;
    // printf("here\n");
      
    found=0;
    sc(n,j);
    l=pow(2,n-1);
    if(l%2==0)
      l=l+1;
   For(i,0,n)
     s[i]='0';
     s[n]=0;
    long long int thiss;
    while(found < j)
    {  
      // printf("here\n");
       thiss=1;
       p=l;
       // prl(p);
       rFore(i,n-1,0){
       s[i]=p%2+'0';
       p=p/2; 
       }
       s[n]=0;
       // cout<<s<<endl;
       // printf("error\n");
       Fore(i,0,n)
         temp.ss[i]=s[i];

       Fore(i,2,10){
        no=0;
        For(pp,0,n){
          no=no*i+s[pp]-'0';
        }
         // prs(no);
        if(IsPrime(no)){
           // printf("error\n");
          thiss =0;
          break;
        }
          else{
            // prl(indd);
          temp.a[i-2]=indd;
          }
       }
       // printf("error\n");
       if(thiss){

        final[found++]=temp;
       }
       l = l+2;
    }
    printf("Case #%lld:\n",k); 
    For(i,0,j)
     {
      printf("%s ",final[i].ss );
      For(k,0,9)
       printf("%lld ",final[i].a[k] );
        printf("\n");
     }
  
  }
 
}  

