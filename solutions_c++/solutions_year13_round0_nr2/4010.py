#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main()
{
    int t;
    int n;
    int m;
    int mx;
    int tmp;
    int count;
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        scanf("%d%d",&n,&m);
        int arr[n][m];
        int rwmx[n];
        //rwmx={0};
        memset(rwmx,0,sizeof(int)*n);
        int columnmx[m];
        //columnmx[m]={0};
        memset(columnmx,0,sizeof(int)*m);
        /*for(int p=0;p<m;p++){
            cout<<columnmx[p]<<"  ";
        }
        cout<<endl;*/

        //mx=0;
        for(int j = 0 ; j < n; j++){
            for(int k = 0 ; k < m ; k++){
                scanf("%d",&arr[j][k]);
                if(arr[j][k] > rwmx[j]){
                    rwmx[j] = arr[j][k];
                }
                if(arr[j][k] > columnmx[k]){
                    columnmx[k] = arr[j][k];
                }
            }
        }
        /*for(int p=0;p<n;p++){
            cout<<rwmx[p]<<"   ";
        }
        cout<<endl;*/
        /*for(int p=0;p<m;p++){
            cout<<columnmx[p]<<"   ";
        }
        cout<<endl;*/
        tmp = 0 ;
        for(int j=0;j<n;j++){
            for(int k=0;k<m;k++){
                if(arr[j][k] < rwmx[j]  &&  arr[j][k] < columnmx[k]){
                    tmp++;
              //      cout<<"enter"<<endl;
                    //printf("NO\n");
                }
            }
        }
        //cout<<tmp<<endl;
        if(tmp==0){
            cout << "Case #" << i+1 <<": "<< "YES" << endl;
        }
        else{
            cout << "Case #" << i+1 <<": "<< "NO" << endl;
        }
    }
    return 0;

}

