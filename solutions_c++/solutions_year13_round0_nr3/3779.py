#include <cstdlib>
#include <stdio.h>
#include <cstring>
#include <math.h>
#include <iostream>
//#include <vector>
#include <fstream>
#define REP(i,n) for(int i=0;i<(n);++i)
#define ZERO(x) memset(x,0,sizeof(x))
typedef long long LL;
using namespace std;
//std::vector<bool> palin ;

//LL storinglimit;
bool ispalindrome(LL n){
    
    int size=0;
    LL revdev=1;
    
    for(;n/revdev!=0;size++){

        revdev*=10;}
    revdev=revdev/10;
    if(size==1)
        return true;

    for( ;revdev>1;){
        if((n/revdev)-10*(n/revdev/10)!= n %10)
            return false;
        n=n/10;
        revdev/=100;
    }
    return true;
}
bool issquare(LL n){
    long double d_sqrt = sqrt( n );
LL i_sqrt = d_sqrt;
if ( d_sqrt == i_sqrt )
    return true;
else return false;
}
//bool isitfairsquare2(LL n){
//    if(n==1)return true;
//    bool sq =issquare(n);
//    bool rootpal=false;
//    LL root;
//    
//    if(sq){root=sqrt(n);
//        rootpal= palin.front();
//        palin.erase (palin.begin());
//        
//    //printf("no is %llu and deleted root palin?%d\n",n,(rootpal?1:0));
//    }
//    if(n>storinglimit && (!rootpal)){
//        return false;
//    }
//    //else part
//    bool pali= ispalindrome(n);
//    palin.push_back(pali);
//    if(pali && rootpal)
//        return true;
//    else return false;
//    
//}
bool isitfairsquare(LL n){
    if(n==1)return true;
    LL root;
    
    if(issquare(n)){
        if(ispalindrome(n)){
            root=sqrt(n);
            if(ispalindrome(root))
                return true;
        }
        
    //printf("no is %llu and deleted root palin?%d\n",n,(rootpal?1:0));
    }
    else return false;
    
}
int main() {
    LL A; 
    LL B;
   
//    palin.clear();
    int T;
    int ii=1;
    ofstream myfile;
    myfile.open ("/home/ds/codes/output.txt");
    scanf("%d",&T);
    while(ii<=T){
        int count=0;
        scanf("%llu",&A);
        scanf("%llu",&B);
  //      storinglimit = (sqrt(B));
        
        for(LL i=A; i<=B;i++){
            if(isitfairsquare(i) && i>=A)
                count++;
        }
        myfile << "Case #"<<ii++<<": "<<count<<endl;
        //printf("",ii++,count);
    }
    myfile.close();
    return 0;
}

