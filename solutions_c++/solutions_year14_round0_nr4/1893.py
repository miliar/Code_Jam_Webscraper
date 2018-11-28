#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<map>
#include<stack>

using namespace std;

int main(){
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int t;
    cin >> t;
    for(int zz=1;zz<=t;zz++){
        int cheat=0,normal=0;
        int n;
        cin >> n;
        vector<double> a,b;
        map<double,int> m;
        for(int i=0;i<n;i++){
            double temp;
            scanf("%lf",&temp);
            a.push_back(temp);
            m[temp] = 1;
        }
        for(int i=0;i<n;i++){
            double temp;
            scanf("%lf",&temp);
            b.push_back(temp);
            m[temp] = 2;
        }

        stack<int> seq;

        int count=0;
        for(auto &x : m){
            //printf("%.6f %d\n",x.first,x.second);
            //printf("%d ",x.second);
            seq.push(x.second);
            if(x.second==1) count++;
            else{
                if(count>0){
                    count--;
                    normal++;
                }
            }
        }
        normal = n-normal;
        //printf("\n");
        count=0;
        while(!seq.empty()){
            int temp = seq.top(); seq.pop();
            if(temp==1) count++;
            else{
                if(count>0){
                    count--;
                    cheat++;
                }
            }
        }


        printf("Case #%d: %d %d\n",zz, cheat, normal);
    }
}
