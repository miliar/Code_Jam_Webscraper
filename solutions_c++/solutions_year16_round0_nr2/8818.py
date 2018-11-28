#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
#include<vector>
#include<list>
#include<set>
#include<utility>
#include<map>
#include<stack>
#include<queue>
using namespace std;
int main(){
    int t,k=1;
    scanf("%d",&t);
    while(t--){
        char str[200];
        scanf("%s",str);
        int n=strlen(str);
        int arr[n];
        if(str[0]=='-')
            arr[0]=1;
        else
            arr[0]=0;
        for(int i=1;i<n;i++){
            if(str[i-1]=='-'&&str[i]==str[i-1])
                arr[i]=arr[i-1];
            else if(str[i-1]=='-'&&str[i]!=str[i-1])
                arr[i]=arr[i-1];
            else if(str[i-1]=='+'&&str[i]==str[i-1])
                arr[i]=arr[i-1];
            else if(str[i-1]=='+'&&str[i]!=str[i-1])
                arr[i]=arr[i-1]+2;
        }
        printf("Case #%d: %d\n",k,arr[n-1]);
        k++;
    }
    return 0;
}
