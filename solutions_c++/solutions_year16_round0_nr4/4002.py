#include <iostream>

#define MAXM 1000100
#define dfr(i,a,b) for(int i=a;i<b;i++)


using namespace std;

int BIArray[MAXM],a[MAXM];
int n;

void update(int pos,int val){
    while(pos<=n){
        BIArray[pos]+=val;
        pos+=pos&(-pos);
    }
}
int getSum(int pos){
    int sum=0;
    while(pos>0){
        sum+=BIArray[pos];
        pos-=pos&(-pos);
    }
    return sum;
}
int main()
{
    ios::sync_with_stdio(false);
    int t;
    cin>>t;
    while(t--){
        cin>>n;
        dfr(i,1,n+1){
            cin>>a[i];
            update(i,a[i]);
        }
        dfr(i,1,n+1){
            cout<<BIArray[i]<<' ';
        }
        cout<<endl;

    }

}
