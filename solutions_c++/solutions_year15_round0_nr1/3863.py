#include<fstream>
#define N 2000
using namespace std;
int n,m,v;
char s[N];
void process();
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T,i;
    scanf("%d",&T);
    for(i=1;i<=T;i++){
        process();
        printf("Case #%d: %d\n",i,v);
    }
    return 0;
}

void process()
{
    int i;
    scanf("%d",&n);
    scanf("%s",s);
    m=v=0;
    for(i=0;i<=n;i++){
        s[i]-='0';
        if(m<i){
            v+=i-m;
            m+=i-m;
        }
        m+=s[i];
    }
}
