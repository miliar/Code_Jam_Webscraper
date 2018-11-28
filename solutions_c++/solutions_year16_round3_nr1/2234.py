/*@author:abhi2110*/
#include <bits/stdc++.h>
using namespace std;
#define TC int tc; scanf("%d",&tc); while(tc--)
#define sii(i,j) scanf("%d%d",&i,&j)
#define si(i) scanf("%d",&i)
#define sl(i) scanf("%lld",&i)
#define ss(i) scanf("%s",i)
#define m0(a) memset(a,0,sizeof(a))
#define m1(a) memset(a,-1,sizeof(a))
#define pb push_back
#define mp make_pair
#define clk 1.0*clock()/CLOCKS_PER_SEC
#define FILEIO(x) freopen(#x ".in","r",stdin);freopen(#x ".out","w",stdout);
#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long int ll;
int present[29];
int main(){
    //FILEIOS
    int cas=1;
    TC{
        int n;
        si(n);
        int arr[n+1];
        int sum=0;
        for(int i=0;i<n;i++)
            present[i]=1;
        for(int i=0;i<n;i++){
            si(arr[i]);
            sum+=arr[i];
        }
        printf("case #%d: ",cas);
        int flag=0;
        while(sum>0){
            int mx=-99999,index,pr=0;
            for(int i=0;i<n;i++){
                if(arr[i]>mx){
                    mx=arr[i];
                    index=i;
                }
                if(arr[i]>0)
                    pr++;
            }
            if(pr>2 || pr<2){
                printf("%c ",char(index+65));
                sum--;
                arr[index]--;
            }
            else if(pr==2 && (mx*2)==sum){
                flag=1;
                break;
            }
        }
        if(flag==1){
            int in1=-1,in2=-1;
            int d=sum/2;
            for(int i=0;i<n;i++){
                if(arr[i]==d && in1==-1)
                    in1=i;
                if(arr[i]==d && in1!=-1)
                    in2=i;
            }
            for(int i=0;i<(sum/2);i++)
                printf("%c%c ",65+in1,65+in2);
        }
        printf("\n");
        cas++;
    }
	return 0;
}
