//#include <bits/stdc++.h>
    #include <cstring>
    #include <vector>
    #include <list>
    #include <map>
    #include <set>
    #include <deque>
    #include <stack>
    #include <bitset>
    #include <algorithm>
    #include <functional>
    #include <numeric>
    #include <utility>
    #include <sstream>
    #include <iostream>
    #include <iomanip>
    #include <cstdio>
    #include <cmath>
    #include <cstdlib>
    #include <ctime>
    #include <memory.h>
    #include <cassert>
    #include <climits>
    using namespace std;
    //end of header files

    #define inf INT_MAX
    #define NO 100005

    #define F(i,a,b) for(int i=(a);i<(b);i++)
    #define RI(n) F(i,0,n)
    #define RJ(n) F(j,0,n)
    #define RK(n) F(k,0,n)

    #define MIN(a,b) ((a) < (b) ? (a) : (b))
    #define MAX(a,b) ((a) > (b) ? (a) : (b))

    #define Clear(a) memset(a,0,sizeof(a))              //clearing memory of an array
    #define setfalse(a) memset(a,false,sizeof(a))       //setting the array into false
    #define settrue(a) memset(a,true,sizeof(a))         //setting the array into true
    #define clrstr(a) memset(a,'\0',sizeof(a))          //setting string array to null

    #define open freopen("input.txt","r",stdin)         //opening input file
    #define close freopen ("output.txt","w",stdout)     //opening output file

    #define Case(a) printf("Case %d: ",a)               //printing case number
    #define caseh(a) printf("Case #%d: ",a)             //printing case number having '#'
    #define getcase(a) scanf("%d",&a)                   //scanning case number
    #define caseloop(a,b) for(a=1;a<=b;a++)  

    #define inp(n) scanf("%d",&n)
    #define inp2(n,m) scanf("%d%d",&n,&m)
    #define ins(s) scanf("%s",s)
    #define out(n) printf("%d\n",n)
    #define out2(n,m) printf("%d %d\n",n,m)

    #define inll(n) scanf("%I64d",&n)
    #define inll2(n,m) scanf("%I64d%I64d",&n,&m)
    #define outll(n) printf("%I64d\n",n)
    #define outll(n) printf("%I64d\n",n)
    #define outll2(n,m) printf("%I64d %I64d\n",n,m)
    #define int_bits __builtin_popcount
    #define ll_bits __builtin_popcountll

    #define take(ar,n) REP(n)cin>>ar[i] ;
    #define ctake(ar,n,br) REP(n){cin>>ar[i];br[i]=ar[i];}
    #define print(ar,n) REP(n)cout<<ar[i]<<" "; 
    
    typedef long long int LL;
    
    LL ans , no_of_persons ; 

    int n , ar[10000] ;
    char ch ; 

    int main(){
        
        //std::ios::sync_with_stdio(false);
        open; close;
        int tc ; 
        cin>>tc ; 

        F( test,1,tc+1 ){

            cin>>n ; 
            RI( n+1 ){

                cin>>ch ; 
                ar[ i ] = ch - '0' ;

            }

            no_of_persons = ans = 0 ;

            RI( n+1 ){

                if( ar[ i ] > 0 ){

                    if( no_of_persons < i ){

                        int temp = i - no_of_persons ;
                        ans += temp ;
                        no_of_persons += temp ;

                    }
                    no_of_persons += ar[ i ] ;

                }

            }
            
            caseh(test) ;
            cout<<ans<<endl ;
            
        }
        

        return 0  ;

    }
