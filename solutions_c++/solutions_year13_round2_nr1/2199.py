#include<cstdio>
#include<algorithm>
using namespace std;
int arr[20];
int N;
int mini;
void proc(int currentnode, int currentreq, int currentsize){
    if(currentnode == N){
        mini = min(currentreq,mini);
        return;
    }else{
        if(arr[currentnode]<currentsize){
            proc(currentnode+1,currentreq,currentsize+arr[currentnode]);
            //printf("option 1\n");
        }
        else if(arr[currentnode]<currentsize+currentsize-1){
            proc(currentnode+1,currentreq+1,currentsize+currentsize-1+arr[currentnode]);
            //printf("go here\n");
        }
        else{
            proc(currentnode+1,currentreq+1,currentsize);
            if(currentsize!=1){
                while(currentsize<=arr[currentnode]){
                currentsize = currentsize + currentsize - 1;
                currentreq++;
                }
                proc(currentnode+1,currentreq,currentsize+arr[currentnode]);
            }
        }
    }
}

int main(void){
    freopen("A-small-attempt3.in","r",stdin);
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tc, casecounter = 1;
    int req;
    int tempreq, tempsize;

    int armin;
    scanf("%d",&tc);
    while(tc--){
        req = 0;
        scanf("%d %d",&armin,&N);
        for(int i=0;i<N;i++){
            scanf("%d",&arr[i]);
        }
        sort(arr,arr+N);
        //for(int i=0;i<N;i++)printf("%d ",arr[i]);
        //printf("\n");
        tempsize = armin;
        mini = 10000;
        proc(0,0,armin);
        /*for(int i=0;i<N;i++){
            if(armin>arr[i]){
                armin+=arr[i];
            }else{
                if(armin + armin - 1 > arr[i]){
                    req++;
                    armin = armin + armin - 1 + arr[i];
                }
                else req++;
            }

        }*/



        printf("Case #%d: %d\n",casecounter++,mini);
    }

    return 0;
}
