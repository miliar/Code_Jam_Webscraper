#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>


using namespace std;

int main(){
freopen("A-small-attempt1.in", "r", stdin);
freopen("output_A_small_1.txt", "w", stdout);
long long int test,metro=0,nest;
long long int i,j,k;
cin>>test;
while(test--){
    metro++;
    cin>>nest;
    
    string two[nest];
    
    string one[nest];
    for(i=0;i<nest;i++){
        cin>>one[i];
        two[i]+=one[i]+'=';
    }
    cout<<"Case #"<<metro<<": ";
    int d=0;
    string tone;
    for(j=0;j<two[0].size();j++){
            if(two[0][j]!=two[0][j+1]){
                tone+=two[0][j];
            }
        }
    for(i=1;i<nest;i++){
            string x;
            for(j=0;j<two[i].size();j++){
                if(two[i][j]!=two[i][j+1]){
                x+=two[i][j];
                }
            }
        if(x.size()!=tone.size()){
            d=1;
            break;
        }
        else{
            for(j=0;j<tone.size();j++){
                if(tone[j]!=x[j]){
                    d=1;
                    break;
                }
            }
            if(d==1){
                break;
            }
        }
    }
    if(d==1){
        cout<<"Fegla Won\n";
    }
    else{
        long long  int pera1=0,pera2=100000000;
        long int sheld[nest][100];
        for(i=0;i<nest;i++){
            for(j=0;j<100;j++){
                sheld[i][j]=0;
            }
        }
        for(i=0;i<nest;i++){
                int k=0;
                string qw=one[i]+'=';
            for(j=0;j<qw.size();j++){
                if(one[i][j]==one[i][j+1]){
                    sheld[i][k]++;
                }
                else
                {sheld[i][k]++;k++;}
            }
        }
        for(i=0;i<nest;i++){
            pera1=0;
            for(j=0;j<nest;j++){
                for(k=0;k<one[i].size();k++){
                    pera1+=abs(sheld[i][k]-sheld[j][k]);
                }
            }
            pera2=min(pera1,pera2);
        }

    cout<<pera2<<"\n";
    pera2=100000000;
    }

}
return 0;}
