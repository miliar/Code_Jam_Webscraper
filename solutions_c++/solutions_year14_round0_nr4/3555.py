#include<iostream>
#include<cstdlib>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
    freopen("test3.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int n;
    cin>> n;
    for(int j=0;j<n;j++){
        int nb;
        double temp;
        cin>>nb;
        vector<double>n;
        vector<double>k;
        
        for(int i=0;i<nb;i++){
            cin>>temp;
            n.push_back(temp);
        }
        for(int i=0;i<nb;i++){
            cin>>temp;
            k.push_back(temp);
            
        }
        sort(n.begin(),n.end());
        sort(k.begin(),k.end());
        int ws=0,ds=nb;
        
        for(int i=nb-1,l=nb-1;l>=0;l--){
            if(k[l] > n[i])
                ds--;
            else
                i--;
        }
        int s=0,e=nb-1;
        for(int i=nb-1;i>=0;i--){
            if(n[i] > k[e]){
                k[s]=0;
                s++;
                ws++;
            }else{
                for(int g=e;g>=0;g--){
                    if(k[g]<n[i]){
                        double temp=k[g+1];
                        k.erase(k.begin()+g+1);
                        k.push_back(temp);
                        e--;
                        break;
                    }
                }
            }        
        }
        cout<<"Case #"<<j+1<<": "<<ds<<" "<<ws<<endl;
    }

return 0;
}
