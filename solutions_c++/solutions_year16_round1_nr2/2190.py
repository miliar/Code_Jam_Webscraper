#include <iostream>
#include<fstream>
#include<algorighm>
using namespace std;
int a[55][55],b[55][55],ans[55];
bool cmp(int x,int y){
    return x>y;
}
int main()
{
    ifstream in;
    ofstream out;
    in.open("in.txt");
    out.open("out.txt");
    int t,n,q=0;
    in>>t;
    while(t--){
        q++;
        in>>n;
        for(int i=1;i<n;i++){
            for(int j=1;j<=n;j++){
                in>>a[i][j];
                cout<<a[i][j]
            }
        }
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                in>>b[i][j];
            }
        }
        for(int i=1;i<n;i++){
            for(int j=1;j<=n;j++){
                bool bb=false;
                for(int k=1;k<=n;k++){
                    if(bb)break;
                    for(int s=1;s<=n;s++){
                        if(a[i][j]==b[k][s]){
                            b[k][s]=0;
                            bb=true;
                        }
                    }
                }
            }
        }
        int s=1;
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                if(b[i][j]!=0)ans[s++]=b[i][j];
            }
        }
        sort(ans,ans+n);
        out<<"Case #"<<q<<": "<<endl;
        for(int i=1;i<=n;i++){
            if(i>1)out<<" ";
            out<<ans[i];
        }
        out<<endl;
    }
    in.close();
    out.close();
    return 0;
}
