#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int deceit_war_calculate(double naomi[],double ken[],int n){
    int deceit_war=0;
    int top=n-1;
    for(int j=0;j<n;j++){
        if(naomi[j]>ken[j]){
            deceit_war++;
        }
        else{
            double temp=ken[top];
            ken[top]=ken[j];
            ken[j]=temp;
            sort(ken+j+1,ken+n);
        }
    }
    return deceit_war;
}
int war_calculate(double naomi[],double ken[],int n){
    int war=0;
    int flag=0;
    int flag2=0;
    for(int j=0;j<n;j++){
        if(naomi[j]>ken[j]){
            for(int k=j+1;k<n;k++){
                if(ken[k]>naomi[j]){
                    double temp=ken[k];
                    ken[k]=ken[j];
                    ken[j]=temp;
                    flag=1;
                    break;
                }
            }
            if(flag==0){war=n-j;break;}
            else flag=0;
        }
    }
    return war;
}
int main(){
    freopen("1.in", "r", stdin) ;
    freopen("1.out", "w", stdout) ;
    int t=0;
    cin>>t;
    for(int i=1;i<=t;i++){
        int n=0;
        cin>>n;
        double naomi[2000]={0};
        double ken[2000]={0};
        for(int j=0;j<n;j++){
            cin>>naomi[j];
        }
        for(int k=0;k<n;k++){
            cin>>ken[k];
        }
        sort(naomi,naomi+n);
        sort(ken,ken+n);
        /*for(int j=0;j<n;j++){
            cout<<naomi[j]<<" ";
        }
        cout<<"\n";
        for(int k=0;k<n;k++){
            cout<<ken[k]<<" ";
        }*/
        int deceit_war=0;
        int war=0;
        int top=n-1;
        deceit_war=deceit_war_calculate(naomi,ken,n); 
        sort(naomi,naomi+n);
        sort(ken,ken+n);
        war=war_calculate(naomi,ken,n);
        cout<<"Case #"<<i<<": ";
        cout<<deceit_war<<" "<<war<<"\n";
    }
}
