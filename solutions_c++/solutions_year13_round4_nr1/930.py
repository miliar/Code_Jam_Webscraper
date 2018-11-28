/*
*   Abdurrahman Akkas
*   Google code jam 2013 Round 2
*   Problem A
*   insallah recursive fonksiyon yazmam
*/

#include<iostream>
#include<algorithm>

using namespace std;
int main(){
    int T,t,N,M,i,i2,i3,b;
    long long baspara,sonpara,k;
    cin>>T;
    for(t=1;t<=T;t++){
        int os[100001],es[100001],ps[100001];
        cin>>N>>M;
        for(i=0;i<M;i++){
            cin>>os[i]>>es[i]>>ps[i];
        }
        baspara=0;
        for(i=0;i<M;i++){
            k=0;
            for(i2=os[i];i2<es[i];i2++){
                k+=(N-i2+os[i])*ps[i];
                k%=1000002013LL;
            }
            baspara+=k;
           baspara%=1000002013LL;
        }
        b=1;
        while(b){
            b=0;
            for(i=0;i<M;i++){
                for(i2=0;i2<M;i2++){
                    if(i==i2)
                        continue;
                    if(os[i2]>os[i]&&os[i2]<=es[i]&&es[i2]>es[i]){
                        b=1;
                        if(ps[i]>ps[i2]){
                            ps[i]-=ps[i2];
                            os[M]=os[i2];
                            es[M]=es[i];
                            ps[M]=ps[i2];
                            M++;
                            os[i2]=os[i];
                        }else if(ps[i]<ps[i2]){
                            ps[i2]-=ps[i];
                            os[M]=os[i2];
                            es[M]=es[i];
                            ps[M]=ps[i];
                            M++;
                            es[i]=es[i2];
                        }else{
                            int tmp=os[i];
                            os[i]=os[i2];
                            os[i2]=tmp;
                        }
                    }
                }
            }
        }
        sonpara=0;
        for(i=0;i<M;i++){
            k=0;
            for(i2=os[i];i2<es[i];i2++){
                k+=(N-i2+os[i])*ps[i];
                k%=1000002013LL;
            }
            sonpara+=k;
            sonpara%=1000002013LL;
        }
        cout<<"Case #"<<t<<": "<<baspara-sonpara<<endl;
    }
    return 0;
}
//Deshi Deshi Basara Basara
