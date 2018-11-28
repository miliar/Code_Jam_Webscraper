#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
int arr[26];
int maxi(int n){
    int mi=0;
    for(int i=1;i<n;i++){
        if(arr[i]>arr[mi])
            mi=i;
    }
    return mi;
}
void chck(int n,int total,int t){
    for(int i=0;i<n;i++){
        if(((double)arr[i])/total>0.5)
            cout<<"horrah "<<n<<" "<<t;
    }
}
int main(){
    FILE *in,*out;
    int t,n,i,j,total,ind;
    in=fopen("in.txt","r");
    out=fopen("out.txt","w");
    fscanf(in,"%d",&t);
    for(j=1;j<=t;j++){
    total=0;
        fscanf(in,"%d",&n);
        for(i=0;i<n;i++){
            fscanf(in,"%d",&arr[i]);
            total+=arr[i];
        }
        fprintf(out,"Case #%d: ",j);
        if(n>2){
        while(total>2){
            ind=maxi(n);
            arr[ind]--;
            fprintf(out,"%c ",'A'+ind);
            total--;
            chck(n,total,j);
        }
        for(i=0;i<n;i++){
            if(arr[i]!=0){
                fprintf(out,"%c",'A'+i);
            }
        }
        fprintf(out,"\n");
        }
        else{
            while(total!=0){
                fprintf(out,"AB ");
                total-=2;
            }
            fprintf(out,"\n");
        }
    }

    return 0;
}
