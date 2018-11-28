#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
struct Node{
    double v;
    int d;
    bool operator ==(const Node &b) const{
        return v==b.v;
    }
    bool operator <(const Node &b) const{
        return v<b.v || (v==b.v && d<b.d);
    }
};
vector<Node> a,b;
int main(){
    a.push_back((Node){1,0});
    a.push_back((Node){0,0x3fff});
    for (int k=0;k<11;k++){
        int len=a.size();
        for (int i=0;i<len;i++)
            for (int j=0;j<len;j++){
                //cout << a[i].v << " " << a[j].v << " " << a[i].d << " " << a[j].d << endl;
                a.push_back((Node){(a[i].v+a[j].v)/2,
                            (a[i].v==1||a[j].v==1)?1:min(a[i].d,a[j].d)+1});
            }
        sort(a.begin(),a.end());
        a.erase(unique(a.begin(),a.end()),a.end());

    }
    /*
    for (int i=0;i<a.size();i++)
        cout << a[i].v << "," << a[i].d << " ";
    cout << endl;
    */
    double p,q;
    int n,t=0;
    scanf("%d",&n);
    while (scanf("%lf/%lf",&p,&q)!=EOF){
        int x=-1;
        for (int i=0;i<a.size();i++)
            if (a[i].v==p/q){
                x=a[i].d;
                break;
            }
        printf("Case #%d: ",++t);
        if (x==-1)
            printf("impossible\n");
        else
            printf("%d\n",x);
    }
    return 0;
}
