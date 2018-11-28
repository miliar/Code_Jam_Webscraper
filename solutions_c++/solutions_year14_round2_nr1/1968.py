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
    int n;    
    char s1[105], s2[105];

    FOR(test,1,tc+1){

        cin>>n;
        cin>>s1>>s2;

        int i , j , counti , countj , ans = 0;
        i = j = 0;
        bool not_equal = false;

        while(true){
        
                
            if( s1[i] != s2[j] ){

                //printf("isme1if \n");
                not_equal = true;
                break;

            }
            else{

                //printf("else me \n");

                counti = countj = 1;
                while( i+1 < strlen(s1) && s1[i+1] == s1[i] ){counti++; i++;}
                while( j+1 < strlen(s2) && s2[j+1] == s2[j] ){countj++; j++;}
                i++;j++;
                //cout<<i<<"  "<<j<<endl;
                //cout<<counti<<" "<<countj<<endl;
                ans += abs( counti - countj );

                if( i == strlen(s1) && j == strlen(s2) ){

                    Case(test);printf("%d\n",ans);break;                    

                }
                else if( ( i == strlen(s1) && j != strlen(s2) ) || ( i != strlen(s1) && j == strlen(s2)  )  ){

                    not_equal = true;
                    break;

                }

            }

        }

        if(  not_equal ){

            Case(test); printf("Fegla Won\n");

        }
        

    }
    
    return 0;
}

