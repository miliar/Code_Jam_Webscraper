#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    for(int k=1;k<=t;k++){
        int sm;
        scanf("%d",&sm);
        char arr[sm+1];
        scanf("%s",arr);
        int sum=arr[0]-'0',reqd=0;
        for(int i=1;i<=sm;i++){
            //scanf("%d",&arr[i]);
            if(sum<i){
                reqd=reqd+i-sum;
                sum=i;
            }
           sum=sum+(arr[i]-'0');

        }
        printf("Case #%d: %d\n",k,reqd);

    }
    return 0;
}
