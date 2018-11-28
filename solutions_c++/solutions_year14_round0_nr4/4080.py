#include<cstdio>
#include<iostream>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<map>
#include<iomanip>

using namespace std;
#define getcx getchar_unlocked
#define scani(i) scanf("%d",&i)
#define scanl(i) scanf("%lld",&i)
#define LL long long
#define PB push_back
#define MP make_pair
#define all(a) a.begin(),a.end()

const double subtract=0.0000001;
int main(){
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        vector<double> naomi,ken;
        int n,DW_naomi=0,DW_ken=0,W_naomi=0,W_ken=0;
        double wt;
        cin>>n;
        for(int j=0;j<n;j++){
            cin>>wt;
            naomi.PB(wt);
        }
        for(int j=0;j<n;j++){
            cin>>wt;
            ken.PB(wt);
        }
        sort(all(naomi));
        sort(all(ken));

        /*for(int j=0;j<n;j++)
            cout<<naomi[j]<<"\t";
        cout<<"\n";
         for(int j=0;j<n;j++)
            cout<<ken[j]<<"\t";
        cout<<"\n";*/

        //cout<<"hi\n";
        int start_ken=0,end_ken=n-1;
        for(int j=0;j<n;j++){
            if(naomi[j]>ken[end_ken]){
                DW_naomi+=(n-j);
                break;
            }
            if(naomi[j]>ken[start_ken]){
                DW_naomi++;
                start_ken++;
            }
            else{
                DW_ken++;
                end_ken--;
            }
        }

        //cout<<"hi\n";
        for(int j=0;j<n;j++){
            int n_ken=ken.size();
            if(naomi[j]>ken[n_ken-1]){
                W_naomi+=(n-j);
                break;
            }
            //cout<<"hi\n";
            for(vector<double>::iterator it=ken.begin();it!=ken.end();it++){
                if(*it > naomi[j]){
                    W_ken++;
                    ken.erase(it);
                    break;
                }
            }
            //cout<<"hi\n";
        }
        cout<<"Case #"<<i+1<<": "<<DW_naomi<<" "<<W_naomi<<"\n";
        //cout<<"\t\t"<<DW_ken<<" "<<W_ken<<"\n";
    }
    return 0;
}
