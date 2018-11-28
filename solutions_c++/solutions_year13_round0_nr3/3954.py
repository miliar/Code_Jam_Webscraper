    //Other Includes
    #include<string>
    #include<iostream>
    #include<cstring>
    #include<cstdlib>
    #include<cstdio>
    #include<cmath>
    using namespace std;

    // Input macros
    #define s(n)                  scanf("%d",&n)
    #define sc(n)                 scanf("%c",&n)
    #define sl(n)                 scanf("%lld",&n)
    #define sf(n)                 scanf("%lf",&n)
    #define ss(n)                 scanf("%s",n)

	// Output Macros
	#define p(n)				  printf("%d\n",n)
	#define pnl					  printf("\n")

    // Useful constants
    #define INF                   (int)1e9
    #define EPS                   1e-9

    // Useful hardware instructions
    #define bitcount              __builtin_popcount
    #define gcd                   __gcd


    // Useful container manipulation / traversal macros
    #define forall(i,a,b)         for(int i=a;i<=b;i++)
    #define foreach(v, c)         for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
    #define all(a)                a.begin(), a.end()
    #define in(a,b)               ( (b).find(a) != (b).end())
    #define pb                    push_back
    #define fill(a,v)             memset(a, v, sizeof a)
    #define sz(a)                 ((int)(a.size()))
    #define mp                    make_pair


    // Some common useful functions
    #define checkbit(n,b)                ( (n >> b) & 1)
    #define DREP(a)                      sort(all(a)); a.erase(unique(all(a)),a.end())
    #define INDEX(arr,ind)               (lower_bound(all(arr),ind)-arr.begin())


    /*Main code begins now */
    int ispalin(int a,int *b)
    {
        if(a==0)
            return 1;
        if(ispalin(a/10,b) &&  (a%10 == ((*b)%10)  ) )
        {
             *b=(*b)/10;
            return 1;
        }
        else
            return 0;
    }
    int ispalindrome(int a)
    {
        if(a<0)
            return 0;
        return ispalin(a,&a);
    }
    bool isFairSquare(int n){
        int root = sqrt(n);
        if( (root*root)==n && ispalindrome(n) ){
            return true;
        }
        return false;
    }

    int solve(){
        int a,b,cnt=0;;
        cin>>a>>b;
        forall(i,a,b){
            if(isFairSquare(i) && ispalindrome(sqrt(i))){
                cnt++;
            }
        }
        return cnt;
	}
    int main()
    {
    	int tcase,i=0;
		scanf("%d",&tcase);
		while(i<tcase){
            i++;
            printf("Case #%d: %d\n",i,solve());
        }
    return 0;
    }
