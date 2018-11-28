#include<bits/stdc++.h>
using namespace std;
#define gc getchar_unlocked
int main(){
    freopen("in.txt","r+",stdin);
    freopen("out.txt","w+",stdout);
    ios_base::sync_with_stdio(false);
    int test,sm;
    string pd;
    cin>>test;
    for(int t=1;t<=test;t++){
        cin>>sm>>pd;
        int term=0,sum=0,ans=0;
        for(int i=0;i<=sm;i++){
            if(i=='0')
                sum+=(pd[i]-'0');
            else{
                if(pd[i]!='0'){
                    if(sum>=i){
                        sum+=(pd[i]-'0');
                    }
                    else{
                        if(i==4){
                            //cout<<"dk"<<endl;
                      //cout<<i<<" "<<ans<<" "<<sum<<" "<<pd[i]<<endl;
                        }
                        ans+=(i-sum);
                        term=(i-sum);
                        sum+=term;
                        sum+=(pd[i]-'0');
                        
                    }
                }
            }
            //cout<<i<<" "<<ans<<" "<<sum<<endl;
        }
        printf("Case #%d: %d\n",t,ans);
    }
      //#ifdef debug
    //fprintf(stdout,"\nTIME: %.3lf sec\n", (double)clock()/(CLOCKS_PER_SEC));  
    // #endif
    return 0;
}//end main
