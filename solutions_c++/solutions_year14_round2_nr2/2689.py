#include<cstdio>
#include<cmath>
#include<cstring>
#include<map>
#include<stack>
#include<vector>
#include<queue>
#include<algorithm>
#include<utility>
#include<set>

using namespace std;

int main(){

    FILE *in,*out;

    in=fopen("input.txt","r");
    out=fopen("output.txt","w");

    int t,a,b,k,ans,i,j,cas=1;
    fscanf(in,"%d",&t);

    while(t--){

        fscanf(in,"%d%d%d",&a,&b,&k);
        ans=0;
        for(i=0;i<a;i++){
            for(j=0;j<b;j++){
                int temp=i&j;

                if(temp<k)
                    ans++;}}
        fprintf(out,"Case #%d: %d\n",cas,ans);
        cas++;
        }
    fclose(in);
    fclose(out);

    return 0;
}
