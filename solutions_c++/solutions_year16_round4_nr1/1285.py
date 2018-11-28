#include <stdio.h>
#include "stdlib.h"
#include "string"
#include "vector"

using namespace std;

char ans[5000];
long n,m,r,p,s;

int main() {
    long t,tt;
    freopen("A-large.in.txt", "r", stdin);
    freopen("A-large.out.txt", "w", stdout);
    scanf("%ld",&t);
    for (tt=1;tt<=t;tt++){
        scanf("%ld%ld%ld%ld",&n,&r,&p,&s);
        m=1<<n;
        for (int i=2;i<=n;i+=2){
            long j=1<<(i-2);
            for (long k=0;k<m;k+=j*4){
                ans[k+j]='R';
                ans[k+j*2]='P';
                ans[k+j*3]='S';
                r--;
                p--;
                s--;
            }
        }
        printf("Case #%ld: ",tt);
        if (r>=0&&p>=0&&s>=0&&r<2&&p<2&&s<2){
            if(r>0){
                ans[0]='R';
                r--;
            }
            else if (p>0){
                ans[0]='P';
                p--;
            }
            else if (s>0){
                ans[0]='S';
                s--;
            }
            if (n%2==1){
                if(r>0){
                    ans[m/2]='R';
                    r--;
                }
                else if (p>0){
                    ans[m/2]='P';
                    p--;
                }
                else if (s>0){
                    ans[m/2]='S';
                    s--;
                }
            }
            vector<string> anss(5000);
            for (int i=0;i<m;i++)
                anss[i]=ans[i];
            for (int i=2;i<=n;i+=2){
                for (int j=0;j<m;j+=4){
                    sort(anss.begin()+j, anss.begin()+j+4);
                }
                for (int j=0;j<m;j+=4){
                    if (anss[j].compare(anss[j+1])||anss[j+2].compare(anss[j+3]))
                        anss[j/4]=anss[j]+anss[j+2]+anss[j+1]+anss[j+3];
                    else
                        anss[j/4]=anss[j]+anss[j+1]+anss[j+2]+anss[j+3];
                }
                m/=4;
            }
            if (m==2){
                if (anss[0]>anss[1])
                    anss[0]=anss[1]+anss[0];
                else
                    anss[0]=anss[0]+anss[1];
            }
            printf("%s\n",anss[0].c_str());
        }
        else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
