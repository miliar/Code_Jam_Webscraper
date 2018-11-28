#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#define max_n 9999999
#define pb push_back
#define mp make_pair
#define fi first
#define sc second
#define pi acos(-1)

using namespace std;

typedef long long ll;
typedef vector <int > vi;
typedef pair<int,int> pii;
typedef vector <pii> vii;

int N,t,sum,x,data[1000003],countt,lo,akhir;
char temp[1000003];
vector <int>doo;

bool cek(char la){
    if(la=='a'||la=='e'||la=='u'||la=='i'||la=='o')return false;
    return true;
}
int find(int lo){
    return lower_bound (doo.begin(), doo.end(), lo)-doo.begin();
}
int main(){
    scanf("%d",&N);
    for(int t=1;t<=N;t++){
        scanf("%s %d",temp,&x);
        memset(data,0,sizeof(data));
        doo.clear();
        lo=strlen(temp);
        countt=0;
        sum=0;
        for(int i=0;i<lo;i++){
            if(cek(temp[i])){
                countt++;
            }
            else countt=0;
            data[i]=countt;
            if(data[i]>=x)doo.pb(i);
        }
        for(int i=0;i<=lo-x;i++){
            
            akhir=find(i);
            if(akhir==doo.size())break;
            while(doo[akhir]-i<x-1){
                akhir++;
                if(akhir==doo.size())break;
            }
            if(akhir<doo.size()){
                sum+=lo-doo[akhir];
              //  printf("%d %d\n",lo-doo[akhir],i);
            }
        }
        printf("Case #%d: %d\n",t,sum);
    }
    return 0;
}
