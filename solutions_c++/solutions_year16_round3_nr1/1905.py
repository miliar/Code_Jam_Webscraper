#include<iostream>
#include<stdio.h>
#include<vector>
#include<set>
#include<cstring>
#include<algorithm>
#include<string>

using namespace std;
int P[1001],N;
vector<string> ret;
char nowRetChar[100];
bool isOk;

void solve(int cnt)
{
    if(cnt==0){
        isOk=true;
        return;
    }
    for(int i=0;i<N;i++){
        if(isOk)break;
        for(int j=i;j<N;j++){
            int newCnt = cnt;
            if(P[i]>0&&P[j]>0){
                P[i]--;
                newCnt--;
                if(i!=j){
                    P[j]--;
                    newCnt--;
                }
                int maxVal=0;
                for(int k=0;k<N;k++){
                    maxVal=max(maxVal,P[k]);
                }
                if(maxVal*2>newCnt){
                    P[i]++;
                    if(i!=j){
                        P[j]++;
                    }
                    continue;
                }
                nowRetChar[0] = ('A'+i);
                nowRetChar[1] = '\0';
                if(i!=j){
                    nowRetChar[1] = ('A'+j);
                    nowRetChar[2] = '\0'; 
                }
                string nowRet(nowRetChar);
                ret.push_back(nowRet);
                solve(newCnt);
                if(isOk)break;
                ret.pop_back();
                P[i]++;
                if(i!=j){
                    P[j]++;
                }

            }
        }
    }

}

int main(){

    FILE *inf, *outf;
    inf=fopen("A-large.in","r");
    outf=fopen("A-large-result.in","w");
    
    int T;
    
    fscanf(inf,"%d",&T);
    for(int i=0;i<T;i++){
        memset(P,-1,sizeof(P));
        ret.clear();
        isOk=false;
        fscanf(inf,"%d",&N);
        int cntSum=0;
        for(int j=0;j<N;j++){
            fscanf(inf,"%d",&P[j]);
            cntSum+=P[j];
        }
        solve(cntSum);
        fprintf(outf,"Case #%d: ",i+1);
        for(int i=0;i<ret.size();i++){
            fprintf(outf,"%s ",ret[i].c_str());
        }
        fprintf(outf,"\n");
            
    }
//    getchar();
}