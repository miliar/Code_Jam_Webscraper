#include <iostream>
#include <cstdio>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <string>
#include <math.h>
#include<map>
#include <vector>
#include <queue>
#include <stack>
#include <set>
using namespace std;

int cards[4][4];
int t , row;
string toString(int num){
    string s1 ="";
    while (num) {
        s1+= (num%10+'0');
        num/=10;
    }
    string s2 ="";
    for (long i = s1.length()-1; i>=0; i--) {
        s2+=s1[i];
    }
    return s2;
}
bool isPowerOfTwo(int mask){
    return mask!=0&&!(mask&(mask-1));
}
int main (){
    scanf("%d",&t);
    int counter =1;
    while (t--) {
        int mask1=0,mask2=0;
        scanf("%d",&row);
        for (int i =0; i<4; i++) {
            for (int j=0; j<4; j++) {
                scanf("%d",&cards[i][j]);
            }
        }
        for (int i =0; i<4; i++) {
            mask1|=(1<<(cards[row-1][i]));
        }
        scanf("%d",&row);
        for (int i =0; i<4; i++) {
            for (int j=0; j<4; j++) {
                scanf("%d",&cards[i][j]);
            }
        }
        for (int i =0; i<4; i++) {
            mask2|=(1<<(cards[row-1][i]));
        }
        int mask = mask1&mask2;
        if(isPowerOfTwo(mask)){
            printf("Case #%d: %d\n",counter,(int)log2((double)mask));
        }else if (mask==0){
            printf("Case #%d: Volunteer cheated!\n",counter);
        }else{
            printf("Case #%d: Bad magician!\n",counter);
        }
        counter++;
    }
    return 0;
}