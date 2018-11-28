/*
* abdurak
* Google CodeJam 2014 - Round 2
* Problem C
* Game after game after game...
*/
#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <utility>

#define pi pair<int,int>
#define vpi vector<pair<int,int> >

#define forn(i,n) for(int i=0;i<n;i++)
#define forr(i,a,b) for(int i=a;i<=b;i++)
#define forn2(i,ni,j,nj) forn(i,ni) forn(j,nj)

//DEBUGGING
#define _s cout<<
#define _d <<" "<<
#define _e <<endl;
long long INF=100000000000LL;

//(int *)calloc(1000000,sizeof(int));
//(int *)malloc(1000000*sizeof(int));

using namespace std; 
ifstream fin ("C.in");
ofstream fout ("C.out");

int mincost;
int W,H,B;
int *ls=(int*)malloc(1002*1002*sizeof(int));

void rec(int x,int isvis[1000],int cost){
    if(mincost>cost+ls[1002*x+1001])
        mincost=cost+ls[1002*x+1001];
    for(int i=0;i<B;i++){
        if(isvis[i]==0){
            isvis[i]=1;
            rec(i,isvis,cost+ls[x*1002+i]);
            isvis[i]=0;
        }
    }
}

int main(){
    int T;
    fin>>T;
    forr(iT,1,T){
        fout<<"Case #"<<iT<<": ";
        fin>>W>>H>>B;
        mincost=W;
        int x1[1000],x2[1000],y1[1000],y2[1000];
        forn(i,B){
            int a,b,c,d;
            fin>>a>>b>>c>>d;
            x1[i]=a;y1[i]=b;
            x2[i]=c+1;y2[i]=d+1;
        }
        ls[1002*1000+1001]=W;
        ls[1002*1001+1000]=W;
        for(int i=0;i<B;i++){
            ls[1002*i+i]=0;
            ls[1002*1000+i]=x1[i];
            ls[1002*i+1000]=x1[i];
            ls[1002*1001+i]=W-x2[i];
            ls[1002*i+1001]=W-x2[i];
            for(int j=0;j<B;j++){
                if(i==j) continue;
                if(x1[i]<x2[j]&&x1[j]<x2[i]){
                    if(y1[i]<y1[j]){
                        ls[1002*i+j]=y1[j]-y2[i];
                        ls[1002*j+i]=y1[j]-y2[i];
                    }else{
                        ls[1002*i+j]=y1[i]-y2[j];
                        ls[1002*j+i]=y1[i]-y2[j];
                    }
                }
                else if(y1[i]<y2[j]&&y1[j]<y2[i]){
                    if(x1[i]<x1[j]){
                        ls[1002*i+j]=x1[j]-x2[i];
                        ls[1002*j+i]=x1[j]-x2[i];
                    }else{
                        ls[1002*i+j]=x1[i]-x2[j];
                        ls[1002*j+i]=x1[i]-x2[j];
                    }
                }
                else{
                    if(x1[i]<x1[j]){
                        if(y1[i]<y1[j]){
                            ls[1002*i+j]=max(x1[j]-x2[i],y1[j]-y2[i]);
                            ls[1002*j+i]=max(x1[j]-x2[i],y1[j]-y2[i]);
                        }else{
                            ls[1002*i+j]=max(x1[j]-x2[i],y1[i]-y2[j]);
                            ls[1002*j+i]=max(x1[j]-x2[i],y1[i]-y2[j]);
                        }
                    }else{
                        if(y1[i]<y1[j]){
                            ls[1002*i+j]=max(x1[i]-x2[j],y1[j]-y2[i]);
                            ls[1002*j+i]=max(x1[i]-x2[j],y1[j]-y2[i]);
                        }else{
                            ls[1002*i+j]=max(x1[i]-x2[j],y1[i]-y2[j]);
                            ls[1002*j+i]=max(x1[i]-x2[j],y1[i]-y2[j]);
                        }
                    }
                }
            }
        }
        cout<<endl;
        for(int i=0;i<B;i++){
            for(int j=0;j<B;j++){
                cout<<ls[1002*i+j]<<" ";
            }
            cout<<endl;
        }
        int isv[1000]={0};
        rec(1000,isv,0);
        cout<<mincost;
        fout<<mincost;
        fout<<endl;
    }
    system("pause");
	return 0;
}
