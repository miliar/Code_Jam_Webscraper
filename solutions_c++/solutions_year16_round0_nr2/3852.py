#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
//string largePath="/Users/lxq/Downloads/A-large-practice.in.txt";
int main() {
    // insert code here...
    vector<long long> resultList;
    int sumCount;
    long long credit,cred;
    int hasFind=10;
    long long myResult;
    bool hasZero;
    FILE *fp=fopen("/Users/lxq/Downloads/A-large.in.txt","r");
    FILE *fw=fopen("/Users/lxq/Downloads/A-large.out.txt","w");
    if (fp) {
        fscanf(fp,"%d",&sumCount);
        for (int j=0; j<sumCount; j++) {
            fscanf(fp,"%lld",&cred);
            hasFind=10;
            hasZero=false;
            int num[10]={0};
            if (cred==0) {
                myResult=0;
            }else{
                int k;
                credit=cred;
                for (k=2;hasFind>0;k++) {
                    if (credit>=10) {
                        long long ii=credit%10;
                        long long jj=credit/10;
                        while (ii!=0||(ii==0&&jj!=0)) {
                            if (num[ii]==0) {
                                num[ii]=1;
                                hasFind--;
                            }
                            ii=jj%10;
                            jj=jj/10;
                        }
                    }else{
                        num[credit]=1;
                        hasFind--;
                    }
                    credit=cred*k;
                }
                myResult=credit-cred;
            }
            resultList.push_back(myResult);
        }
    }
    for (int i=0; i<sumCount; i++)
        if (resultList[i]==0)
            fprintf(fw,"Case #%d: INSOMNIA\n",i+1);
        else
            fprintf(fw,"Case #%d: %lld\n",i+1,resultList[i]);
    return 0;
}