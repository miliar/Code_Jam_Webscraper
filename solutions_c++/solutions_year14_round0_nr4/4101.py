#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

int dwar(vector<double> & nm, vector<double> & ken){
    int nb = 0;
    int kb = 0;
    int ne = nm.size()-1;
    int ke = ken.size()-1;
    int ans = 0;
    while(nb<=ne){
        if(nm[nb]>ken[kb]){//if NaoMi can dominate Ken
            ans ++;
            nb++;
            kb++;
        }
        else{
            nb++;
            ke--;
        }
    }
    return ans;
}

int war(vector<double> & nm, vector<double> & ken){
    int nb = 0;
    int kb = 0;
    int ne = nm.size()-1;
    int ke = ken.size()-1;
    int ans = 0;
    while(nb<=ne){
        if(nm[ne]>ken[ke]){//if NaoMi can dominate Ken
            ans ++;
            ne--;
            kb++;
        }
        else{
            ne--;
            ke--;
        }
    }
    return ans;
}

int main(){
    int t;
    scanf ("%d",&t);
    for(int i=1;i<=t;i++){
        int size;
        scanf("%d\n",&size);
        vector<double> ken;
        vector<double> nm;
        for(int j=0;j<size;j++){
            double w;
            scanf("%lf", &w);
            nm.push_back(w);
        }
        for(int j=0;j<size;j++){
            double w;
            scanf("%lf", &w);
            ken.push_back(w);
        }
        sort(nm.begin(), nm.end());
        sort(ken.begin(), ken.end());
        printf("Case #%d: %d %d\n", i, dwar(nm, ken), war(nm, ken));
    }
}