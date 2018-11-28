#include <cstdio>
#include <vector>
#include <cstring>
using namespace std;

int main(){
    
    int t;
    
    scanf("%d ",&t);
    
    for(int i=0;i<t;i++){
        vector<int> count(26,0);
        char s[2001];
        scanf("%s ",s);
        int len = strlen(s);
        for(int j=0;j<len;j++){
            count[s[j]-65]++;
        }
        vector<int> num(10,0);
        num[0]=count['Z'-65];
        count['O'-65]-=num[0];
        num[2]=count['W'-65];
        count['O'-65]-=num[2];
        num[4]=count['U'-65];
        num[6]=count['X'-65];
        num[8]=count['G'-65];
        count['F'-65]-=num[4];
        count['O'-65]-=num[4];
        count['S'-65]-=num[6];
        count['H'-65]-=num[8];
        num[5]=count['F'-65];
        num[1]=count['O'-65];
        num[3]=count['H'-65];
        num[7]=count['S'-65];
        num[9]= (count['N'-65]-num[7]-num[1])/2;
        printf("Case #%d: ",i+1);
        for(int j=0;j<10;j++){
            for(int k=0;k<num[j];k++){
                printf("%d",j);
            }
        }
        printf("\n");
    }
    
}
