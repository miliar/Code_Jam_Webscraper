#include<iostream>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<set>
#include<map>
#include<utility>
#include<climits>
 
#define unsigned long long int ulli
# define FRm(i, m, n)     for( int i = m; i <=n; i++)
# define FRrev(i, n)         for( int i = n; i >= 0; i-- )
# define FRrevm(i,n,m)         for( int i = n; i >= m; i-- )
#define max(a,b) ((a)>(b)?(a):(b))
#define S(a) scanf("%d",&(a))
#define P(a) printf("%d",(a))
#define min(a,b) ((a)<(b)?(a):(b))
#define NL printf("\n")
#define sqr(a) ((a)*(a))
#define SL(a) scanf("%lld",&(a))
#define PL(a) printf("%lld",(a))
#define lli long long int
#define FOR(I,A,B) for(int I= (A); I<(B); ++I)
#define inarrd(arr,n) for(int i=0;i<n;i++)S(arr[i]);
#define outarrd(arr,n) for(int i=0;i<n;i++){PFd(arr[i]);PF(" ");}NL;
#define outarrN(arr,n) for(int i=0;i<n;i++){PFd(arr[i]);PFN;}
using namespace std;
char s[6][7];
char temp[6][7];
int main(){
    int tc,cs=1,c,k1,k;
    char ch;
    bool flagX,flag0;
    S(tc);
    for(int i=0;i<6;i++){
        s[i][0]='Z';
        s[i][5]='Z';
    }
    for(int j=0;j<6;j++){
        s[0][j]='Z';
        s[5][j]='Z';
    }
    while(tc--){
        flagX=false;
        flag0=false;
        for(int i=0;i<4;i++)
            scanf("%s",temp[i]);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                s[i+1][j+1]=temp[i][j];
        /*for(int i=0;i<4;i++)
            cout<<temp[i]<<endl;
        for(int i=0;i<6;i++)
            printf("%s\n",s[i]);*/
        int dot=0;
        for(int i=1;i<5;i++){
            for(int j=1;j<5;j++){
                //cout<<"Xizzt\n";
                ch=s[i][j];
                if(ch=='.'){
                    dot++;
                    continue;
                }
                
                k=i+1;
                c=0;
                while(k<5){
                    if(s[k][j]==ch || s[k][j]=='T')
                        c++;
                    k++;
                }
                k=i-1;
                while(k>0){
                    if(s[k][j]==ch || s[k][j]=='T')
                        c++;
                    k--;
                }
                //cout<<c<<endl;
                if(c==3){
                    if(ch=='X')
                        flagX=true;
                    else
                        flag0=true;
                    break;
                }                
                c=0;
                k=j+1;
                while(k<5){
                    if(s[i][k]==ch || s[i][k]=='T')
                        c++;
                    k++;
                }
                k=j-1;
                while(k>0){
                    if(s[i][k]==ch || s[i][k]=='T')
                        c++;
                    k--;
                }
                //cout<<c<<endl;
                if(c==3){
                    if(ch=='X')
                        flagX=true;
                    else
                        flag0=true;
                    break;
                }
                k=i+1;
                k1=j+1;
                c=0;
                while(k<5 && k1<5){
                    if(s[k][k1]==ch || s[k][k1]=='T')
                        c++;
                    k++;
                    k1++;
                }
                k=i-1;
                k1=i-1;
                while(k>0 && k1>0){
                    if(s[k][k1]==ch || s[k][k1]=='T')
                        c++;
                    k--;
                    k1--;
                }
                //cout<<c<<endl;
                if(c==3){
                    if(ch=='X')
                        flagX=true;
                    else
                        flag0=true;
                    break;
                }
                
                k=i-1;
                k1=j+1;
                c=0;
                while(k>0 && k1<5){
                    if(s[k][k1]==ch || s[k][k1]=='T')
                        c++;
                    k--;
                    k1++;
                }
                k=i+1;
                k1=j-1;
                while(k<5 && k1>0){
                    if(s[k][k1]==ch || s[k][k1]=='T')
                        c++;
                    k++;
                    k1--;
                }
                //cout<<c<<endl;
                if(c==3){
                    if(ch=='X')
                        flagX=true;
                    else
                        flag0=true;
                    break;
                }
                
            }
            if(flagX || flag0)
                break;
        }
        if(flagX)
            printf("Case #%d: X won\n",cs++);
        else if(flag0)
            printf("Case #%d: O won\n",cs++);
        else if(dot)
            printf("Case #%d: Game has not completed\n",cs++);
        else
            printf("Case #%d: Draw\n",cs++);
        getchar();
        
    }
}