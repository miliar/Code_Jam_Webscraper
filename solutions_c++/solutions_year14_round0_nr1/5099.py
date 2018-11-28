#include<iostream>
//#include<fstream>

using namespace std;
int global_ans;

int trick(int c[4],int d[4]){
    int ret=0;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++){
            if(c[i]==d[j])  {
                ret++;
                global_ans=c[i];
                break;
            }
        }
    return ret;
}
int main(){
    int t,T, r=-1, a[4][4],b[4][4], c[4], d[4];
    cin>>t;
    T=1;
    while(t!=0){
        cin>>r;
        for(int i=0;i<4; i++)
            for(int j=0;j<4;j++)
                cin>>a[i][j];
        for(int k=0; k<4; k++)
            c[k]=a[r-1][k];
        cin>>r;
        for(int i=0;i<4; i++)
            for(int j=0;j<4;j++)
                cin>>b[i][j];
        for(int k=0; k<4; k++)
            d[k]=b[r-1][k];
        int ans = trick(c,d);
        if(ans==0)  cout<<"Case #"<<T++<<": Volunteer Cheated!"<<endl;
        if(ans==1)  cout<<"Case #"<<T++<<": "<<global_ans<<endl;
        if(ans>1)   cout<<"Case #"<<T++<<": Bad Magician!"<<endl;
        t--;
    }
    //in_file.close();
    //out_file.close();
return 0;}
