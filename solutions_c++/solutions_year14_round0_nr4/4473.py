//source here
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <map>
#include <string>

using namespace std;

const string ANS[3]={"", "Bad magician!", "Volunteer cheated!"};

int calls=0;



int main()
{
    FILE* fp=freopen("input.txt", "r", stdin);
    FILE* fp2=freopen("output.txt", "w", stdout);
    int cases;

    cin>>cases;
    for(int cn=1; cn<=cases; ++cn){
        int N, res1=0, res2=0;
        double tem;
        vector<double> naomi, ken;
        cin>>N;
        for(int i=0; i<N; ++i){
            cin>>tem;
            naomi.push_back(tem);
        }
        for(int i=0; i<N; ++i){
            cin>>tem;
            ken.push_back(tem);
        }
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());
        unsigned int i=0, j=0;
        while(i<ken.size()&&j<naomi.size()){
            if(naomi[j]>ken[i]){
                res1++;
                j++;
                i++;
                continue;
            }
            j++;
        }
        i=0;
        j=0;
        while(i<ken.size()&&j<naomi.size()){
            if(naomi[j]<ken[i]){
                res2++;
                j++;
                i++;
                continue;
            }
            i++;
        }
        res2=N-res2;
        //cout<<setprecision(7)<<fixed;
        cout<<"Case #"<<cn<<": "<<res1<<" "<<res2<<endl;

    }
    fclose(fp);
    fclose(fp2);
    return 0;
}
