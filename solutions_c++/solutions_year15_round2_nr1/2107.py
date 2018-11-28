#include<cstdio>
#include<climits>
#include<queue>

int num[10000000];

int Reverse(int x){
    int y=0;
    while(x!=0){
        y=y*10+x%10;
        x/=10;
    }
    return y;
}

int main(){
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2-output.txt","w",stdout);
    int t,in,temp;
    bool check;
    std::queue<int> bfs;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        scanf("%d",&in);
        num[1]=1;
        for(int j=2;j<10000000;j++){
            num[j]=INT_MAX;
        }
        while(!bfs.empty()){
            bfs.pop();
        }
        bfs.push(1);
        check=true;
        while(check){
            temp=bfs.size();
            for(int j=0;j<temp;j++){
                if(bfs.front()==in){
                    check=false;
                    break;
                }
                if(num[bfs.front()+1]>num[bfs.front()]+1){
                    num[bfs.front()+1]=num[bfs.front()]+1;
                    bfs.push(bfs.front()+1);
                }
                if(num[Reverse(bfs.front())]>num[bfs.front()]+1){
                    num[Reverse(bfs.front())]=num[bfs.front()]+1;
                    bfs.push(Reverse(bfs.front()));
                }
                bfs.pop();
            }
        }
        printf("Case #%d: %d\n",i,num[in]);
    }
    return 0;
}

