#include <cstdio>
#include <cstring>
using namespace std;
typedef long long int ll;
int present[10];
int main()
{
    FILE *p=fopen("C://Users//home//Desktop//output_jam.txt","w");
    FILE *q=fopen("C://Users//home//Desktop//inp.txt","r");
    int tc;
    ll n;
    fscanf(q,"%d",&tc);
    //scanf("%d",&tc);
    for(int i=1;i<=tc;i++){
        memset(present,0,sizeof(present));
        //scanf("%d",&n);
        fscanf(q,"%lld",&n);
        if(n==0){
            fprintf(p,"Case #%d: INSOMNIA\n",i);
            //printf("Case #%d: INSOMNIA\n",i);
            continue;
        }
        int cnt=0;
        for(ll j=n;;j+=n){
            ll k=j;
            while(k>0){
                int r=k%10;
                if(!present[r]){
                    present[r]++;
                    cnt++;
                }
                k=k/10;
            }
            if(cnt==10){
                fprintf(p,"Case #%d: %lld\n",i,j);
                //printf("Case #%d: %d\n",i,j);
                break;
            }
        }
    }
    fclose(q);
    fclose(p);
    return 0;
}
