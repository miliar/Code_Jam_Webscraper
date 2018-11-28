#include<iostream>
#include<cstdio>
#include<set>

using namespace std;

typedef long long ll; 

int main(){
	
	//freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);

    for(int tt=1;tt<=t;++tt){
        
        ll n,nn;
        set<int>st;

        scanf("%lld",&n);
        nn=n;
        
        if(!n){
            
            printf("Case #%d: INSOMNIA\n",tt);
            continue;
        }
        
        
        while(1){
            
            ll tmp=n;

            while(tmp){

                int d=tmp%10;
                st.insert(d);
                tmp/=10;

            }  
  
            if(st.size()==10)
                break;
            
            n+=nn;
        }        
        printf("Case #%d: %lld\n",tt,n);
    }


    return 0;


}
