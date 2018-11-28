#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<string.h>
using namespace std;
char odd[55];
char even[55];
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int t,ca;
    scanf("%d",&t);
    printf("Case #1:\n");
    int n = 16;
    int target = 50;
   // n = 32;
    //target = 500;
    int found = 0;
    int l = n/2-1;
    int i;
    for(i=0;i<l;i++)odd[i] = '0';
    odd[i] = 0;
    odd[0] = odd[1] = odd[2] = '1';
    reverse(odd,odd+l);
   // printf("%s\n",odd);
    while(target)
        {
       for(i=0;i<l;i++)even[i] = '0';
    even[i] = 0;
    even[0] = even[1] = even[2] = '1';
    reverse(even,even+l);
     //   printf("start with %s %s\n",even,odd);
        while(1)
            {
        //  printf("%d ",target);
           // printf("%s %s\n",odd,even);
            printf("1");
            int i;
            for(i=0;i<l;i++)printf("%c%c",even[i],odd[i]);
           // printf("%c",even[i]);
            printf("1 3 4 5 6 7 8 9 10 11\n");
            target--;
            if(target==0)break;
            if(!next_permutation(even,even+l))break;;
            
        }
        next_permutation(odd,odd+l);
    }
    return 0;
}
