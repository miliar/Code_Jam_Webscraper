#include <iostream>
#include <algorithm>
#define TASK "B"
#define Small "-small-attempt"
#define NUM "0"
#include <string>
#include <map>
#include <set>

using namespace std;

int test;
int n;
long long p;
long long X,Y;

void readinput(){
    //scanf("%s %i\n",s,&n);
    //printf("!! %i\n",n);
    cin>>n>>p;
}

void solve(){
    {
    long long x = 1LL;    
    long long step = 1;
    for (int i=0;i<n;i++){
        x*=2LL;    
    }

    long long size = x;
    x=x-1LL;
    long long init = x;
    long long pos = x;
    while (p<=x)
    {
        //cout<<x<<" "<<size<<" "<<pos<<" "<<p<<endl;
        size=size/2LL;
        x-=step;
        step=step*2LL;
        pos = pos - size;
                    

    }
    //cout<<x<<" "<<size<<" "<<pos<<" "<<p<<" "<<step<<endl;
            
    X = (pos==init)?pos:pos+size-1LL;
    }   
    {
    long long x = 1LL;    
    long long step = 1LL;
    for (int i=0;i<n;i++){
        x*=2LL;    
    }

    long long size = x;
    x = 0;
    
    long long pos = 0;
    while (p>x)
    {
        size=size/2LL;
        x+=step;
        step=step*2LL;
        pos = pos + size;                    
    }        
    
    Y = (pos<p)?pos:pos-size;
    }   
}

void writeoutput(int t){
    printf("Case #%i: ",t+1);        
    //cout<<answer<<endl;
    cout<<X<<" "<<Y<<endl;;
}

int main(void){
    //freopen("input.txt","r",stdin);    
    //freopen(TASK""Small""NUM".in","r",stdin);
    freopen(TASK"-large.in","r",stdin);
    freopen("output2.txt","w",stdout);
        
    scanf("%i\n",&test);
        
    for (int i=0;i<test;i++){
        readinput();
        solve();
        writeoutput(i);
    }
    
    return 0;    
}
