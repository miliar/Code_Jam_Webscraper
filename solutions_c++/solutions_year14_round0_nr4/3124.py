#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

int d_war_func(vector<double>m,vector<double>n){
      int d_war=0,c,j,k;
     while(m.size()>0 && n.size()>0){
        if(m[m.size()-1]>n[n.size()-1]){
            m.erase(m.begin()+m.size()-1);
            n.erase(n.begin()+n.size()-1);
            d_war++;
        }
        else{
            m.erase(m.begin());
            n.erase(n.begin()+n.size()-1);
        }
     
     }

    return d_war;
}
int war_func(vector<double>m,vector<double>n){
   int flag=0,war=0;
    for(int i=0;i<m.size();i++){
        flag=0;
        for(int j=0;j<n.size();j++){
            if(n[j]>m[i]){
                n.erase(n.begin()+j);
                flag=1;
                break;
            }
        
        }
        if(flag==0) war++;
        }
        return war;

}
int main(){
    int T,Y;
    vector<double>m;
    vector<double>n;
    scanf("%d",&T);
    Y=T;
    while(T--){
        int num;
        double a;
        scanf("%d",&num);
        for(int i=0;i<num;i++){
            scanf("%lf",&a);
            m.push_back(a);
        }
        for(int i=0;i<num;i++){
            scanf("%lf",&a);
            n.push_back(a);
        }
        sort(m.begin(),m.end());
        sort(n.begin(),n.end());
       
       printf("Case #%d: %d %d\n",Y-T,d_war_func(m,n),war_func(m,n));
        m.clear();
        n.clear();
    }

}
