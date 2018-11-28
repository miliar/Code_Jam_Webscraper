#include<stdio.h>
//#include<iostream>
#include<string.h>
//#include<stdlib.h>
//#include<math.h>
//#include<map>
//#include<stack>
//#include<queue>
//#include<algorithm>
#define mem(a,b) memset(a,b,sizeof(a))
//#define Max(a,b) ((a)>(b)?(a):(b))
//#define Min(a,b) ((a)<(b)?(a):(b))
//#define INF 0x3f3f3f3f
#define MAX 10500

//using namespace std;

int from,to;

int res[MAX];

//int huiwen(int a){
//    char hui[100];
//    int len,i;
//    itoa(a,hui,10);
//    len = strlen(hui);
//    for(i = 0;i < len;++ i){
//        if(hui[i] != hui[len - i - 1])
//            return 0;
//    }
//    return 1;
//}
//void dabiao(){
//    int i,k;
//    int temp[MAX];
//    mem(res,0);
//    for(i = 1,k = 0;i < 40;++ i){
//        if(huiwen(i)){
//            temp[k ++] = i;
//        }
//    }
//    for(i = 0;i < k;++ i){
//        if(huiwen(temp[i] * temp[i])){
//            res[temp[i] * temp[i]] = 1;
//        }
//    }
//    return ;
//}

int main(){
#ifndef ONLINE_JUDGE
    freopen("G:\\study\\programs\\test\\in.txt","r",stdin);
    freopen("G:\\study\\programs\\test\\out.txt","w",stdout);
#endif
    int num_text,i,num,k = 0;
    scanf("%d",&num_text);
    //dabiao();
    mem(res,0);
    res[1] = res[4] = 1;
    res[9] = res[121] = 1;
    res[484] = 1;
    while(k < num_text){
        k ++;
        printf("Case #%d: ",k);
        num = 0;
        scanf("%d %d",&from,&to);
        for(i = from;i <= to;++ i){
            if(res[i]){
                num ++;
            }
        }
        printf("%d\n",num);
    }
    return 0;
}
