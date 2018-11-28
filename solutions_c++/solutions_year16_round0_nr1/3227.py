#include<iostream>
#include<stdio.h>
#include<vector>
#include<set>

using namespace std;
set<int> getndata(int val);
int main(){
    FILE *inf, *outf;
    inf=fopen("A-large.in","r");
    outf=fopen("A-large-result.in","w");
    
    int T,N;
    set<int> oset;
    set<int> nset;
    
    fscanf(inf,"%d",&T);
    for(int i=0;i<T;i++){
            int nowdata;
            int lastdata;
            fscanf(inf,"%d",&nowdata);
            
            oset.clear();
            nset.clear();
            
            int cnt = 1;
            if(nowdata==0)fprintf(outf,"Case #%d: INSOMNIA\n",i+1);
            else{
                while(true){
                            int nowval = cnt * nowdata;
                            set<int> nowset = getndata(nowval);
                            nset.insert(nowset.begin(),nowset.end());
                            cnt++;
                            if(nset.size()==10){
                                                lastdata=nowval;
                                                break;
                            }            
                }
                fprintf(outf,"Case #%d: %d\n",i+1,lastdata);
            }
            
    }
//    getchar();
}

set<int> getndata(int val){
            set<int> ret;
            int maxval = 1;
            int vallength = 1;
            int valdump = val;
            if(val==0){
                       ret.insert(0);
                       return ret;
            }
            while(maxval * 10 <= val){
                         vallength++;
                         maxval*=10;
            }
            for(int i=maxval;i>=1;i/=10){
                    ret.insert(valdump/i);
                    valdump = valdump - (valdump/i) * i;
            }
            return ret;
}
