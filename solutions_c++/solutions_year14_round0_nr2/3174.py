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
    
    openInput; openOutput;
    int tc;
    cin>>tc;
    double C , F , X , min_time , count1 , count2 , ans , rate ; 


    FOR(test,1,tc+1){

        cin>>C>>F>>X;
        count1 = 0;count2 = 0 ; rate = 2.0 ; ans = inf;
        min_time = X/rate;

        while(true){
                    
            count2 = count1 + X/rate;       //complete the X 
            count1 += ( C/rate  );         //buy Farm 
            
            ans = MIN( ans , count2 );  // update the ans;
            if( count1 > ans ){        //don not buy more farms 
                
                    break;
                
            }    
            rate += F;
            //update the ans;
            //cout<<"buying room: "<<count1<<" not buying room "<<count2<<endl;
            //if(count1 >= min_time)break;
            //if( count1>count2 )break;
            //rate += F;
            //count1 -= X/(rate);

        }
        Case(test);printf("%0.20f\n",ans);

    }
    
    return 0;
}

