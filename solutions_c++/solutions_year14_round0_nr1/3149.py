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
    bool choosen[17];
    int choosen_first , choosen_second , first_arrangement[4][4] , second_arrangement[4][4] ;
    int ans , count ;

    FOR(i,1,tc+1){

        ans = 20 ; count = 0 ;
        FOR(j,0,17)choosen[j] = false;
        cin>>choosen_first;
        FOR( j,0,4 )FOR(k,0,4) cin>>first_arrangement[j][k];
        cin>>choosen_second;
        FOR( j,0,4 )FOR(k,0,4) cin>>second_arrangement[j][k];

        FOR(j,0,4)choosen[ first_arrangement[choosen_first - 1 ][ j ] ] = true;

        FOR(j,0,4){

            if( choosen[ second_arrangement[choosen_second - 1 ][ j ] ] ){
                
                ans = second_arrangement[choosen_second - 1 ][ j ];
                count++;

            }
            if( count > 1 ){

                break;

            }

        }

        if( count == 1 ){   // ans is possible

            Case(i);cout<<ans<<endl;

        }
        if( count == 0 ){

            Case(i);cout<<"Volunteer cheated!"<<endl;

        }

        if( count > 1 ){

            Case(i);cout<<"Bad magician!"<<endl;

        }

    }

    
    
    
    
    return 0;
}

