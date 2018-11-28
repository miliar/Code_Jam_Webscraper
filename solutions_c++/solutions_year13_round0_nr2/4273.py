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
  #define p(n)          printf("%d\n",n)
  #define pnl           printf("\n")

    // Useful constants
    #define INF                   (int)1e9
    #define EPS                   1e-9

    // Useful hardware instructions
    #define bitcount              __builtin_popcount
    #define gcd                   __gcd


    // Useful container manipulation / traversal macros
    #define forall(i,a,b)         for(int i=a;i<b;i++)
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


     int solve(){
        int N,M;
        cin>>N>>M;
        int b[N][M],a[N][M];
        forall(i,0,N){
            forall(j,0,M){
                cin>>b[i][j];
                a[i][j] = 100;
            }
        }

        forall(i,0,N){
            forall(j,0,M){
                int p = b[i][j];
                int rmax = b[i][j];
                for(int k=0;k<M;k++){
                    rmax =( rmax > b[i][k] ? rmax : b[i][k] );
                }
                int cmax = b[i][j];
                for(int k=0;k<N;k++){
                    cmax =( cmax > b[k][j] ? cmax : b[k][j] );
                }
                if(p < rmax && p < cmax){
                    return 0;
                }
            }
        }
    return 1;
  }
    int main()
    {
        int tcase,i=0;
        cin>>tcase;
        while(i<tcase){
            i++;
            cout<<"Case #"<<i<<": "<<( solve() ? "YES" : "NO" )<<"\n";
        }
    return 0;
    }