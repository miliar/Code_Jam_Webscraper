#include<iostream>
#include<stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <vector>
using namespace std;
int main(){
    int noOfBlocks,testcases,testcasesran = 0,cnt = 0,resultwar = 0,resultdec =0;;
    freopen("D-large.in","r",stdin);
    freopen("deceitfulout.txt","w",stdout);
    cin>>testcases;
    double value;
    int deceitfulresult[testcases];
    int warresult[testcases];
    int decresult[testcases];
    while(testcasesran < testcases){
        resultwar =0;
        resultdec =0;
        warresult[cnt] = 0;
        decresult[cnt] = 0;
        cin>>noOfBlocks;
        vector<double> naomi;
        vector<double> ken;

        for(int i=0;i<noOfBlocks;i++){
            cin>>value;
            naomi.push_back(value);
        }
        for(int i=0;i<noOfBlocks;i++){
            cin>>value;
            ken.push_back(value);
        }
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());
        int i=0;
        int j=0;
        while(resultwar == 0){
            if(naomi[i] < ken[j]){
                i++;
                j++;
            }
            else{
              j++;
            }
            if(j == noOfBlocks){
                warresult[cnt] = noOfBlocks - i;
                resultwar = 1;
            }
        }
        sort(ken.rbegin(),ken.rend());
        sort(naomi.rbegin(),naomi.rend());
        int k=0;
        int l=0;
        while(resultdec == 0){
            if(naomi[k] > ken[l]){
                l++;
                k++;
            }
            else{
                l++;
            }
            if(l == noOfBlocks){
                decresult[cnt] = k;
                resultdec = 1;
            }
        }

        cnt++;
        testcasesran++;
    }
for(int i=0;i<testcases;i++){
        cout<<"Case #"<<i+1<<": "<<decresult[i]<<" "<<warresult[i]<<endl;
    }
return 0;
}
