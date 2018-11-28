#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;
const int MAX_LEN = 500;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    cin>>t;
    int i = 0;
    int case_num;
    for(case_num=0;case_num<t;case_num++){
        int n, m;
        cin>>n>>m;
        int a[MAX_LEN][MAX_LEN];
        int j, k;
        for(j=0;j<MAX_LEN;j++){
            for(k=0;k<MAX_LEN;k++){
                a[j][k] = 0;
            }
        }
        for(j=0;j<n;j++){
            for(k=0;k<m;k++){
                cin>>a[j][k];
            }
        }
    int a_col_max[MAX_LEN];
    int a_row_max[MAX_LEN];
    int flag1 = 1;
    for(i=0;i<n;i++){
        int count=0;
        int temp_max = a[i][0];
            for(count=1;count<m;count++){
                if(a[i][count]>temp_max) temp_max=a[i][count];
            }
    a_row_max[i] = temp_max;
    if(a_row_max[i]>100 || a_row_max[i]<1){
        cout<<"Case #"<<case_num+1<<": NO"<<endl;
        flag1 = 0;break;
    }
    }
    for(i=0;i<m;i++){
        int count=0;
        int temp_max = a[0][i];
        for(count=1;count<n;count++){
            if(a[count][i]>temp_max) temp_max=a[count][i];
        }
    a_col_max[i] = temp_max;
    if(a_col_max[i]>100||a_col_max[i]<1){
        cout<<"Case #"<<case_num+1<<": NO"<<endl;
        flag1 = 0; break;
    }
    }

    int flag = 1;
    if(flag1==1){
        for(j=0;j<n;j++){
            for(k=0;k<m;k++){
                if(flag==1){
                    if(a[j][k]!=a_col_max[k] && a[j][k]!=a_row_max[j]){
                            flag = 0;
                            cout<<"Case #"<<case_num+1<<": NO"<<endl;
                    }
                }
            }
        }
        if(flag==1){
            cout<<"Case #"<<case_num+1<<": YES"<<endl;
        }
    }
    }
    return 0;
}
