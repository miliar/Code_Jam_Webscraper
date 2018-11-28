#include <iostream>
#include <algorithm>
#define TASK "A"
#define Small "-small-attempt"
#define NUM "1"
#include <string>
#include <map>
#include <set>

using namespace std;

int test;
int n;
int marktest;
int a,answer;
int b[200];

void readinput(){
    scanf("%i%i",&a,&n);
    for (int i=0;i<n;i++)
    {
        scanf("%i",&b[i]);    
    }
}


long long Calc(long long A,int m){
        int num = 1<<m;
        long long BB = ((long long)(num))*(A-1)+1LL;
        return BB;
}

void solve(){
    sort(b,b+n);
    marktest++;
    answer = n;
    int cnt = 0;
    
    long long A = a;
    for (int i=0;i<n;i++){
        if (answer>cnt+n-i){
            answer = cnt+n-i;    
        }
        int l = -1;
        int r = 22;    
        while (r-l>1){
            int m=(l+r)/2;    
            long long BB = Calc(A, m);
            
            if (BB>b[i]) r=m;
            else l = m;
        }
        //cout<<"old A = "<<A<<" b = "<<b[i]<<endl;
        
        cnt+=r;
        A = Calc(A,r)+b[i];
        //cout<<"new A = "<<A<<" pow = "<<r<<endl;
        //cout<<endl;
    }
    if (answer>cnt){
        answer = cnt;    
    }
}

void writeoutput(int t){
    printf("Case #%i: ",t+1);        
    printf("%i\n",answer);
}

int main(void){
    //freopen("input.txt","r",stdin);    
    freopen(TASK""Small""NUM".in","r",stdin);
    //freopen(TASK"-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%i\n",&test);
    marktest=0;
    for (int i=0;i<test;i++){
        readinput();
        solve();
        writeoutput(i);
    }
    
    return 0;    
}
