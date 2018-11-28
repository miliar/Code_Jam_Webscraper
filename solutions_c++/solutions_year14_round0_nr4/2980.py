    #include<iostream>
    #include<cstdio>
    #include<algorithm>
    #include<vector>
    #include<list>
    #include<stack>
    #include<set>
    #include<map>
    #include<cmath>
    #include<cstring>
    #include<ctime>
    #include<assert.h>
    using namespace std;

    //end of header files
    #define inf 1000000000
    #define MOD 1000000007
    #define FOR(i,a,b) for(int i=(a);i<(b);i++)
    #define REP(n) FOR(i,0,n)
    #define MIN(a,b) ((a) < (b) ? (a) : (b))
    #define MAX(a,b) ((a) > (b) ? (a) : (b))
    #define Clear(a) memset(a,0,sizeof(a))              //clearing memory of an array
    #define setfalse(a) memset(a,false,sizeof(a))       //setting the array into false
    #define settrue(a) memset(a,true,sizeof(a))         //setting the array into true
    #define clrstr(a) memset(a,'\0',sizeof(a))          //setting string array to null
    #define openInput freopen("input.txt","r",stdin)         //opening input file
    #define openOutput freopen ("output.txt","w",stdout)     //opening output file
    #define Case(a) printf("Case #%d: ",a)               //printing case number
    #define caseh(a) printf("Case #%d: ",a)             //printing case number having '#'
    #define getcase(a) scanf("%d",&a)                   //scanning case number
    #define caseloop(a,b) for(a=1;a<=b;a++)  
    typedef long long int LL;


int main()
{
    
    openInput;
    openOutput;
    int tc;
    cin>>tc;
    int n ; 
    bool visited[1000];

    FOR(test,1,tc+1){

        int count_decieved = 0 , count_war = 0 , n;
        cin>>n;
        double a1[n] , a2[n] , b1[n] , b2[n] ; 
        

        REP(n)cin>>a1[i];
        REP(n)cin>>b1[i];

        sort(a1,a1+n); 
        sort(b1,b1+n);
        REP(n){ b2[i] = b1[i] ; a2[i] = a1[i] ; }
        REP(n)visited[i] = false;

        FOR(i,0,n){

            FOR(j,0,n){

                if( !visited[j] && b1[j] < a1[i] ){

                    visited[j] = true;
                    count_decieved++;
                    break;

                }

            }

        }

        reverse(a2,a2+n);reverse(b2,b2+n);
        REP(n) visited[i] = false;
        int top = 0; 

        FOR(i,0,n){

            if( b2[top] > a2[i] ){

                top++;
                visited[top] = true;
                count_war++;

            }
            else{

                for(int j = n-1; j>=0 ; j--){

                    if(!visited[j]){

                        visited[j] = true;
                        break;

                    }

                }

            }

        }


        Case(test);cout<<count_decieved<<" "<<(n - count_war)<<endl;

    }
    
    return 0;
}

