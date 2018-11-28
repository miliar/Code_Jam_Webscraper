#include <cstdlib>
#include <stdio.h>
#include <cstring>
#include <fstream>
#define REP(i,n) for(int i=0;i<(n);++i)
#define ZERO(x) memset(x,0,sizeof(x))

using namespace std;
int a[100][100];
int max1[100];
int max2[100];
bool isit(){
    ZERO(a);ZERO(max1);ZERO(max2);
    int N, M;
    scanf("%d %d",&N,&M);
    for(int i=0; i<N; i++){
        int max=0;
        for(int j=0; j<M; j++){
            scanf("%d",&a[i][j]);
            if(max<a[i][j])
                max=a[i][j];
        }
        max1[i]=max;
    }
    for(int j=0; j<M;j++){
        int max =0;
        for(int i=0; i<N; i++){
            if(max<a[i][j])
                max=a[i][j];
            }
        max2[j]=max;
    }
    
    
    for( int i=0;i<N;i++){
        for( int j=0; j<M;j++)
            if(a[i][j]<max1[i] && a[i][j]<max2[j])
            {//printf("Bye bye\n");
            return false;}
        
    }
    return true;
}

int main(){
    int T;
    scanf("%d",&T);
    ofstream myfile;
    
    myfile.open ("/home/ds/codes/outputlawn.txt");
    for(int ii=1; ii<=T;){
    if(isit())
        myfile << "Case #"<<ii++<<": YES"<<endl;
    else
        myfile << "Case #"<<ii++<<": NO"<<endl;
    }
    myfile.close();
    return 0;
}
 
