#include <string> 
#include <vector> 
#include <map> 
#include <utility> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <queue> 
#include <stack> 
#include <set> 
#include <sstream> 
#include <algorithm> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
using namespace std; 
  
#define INF 0x3f3f3f3f
#define ALL(v) v.begin(),v.end() 
typedef pair<char,int> pci;
typedef long long ll;

bool isvowel(char x){
    return (x=='a'||x=='e'||x=='i'||x=='o'||x=='u');
}

char cstr[10000005];

int nvalue(string &s){
    int res=0,cons=0;
    for(int i=0;i<s.size();i++)
        if(isvowel(s[i])){
            res=max(res,cons);
            cons=0;      
        }else{
            cons++;
        }
    res=max(res,cons);
    return res;
}

int main(){
    int test;
    scanf("%d",&test);
        
    for(int tt=1;tt<=test;tt++){
        printf("Case #%d: ",tt);

        int n,nv;
        scanf("%s %d",cstr,&n);
        string s(cstr);
        long long res=0,incr=0;
        int cons=0;
        for(int i=0;i<s.size();i++){
            if(isvowel(s[i])){
                cons=0;            
            }else{
                cons++;
                if(cons>=n){
                    incr=i-n+2;
                }
            }
            res+=incr;        
        }

        printf("%lld",res);
        printf("\n");
    }

    return 0;
}
