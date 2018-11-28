#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int arr[10],ans[100];
int mark[10];
int chck(int* mark){
    for(int i=0;i<10;i++){
        if(!mark[i])
            return 1;
    }
    return 0;
}
int main(){
    int a,b,i,j,n,t,carry,temp;
    FILE *rr,*ww;
    rr=fopen("A.txt","r");
    ww=fopen("AAns.txt","w");
    fscanf(rr,"%d",&t);
    //cin>>t;
    temp=t;
    for(temp=1;temp<=t;temp++){
        memset(arr,0,sizeof(arr));
        memset(mark,0,sizeof(mark));
        memset(ans,0,sizeof(ans));
        //cin>>n;
        fscanf(rr,"%d",&n);
        //cout<<n<<t;
        if(n==0){
            //cout<<"INSOMNIA\n";
            fprintf(ww,"Case #%d: INSOMNIA\n",temp);
            continue;
        }
        i=0;
        while(n!=0){
            arr[i++]=n%10;
            mark[arr[i-1]]=1;
            n/=10;
        }
        while(chck(mark)){
            carry=0;
            for(j=0;j<i;j++){
                ans[j]+=arr[j]+carry;
                carry=ans[j]/10;
                ans[j]=ans[j]%10;
                mark[ans[j]]=1;
            }
            if(carry==1){
                ans[i]+=1;
                mark[ans[i]]=1;
            }
            /*for(int k=0;k<10;k++)
                cout<<mark[k];
            cout<<endl;*/
        }
        fprintf(ww,"Case #%d: ",temp);
        if(ans[i]){
            for(j=i;j>=0;j--){
                fprintf(ww,"%d",ans[j]);
                //cout<<ans[j];
            }
        }
        else{
            for(j=i-1;j>=0;j--){
                fprintf(ww,"%d",ans[j]);
                //cout<<ans[j];
            }
        }
        fprintf(ww,"\n");
        //cout<<endl;
    }
    return 0;
}
