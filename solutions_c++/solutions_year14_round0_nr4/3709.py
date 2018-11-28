#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<double> na;
vector<double> ke;

int n;

int main(){
    freopen ("dlarge.out","w",stdout);
    int t;
    cin>>t;
    for (int tc=1;tc<=t;tc++){
        cin>>n;
        na.clear();
        ke.clear();
        for (int i=0;i<n;i++){
            double a;
            cin>>a;
            na.push_back(a);
        }
        for (int i=0;i<n;i++){
            double a;
            cin>>a;
            ke.push_back(a);
        }
        sort(na.begin(),na.end());
        sort (ke.begin(),ke.end());
        int i2=0;
        int i;
        for (i=0;i<n&&i2<n;i++){
            if (na[i]>ke[i2]){
                i--;
            }
            i2++;
        }
        int v1=n-i;
        int mp=0;
        for (int a=0;a<n;a++){
            int i2=0;
            int i;
            int v=0;
            for (i=0;i<n;i++){
                if (a+i<n){
                    if (na[a+i]>ke[i]){
                        v++;
                    }
                }
            }
            mp=max(mp,v);
        }
        cout <<"Case #"<<tc<<": ";
        cout <<mp<<" "<<v1<<endl;
    }
}
