#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    int t,n;
    scanf("%d",&t);
    for(int p=1;p<=t;p++){
        scanf("%d",&n);
        char a[n+1];
        scanf("%s",a);
        long count=0,frnd=0;
        for(int i=0;i<=n;i++){
            if(count<i&&(a[i]-48)>0){
                    frnd+=i-count;
                    count=a[i]-48+i;}
            else
            count+=a[i]-48;
        //printf("%ld\n",frnd);
        }
        printf("Case #%d: %ld\n",p,frnd);
    }
    return 0;
}
