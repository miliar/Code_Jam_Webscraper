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

    #define take(ar,n) RI(n)cin>>ar[i] ;
    #define ctake(ar,n,br) RI(n){cin>>ar[i];br[i]=ar[i];}
    #define print(ar,n) RI(n)cout<<ar[i]<<" "; 
    
    typedef long long int LL;
    
    bool descending(int a,int b){
        return a>b;
    }
    
    int solve( char ch[200] ){
        
        
            
    }

    int main(){
        
        open ; close ;
        int tc ;
        cin>>tc ; 
        
        char ch[2500] ; 

        F(test,1,tc+1){

            cin>>ch ; 
            int length = strlen( ch ) ; 
            int digitsPresent[ 30 ] ; 
            int digitsInAnswer[ 15 ] ; 

            RI( 15 ) digitsInAnswer[ i ] = 0 ;

            RI( 30 ) digitsPresent[ i ] = 0 ; 

            sort( ch , ch + length ) ; 
            
            RI( length ){

                digitsPresent[ ch[ i ] % int('A') ]++ ; 

            }

            int ntd = 0 ;
            if( digitsPresent[ 25 ] ){   //Z

                ntd = digitsPresent[ 25 ] ; 
                digitsPresent[ 25 ] = 0 ; 
                digitsPresent[ 4 ] -= ntd ; 
                digitsPresent[ 17 ] -= ntd ; 
                digitsPresent[ 14 ] -= ntd ;

                digitsInAnswer[ 0 ] += ntd ; 

            }
            if( digitsPresent[ 23 ] ){  //X

                ntd = digitsPresent[ 23 ] ; 
                digitsPresent[ 23 ] = 0 ; 
                digitsPresent[ 8 ] -= ntd ; 
                digitsPresent[ 18 ] -= ntd ; 

                digitsInAnswer[ 6 ] += ntd ;

            }
            if( digitsPresent[ 22 ] ){   //W

                ntd = digitsPresent[ 22 ] ; 
                digitsPresent[ 22 ] = 0 ; 
                digitsPresent[ 19 ] -= ntd ; 
                digitsPresent[ 14 ] -= ntd ; 
            
                digitsInAnswer[ 2 ] += ntd ;

            }
            if( digitsPresent[ 20 ] ){  // U

                ntd = digitsPresent[ 20 ] ; 
                digitsPresent[ 20 ] = 0 ; 
                digitsPresent[ 5 ] -= ntd ; 
                digitsPresent[ 17 ] -= ntd ; 
                digitsPresent[ 14 ] -= ntd ; 
                digitsInAnswer[ 4 ] += ntd ;

            }
            if( digitsPresent[ 6 ] ){  // G

                ntd = digitsPresent[ 6 ] ; 
                digitsPresent[ 6 ] = 0 ; 
                digitsPresent[ 4 ] -= ntd ; 
                digitsPresent[ 8 ] -= ntd ; 
                digitsPresent[ 7 ] -= ntd ; 
                digitsPresent[ 19 ] -= ntd ; 

                digitsInAnswer[ 8 ] += ntd ;

            }
            if( digitsPresent[ 14 ] ){  //O

                ntd = digitsPresent[ 14 ] ; 
                digitsPresent[ 14 ] = 0 ; 
                digitsPresent[ 13 ] -= ntd ; 
                digitsPresent[ 4 ] -= ntd ; 
            
                digitsInAnswer[ 1 ] += ntd ;

            }
            if( digitsPresent[ 5 ] ){  //F

                ntd = digitsPresent[ 5 ] ; 
                digitsPresent[ 5 ] = 0 ; 
                digitsPresent[ 8 ] -= ntd ; 
                digitsPresent[ 21 ] -= ntd ; 
                digitsPresent[ 4 ] -= ntd ; 
            
                digitsInAnswer[ 5 ] += ntd ;
                
            }
            if( digitsPresent[ 21 ] ){  //V

                ntd = digitsPresent[ 21 ] ; 
                digitsPresent[ 21 ] = 0 ; 
                digitsPresent[ 4 ] -= ntd ; 
                digitsPresent[ 4 ] -= ntd ; 
                digitsPresent[ 18 ] -= ntd ; 
                digitsPresent[ 13 ] -= ntd ; 

                digitsInAnswer[ 7 ] += ntd ;
                
            }
            if( digitsPresent[ 8 ] ){  //N

                ntd = digitsPresent[ 8 ] ; 
                digitsPresent[ 8 ] = 0 ; 
                digitsPresent[ 13 ] -= ntd ; 
                digitsPresent[ 13 ] -= ntd ; 
                digitsPresent[ 4 ] -= ntd ; 

                digitsInAnswer[ 9 ] += ntd ;
                
            }

            digitsInAnswer[3] += digitsPresent[ 19 ] ; 
            

            caseh( test );

            F( digit , 0 , 10 ){

                RI( digitsInAnswer[ digit ] ){

                    cout<<digit ; 

                }

            }
            cout<<endl ; 

        }
        
        //getchar() ;
        return 0  ;

    }


    
