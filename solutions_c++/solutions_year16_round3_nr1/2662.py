#include <iostream>

using namespace std;

char ALP[]={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};

int sens[26];
int T,N,sensN;

bool pickOne(){
    bool flag;
    sensN--;
    for(int n=0;n<N;n++){
		if(sens[n]==0)continue;
        sens[n]--;
        flag=true;
        for(int j=0;j<N;j++){
            if(sens[j]>sensN/2)flag=false;
        }
        if(flag){
            cout<<ALP[n]<<" ";
            return true;
        }
        else sens[n]++;
    }
    sensN++;
    return false;
}

void pickTwo(){
    bool flag;
    sensN-=2;
    for(int n=0;n<N;n++){
		if(sens[n]==0)continue;
        sens[n]--;
        for(int j=0;j<N;j++){
			if(sens[j]==0)continue;
            sens[j]--;
            flag=true;
            for(int i=0;i<N;i++){
                if(sens[i]>sensN/2)flag=false;
            }
            if(flag){
                cout<<ALP[n]<<ALP[j]<<" ";
                return;
            }
            else sens[j]++;
        }
        sens[n]++;
    }
}

int main() {
    cin>>T;
    for(int t=1;t<=T;t++){
        cin>>N;
        sensN=0;
        for(int n=0;n<N;n++){
            cin>>sens[n];
            sensN+=sens[n];
        }
        cout<<"Case #"<<t<<": ";
        while(sensN!=0){
            if(pickOne())continue;
            else pickTwo();
        }
        cout<<endl;
    }
    return 0;
}
