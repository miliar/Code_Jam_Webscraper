#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,n;
    char st[1005];
    FILE *fr=fopen("A-large.in","r");
    FILE *fw=fopen("codejam1large.txt","w");
    fscanf(fr,"%d",&t);
    for(int j=1;j<=t;j++){
        fscanf(fr,"%d",&n);
        fscanf(fr,"%s",st);
        int count=0,res=0;
        count+=st[0]-'0';
        for(int i=1;i<n+1;i++){
            if(i>count){
                res+=i-count;
                count+=i-count;
            }

            count+=st[i]-'0';
        }
        fprintf(fw,"Case #%d: %d\n",j,res);
        //cout<<res<<endl;
    }
    return 0;
}
