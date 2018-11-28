//HARE KRISHNA
#include<bits/stdc++.h>
using namespace std;

#define pb push_back
string arr[]={"ZERO","EIGHT","SIX","SEVEN","FIVE","FOUR","TWO","THREE","ONE","NINE"};
int arrano[]={0,8,6,7,5,4,2,3,1,9};
char arr1[]={'Z','G','X','S','V','U','W','R','O','I'};
vector<int>myvec;
int cnt[30];
char str[3000];
int main(){
    freopen("input-1.in","r",stdin);
    freopen("out-1.txt","w",stdout);
    int t,tcase;
    scanf("%d",&t);
    for(tcase=1;tcase<=t;tcase++){
    myvec.clear();
    memset(cnt,0,sizeof(cnt));
    scanf("%s",str);
    int len=strlen(str);
    int i;
    for(i=0;i<len;i++){
        cnt[str[i]-'A']++;
    }
    int j;
    for(i=0;i<10;i++){
        int id=arr1[i]-'A';
        int howmany=cnt[id];
        for(j=0;j<howmany;j++)myvec.pb(arrano[i]);
        string what=arr[i];
        int whatlen=what.size();
        for(j=0;j<whatlen;j++){
            cnt[what[j]-'A']=cnt[what[j]-'A']-howmany;
        }

    }
    sort(myvec.begin(),myvec.end());
    int sz=myvec.size();
    printf("Case #%d: ",tcase);
    for(i=0;i<sz;i++){
        printf("%d",myvec[i]);
    }
    printf("\n");
    }
    return 0;
}
