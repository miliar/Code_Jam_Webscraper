#include <iostream>
#define TASK "B"
#define Small "-small-attempt"
#define NUM "1"
#include <string>
#include <deque>

using namespace std;

int test;
int n,m;
int c[101][101];
int used[101][101];
int answer;
deque<int> X;
deque<int> Y;

int dx[8] = { 0,-1, 1, 0, 1,-1,-1, 1};
int dy[8] = {-1, 0, 0, 1,-1, 1,-1, 1};


void readinput(){
    scanf("%i %i",&n,&m);
    for (int i=0;i<n;i++)
    {
        for (int j=0;j<m;j++){
            scanf("%i",&c[i][j]);
            used[i][j]=0;   
        }   
    }    
}

void solve(){
    answer = 1;   
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++) used[i][j]=100;                
    }
    for (int i=0;i<n;i++){
        int maxnum = c[i][0];
        for (int j=0;j<m;j++)
        {        
            maxnum=max(maxnum,c[i][j]); 
        }
        for (int j=0;j<m;j++)
        {        
            used[i][j]=min(maxnum,used[i][j]);
        }                
    }
    for (int j=0;j<m;j++){
        int maxnum = c[0][j];
        for (int i=0;i<n;i++)
        {
            maxnum=max(c[i][j],maxnum); 
        }                
        for (int i=0;i<n;i++)
        {
            used[i][j]=min(used[i][j],maxnum); 
        } 
    }
    for (int i=0;i<n;i++)
    {
        for (int j=0;j<m;j++)
        {
            if (used[i][j]!=c[i][j]) answer = 0;        
            //printf("%i ",used[i][j]);
        }    
        //printf("\n");
    }
    //printf("\n");

}

void writeoutput(int t){
    printf("Case #%i: ",t+1);        
    if (answer) printf("YES\n");
    else printf("NO\n");
}

int main(void){
    //freopen("input.txt","r",stdin);    
    //freopen(TASK""Small""NUM".in","r",stdin);
    freopen(TASK"-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%i\n",&test);
    for (int i=0;i<test;i++){
        readinput();
        solve();
        writeoutput(i);
    }
    
    return 0;    
}
