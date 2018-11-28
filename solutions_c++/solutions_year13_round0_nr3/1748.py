#include <iostream>
#define TASK "C"
#define Small "-small-attempt"
#define NUM "0"


using namespace std;

int test;
long long a,b;
long long answer;
int cif[20];
int size;
long long all_pals[1000];

bool flag[10000002];

void readinput(){
    cin>>a>>b;        
}

long long calcAns(long long num)
{
    int cnt = 0;
    for (int i=0;i<size;i++){
        if (num>=all_pals[i]) cnt++;    
        else break;
    }
    return cnt;
}

void solve(){
    answer = calcAns(b)-calcAns(a-1);    
}

bool palindrome(long long c){
    int n = 0;
    while (c>0)
    {
        cif[n++]=c % 10LL;
        c/=10LL;        
    }        
    int l =0;
    int r = n-1;
    while (l<r)
    {
        if (cif[l]!=cif[r]) return false;
        l++;
        r--;
    }
    return true;
}

void precalc()
{
    size=0;    
    for (int i=1;i<=10000000;i++)
    {
        if (palindrome(i) && palindrome(((long long)i)*i))
        {
            all_pals[size++] = (((long long)i)*i);  
        }
    }        
}



void writeoutput(int t){
    printf("Case #%i: ",t+1);        
    cout<<answer<<endl;
}

int main(void){
    //freopen("input.txt","r",stdin);    
    //freopen(TASK""Small""NUM".in","r",stdin);
    freopen(TASK"-large-1.in","r",stdin);
    freopen("output.txt","w",stdout);
    
    precalc();
    /*for (int i=0;i<size;i++){
        cout<<all_pals[i]<<endl;    
    }*/
        
    scanf("%i\n",&test);
    for (int i=0;i<test;i++){
        readinput();
        solve();
        writeoutput(i);
    }
    
    return 0;    
}
