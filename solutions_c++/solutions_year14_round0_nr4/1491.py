#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    long long int t;
    cin >> t;
    for(long long int q=1;q<=t;++q){
        vector<double> naomi;
        vector<double> ken;
        long long int naomi_war, naomi_dwar=0;
        long long int n;
        cin >> n;
        for(long long int i=0;i<n;++i){
            double temp;
            cin >> temp;
            naomi.push_back(temp);
        }
        for(long long int i=0;i<n;++i){
            double temp;
            cin >> temp;
            ken.push_back(temp);
        }
        sort(naomi.begin(),naomi.end());
        sort(ken.begin(),ken.end());
        /*vector<double> copy_ken;
        for(long long int i=0;i<n;++i){
            copy_ken.push_back(ken[i]);
        }*/
        long long int ken_war=0;
        for(long long int i=0,j=0;j<n;++j){
            if(ken[j]>naomi[i])
                {ken_war++;i++;}
        }
        naomi_war=(n-ken_war);
        for(long long int i=n-1;i>=0;--i){
            if(ken[i]==0.99999)
            {
                naomi.erase(naomi.begin());
                ken.erase(ken.begin()+i);
            }
            else if(naomi[i]>ken[i])
                naomi_dwar++;
            else
            {
                naomi.erase(naomi.begin());
                ken.erase(ken.begin()+i);
            }
        }
        cout << "Case #" << q << ": " << naomi_dwar << " " << naomi_war << endl;
    }
    return 0;
}
