#include<stdio.h>
#include<iostream>

using namespace std;

int main(){

    int T, N, posKen[1000], pposKen[1000], NDCount, NOCount, flag, max;
    double Naomi[1000], Ken[1000], temp;

    cin>>T;

    for(int i=0; i<T; i++){

        cin>>N;
        for(int j=0; j<N; j++){
            cin>>Naomi[j];
        }
        for(int j=0; j<N; j++){
            cin>>Ken[j];
            posKen[j]=1;
            pposKen[j]=1;
        }
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(Naomi[i]<Naomi[j]){
                    temp=Naomi[i];
                    Naomi[i]=Naomi[j];
                    Naomi[j]=temp;
                }
                if(Ken[i]<Ken[j]){
                    temp=Ken[i];
                    Ken[i]=Ken[j];
                    Ken[j]=temp;
                }
            }
        }
        NDCount=0;
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(Naomi[i]>Ken[j]&&pposKen[j]==1){
                    pposKen[j]=0;
                    NDCount++;
                    break;
                }
            }
        }
        NOCount=0;
        for(int i=0; i<N; i++){
            flag=0;
            for(int j=0; j<N; j++){
                if(Ken[j]>Naomi[i]&&posKen[j]==1){
                    flag=1;
                    posKen[j]=0;
                    break;
                }
            }
            if(flag==0){
                NOCount++;
            }
        }
        cout<<"Case #"<<i+1<<": "<<NDCount<<" "<<NOCount<<endl;

    }

    return 0;
}
