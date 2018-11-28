#include<bits/stdc++.h>
using namespace std;

int main(){
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int i,k,cases;
    cin>>cases;
    for(k=1;k<=cases;k++){
        int n;
        double v,x;
        cin>>n>>v>>x;
        double r[n],c[n],t[n];
        for(i=0;i<n;i++){
            cin>>r[i]>>c[i];
        }
        cout<<"Case #"<<k<<": ";
        if(n==1){
            if(x==c[0]){
                t[0]=v/r[0];
                printf("%.8lf\n",t[0]);
            }
            else{
                cout<<"IMPOSSIBLE"<<endl;
            }
        }
        else{
            if(c[0]==c[1]){
                if(x==c[0]){
                    t[0]=v/(r[0]+r[1]);
                    printf("%.8lf\n",t[0]);
                }
                else{
                    cout<<"IMPOSSIBLE"<<endl;
                }
            }
            else{
                t[1]=(x-c[0])/(c[1]-c[0]);
                t[0]=v * (1.0 - t[1]);
                t[1]=v * t[1];
                t[1]=t[1]/r[1];
                t[0]=t[0]/r[0];
                if(t[0]<0||t[1]<0){
                    cout<<"IMPOSSIBLE"<<endl;
                }
                else{
                    if(t[0]>t[1]){
                        printf("%.8lf\n",t[0]);
                    }
                    else{
                        printf("%.8lf\n",t[1]);
                    }
                }
            }
        }
    }
}
