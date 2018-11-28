#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <math.h>
using namespace std;
int main() {
    int sumCount,sumcount;
    vector< vector<long long> > resultList;
    int k,c,s;
    int a,b,count;
    //FILE *fp=fopen("/Users/lxq/Downloads/A-large.in.txt","r");
    //FILE *fw=fopen("/Users/lxq/Downloads/A-large.out.txt","w");
    FILE *fp=fopen("/Users/lxq/Downloads/D-small-attempt2.in.txt","r");
    FILE *fw=fopen("/Users/lxq/Downloads/D-small-attempt2.out.txt","w");
    if (fp){
        fscanf(fp,"%d",&sumCount);
        for (int j=0; j<sumCount; j++) {
            fscanf(fp,"%d %d %d\n",&k,&c,&s);
            vector<long long> tempResult;
            a=k/c;
            if (a>s)
                tempResult.push_back(0);
            else{
                for (int i=1; i<=k; i++)
                    tempResult.push_back(i);
            }

            /*
            if (a>s)
                tempResult.push_back(0);
            else if(c==1){
                for (int i=1; i<=k; i++)
                    tempResult.push_back(i);
            }
            else if(c>1){
                if(k%c)a++;
                long long x[101]={0};
                b=0;
                sumcount=0;
                for (int ii=0; ii<a; ii++) {
                    count=0;
                    while (count<c-1) {
                        x[ii]+=b*pow(k, c-count-1);
                        b++;
                        count++;
                        sumcount++;
                    }
                    if (ii==0){
                        x[ii]+=c;sumcount++;b++;}
                    else if(sumcount<k)
                        x[ii]+=b;
                    tempResult.push_back(x[ii]);
                }
                }
             */
            resultList.push_back(tempResult);
             
        }
    }
    for (int i=0; i<sumCount; i++)
        if(resultList[i]==vector<long long>(1,0))
            fprintf(fw,"Case #%d: IMPOSSIBLE\n",i+1);
        else{
            fprintf(fw, "Case #%d: ",i+1);
            for (int j=0; j<resultList[i].size(); j++)
                fprintf(fw, "%lld ",resultList[i][j]);
            fprintf(fw, "\n");
        }
    return 0;
}