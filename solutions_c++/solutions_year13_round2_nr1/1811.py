#include<stdio.h>
#include <algorithm>
#include <string.h>


using namespace std;

unsigned long long int mote[200], extra[200], num, a;
int n;


int calmin(int i, long long int a, int ins){
    if(i==n) return 0;
    if(ins > n-i) return (n-i);
    if(a > mote[i]){
        a += mote[i];
        return (ins + calmin(i+1, a, 0) );
    }
    else{
        int temp1 = calmin(i, 2*a-1, ins+1);
        if(temp1 < n-i) return temp1;
        return n-i;
    }

}



int main(){
    int T, ans,ins;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for(int t=0; t<T; t++){
        scanf("%llu%d",&a,&n);
        for(int i=0; i<n; i++){
            scanf("%llu",&mote[i]);
        }
        sort(mote, mote+n);

        ans = 0;
        //i=0;
        ans = calmin(0,a,0);
 /*       while(1){
            if(i==n) break;
            ins = 0;
            while(1){
                int j =i;
                if(a>mote[j]){
                    a += mote[j];
                    i++;
                    break;
                }
                if(j==n) break;
                num = a-1;
                a += num;
                ins++;
                i++
            }

            num = a-1;
            if(a>mote[i]){
                a += mote[i];
            }
            else if( a+num > mote[i]){
                a += num + mote[i];
                ans++;
            }
            for(int temp = i; )
            else if(){
                ans = ans + n - i;
                break;
            }

        }*/
        printf("Case #%d: %d\n",t+1,ans);

    }


    return 0;
}
