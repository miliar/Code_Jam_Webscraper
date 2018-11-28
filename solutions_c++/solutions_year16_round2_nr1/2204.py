#include <bits/stdc++.h>
using namespace std;
int bucket[30];
char cad[2005];
int sol[2005];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large_output.out","w",stdout);
    int t,l;
    scanf("%d",&t);
    for (int _case=1; _case<=t; _case++){
        scanf("%s",cad);
        l=strlen(cad);
        fill(bucket,bucket+30,0);
        for (int i=0; i<l; i++){
            bucket[cad[i]-'A']++;
        }
        int k=0;
        while (bucket['X'-'A']>0){
            bucket['S'-'A']--;
            bucket['I'-'A']--;
            bucket['X'-'A']--;
            sol[k++]=6;
        }
        while (bucket['W'-'A']>0){
            bucket['T'-'A']--;
            bucket['W'-'A']--;
            bucket['O'-'A']--;
            sol[k++]=2;
        }
        while (bucket['Z'-'A']>0){
            bucket['Z'-'A']--;
            bucket['E'-'A']--;
            bucket['R'-'A']--;
            bucket['O'-'A']--;
            sol[k++]=0;
        }
        while (bucket['S'-'A']>0){
            bucket['S'-'A']--;
            bucket['E'-'A']--;
            bucket['V'-'A']--;
            bucket['E'-'A']--;
            bucket['N'-'A']--;
            sol[k++]=7;
        }
        while (bucket['V'-'A']>0){
            bucket['F'-'A']--;
            bucket['I'-'A']--;
            bucket['V'-'A']--;
            bucket['E'-'A']--;
            sol[k++]=5;
        }
        while (bucket['F'-'A']>0){
            bucket['F'-'A']--;
            bucket['O'-'A']--;
            bucket['U'-'A']--;
            bucket['R'-'A']--;
            sol[k++]=4;
        }
        while (bucket['O'-'A']>0){
            bucket['O'-'A']--;
            bucket['N'-'A']--;
            bucket['E'-'A']--;
            sol[k++]=1;
        }
        while (bucket['N'-'A']>0){
            bucket['N'-'A']--;
            bucket['I'-'A']--;
            bucket['N'-'A']--;
            bucket['E'-'A']--;
            sol[k++]=9;
        }
        while (bucket['G'-'A']>0){
            bucket['E'-'A']--;
            bucket['I'-'A']--;
            bucket['G'-'A']--;
            bucket['H'-'A']--;
            bucket['T'-'A']--;
            sol[k++]=8;
        }
        while (bucket['T'-'A']>0){
            bucket['T'-'A']--;
            bucket['H'-'A']--;
            bucket['R'-'A']--;
            bucket['E'-'A']--;
            bucket['E'-'A']--;
            sol[k++]=3;
        }
        sort(sol,sol+k);
        printf("Case #%d: ",_case);
        for (int i=0; i<k; i++){
            printf("%d",sol[i]);
        }
        printf("\n");
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
