#include<iostream>
#include<stdlib.h>
using namespace std;
int compare (const void * a, const void * b)
{
  if( *(double*)a - *(double*)b >0){return 1;}
  else if(  *(double*)a - *(double*)b <0 ){return -1;}
  else if(  *(double*)a == *(double*)b ){return 0;}
}

int main(){
    int cases,counter=0;
    cin>>cases;
    while(cases--){
        int a,num,b,ans=0,anss=0,flag,i,j,x,y,z;
        cin>>num;
        double n[num],k[num],temp[num];
        for(i=0;i<num;i++){cin>>n[i];}
        for(i=0;i<num;i++){cin>>k[i];}
        qsort(k,num,sizeof(double), compare);

        for(i=0;i<num;i++){temp[i]=k[i];}
        for(i=0;i<num;i++){
            flag=0;
            for(j=0;j<num;j++){
                if(temp[j] > n[i] ){
                    temp[j]=0;
                    anss++;
                    flag=1;
                    break;
                }
            }
            if(flag==0){for(j=0;j<num;j++){
                           if(temp[j]!=0){temp[j]=0;break;}
            }            }
        }

        qsort(n,num,sizeof(double), compare);
        int nb=0,kb=0,nt=num-1,kt=num-1;
        i=0;
        while(i<num){
            while((n[nb]<k[kb])&& nb<=nt &&kt>=kb ){
                nb++;kt--;
            }
            while((n[nb]>k[kb]) && nb<=nt && kb<=kt){
                ans++;nb++;kb++;
            }
            i++;
        }
        counter++;
        anss=num-anss;
        cout<<"Case #"<<counter<<": "<<ans<<" "<<anss<<endl;
    }
}
