#include <bits/stdc++.h>

#define inf 0x3f3f3f3
#define maxn 1000010
using namespace std;
int qtd[maxn];
string aux[]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
char le[]={'Z','G','H','U','X','T','S','O','V','E'};
int num[]={0,8,3,4,6,2,7,1,5,9};
vector <int> ad[maxn];
int main(){
  int t;
  char a[maxn];
  scanf("%d",&t);
  getchar();
  for(int i=0;i<t;i++){
    memset(qtd,0,sizeof(qtd));
    gets(a);
    int len=strlen(a);
    for(int j=0;j<len;j++){
      qtd[a[j]-'A']++;
      //printf("%d\n",qtd[a[j]-'A']);
    }
    for(int k=0;k<=9;k++){
      ad[num[k]].clear();
      int val=qtd[le[k]-'A'];
      // printf("%d\n",qtd[le[k]-'A']);
      
      for(int i=0;i<aux[num[k]].size();i++){
	qtd[aux[num[k]][i]-'A']-=val;
      }
      ad[num[k]].push_back(val);
    }
    printf("Case #%d: ",i+1);
    for(int k=0;k<=9;k++){
      for(int j=0;j<ad[k][0];j++){
	printf("%d",k);
      }
    }
    printf("\n");
  }
  return 0;
}
