#include<bits/stdc++.h>
    #include<string>
    using namespace std;
    template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
    template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
    #define traverse(container, it) \
      for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
    #define         mp(x, y) make_pair(x, y)
    #define         SIZE(c) (int)c.size()
    #define         pb(x) push_back(x)
    //#define       map<char,int>::iterator it;
    #define         ff first
    #define         ss second
    #define         ll long long
    #define         ld long double
    #define         pii pair< int, int >
    #define         psi pair< string, int >
    #define         p(n) printf("%d\n",n)
    #define         p64(n) printf("%lld\n",n)
    #define         s(n) scanf("%d",&n)
    #define         s64(n) scanf("%I64d",&n)
    #define         rep(i,a,b) for(i=a;i<b;i++)
    #define         MOD (1000000007LL)




    ///////////////////////////////////////////////////////

string str;

int k;

int arr[123456];
void solve(){
    int n=str.length();


    memset(arr,0,sizeof(arr));
    int i;
    rep(i,0,n){
        arr[i]=str[i]-'0';
    }

    int cnt=0;
    int pre=arr[0];
    rep(i,1,n){
        if(pre>=i)  pre+=arr[i];

        else{
            cnt+=i-pre;
            pre+=i-pre;
            pre+=arr[i];
        }



    }

    cout<<cnt<<endl;

}


int main(){
   //std::ios::sync_with_stdio(false);

    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    cin>>t;
    int num=1;
    while(t--){
        cin>>k;

        cin>>str;
        cout<<"Case #"<<num++<<": ";
        solve();

    }


return 0;

}
