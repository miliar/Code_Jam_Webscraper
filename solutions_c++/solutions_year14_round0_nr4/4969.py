#include<iostream>
#include <fstream>
#include<algorithm>
using namespace std;
int cases;
int n;
float nao[1000];
float ken[1000];
bool kens[1000];
int cheat(float *a,float *b){
    int i,j;
    int score=0;
    for(i=n-1;i>=0;i--){
        for(j=n-1;j>=0;j--){
        if(kens[j]==0&&a[i]>b[j]){
        score++;
        kens[j]=1;
        break;
        }
        }  
    }
    return score;
    }
int uncheat(float *a,float *b){
     int i,j;
    int score=0;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
     //   cout<<a[i]<<" "<<b[j]<<endl;
        if(kens[j]==0&&b[j]>a[i]){
        kens[j]=1;
        break;
        }
        }  
        if(j==n)
        score++;
    }
    return score; 
}
int main(){

    scanf("%d",&cases);
    int i,j,ts;
  //  ofstream ocout;
  //  ocout.open("test.txt");
    for(ts=1;ts<cases;ts++){
    scanf("%d",&n);
    for(i=0;i<n;i++)
    scanf("%f",&nao[i]);
    for(j=0;j<n;j++)
    scanf("%f",&ken[j]);
    sort(nao,nao+n);
    sort(ken,ken+n);
    memset(kens,0,sizeof(kens));
    int t1=cheat(nao,ken);
    memset(kens,0,sizeof(kens));
    int t2=uncheat(nao,ken);
    cout<<"Case #"<<ts<<": "<<t1<<" "<<t2<<endl;
    }
    scanf("%d",&n);
    for(i=0;i<n;i++)
    scanf("%f",&nao[i]);
    for(j=0;j<n;j++)
    scanf("%f",&ken[j]);
    sort(nao,nao+n);
    sort(ken,ken+n);
    memset(kens,0,sizeof(kens));
    int t1=cheat(nao,ken);
    memset(kens,0,sizeof(kens));
    int t2=uncheat(nao,ken);
    cout<<"Case #"<<ts<<": "<<t1<<" "<<t2;
    //ocout.close();
   // system("pause");
    return 0;
    }

