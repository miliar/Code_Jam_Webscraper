#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
    int t,c=1;
    cin >> t;
    while(t--){
        int ar[5][5],br[5][5];
        int i,j,k,l,m,n,d=0,p,o;
        vector<int>v1,v2;
        cin >> k;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                cin >> m;
                ar[i][j]=m;
            }
        }
        for(i=0;i<4;i++){
            v1.push_back(ar[k-1][i]);
        }
        cin >> p;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                cin >> m;
                br[i][j]=m;
            }
        }
        for(i=0;i<4;i++){
            v2.push_back(br[p-1][i]);
        }
        for(i=0;i<v1.size();i++){
            for(j=0;j<v2.size();j++){
                if(v1[i]==v2[j]){
                    d++;
                    o=v1[i];
                }
            }
        }
        if(d==0)
            cout << "Case #" << c << ": Volunteer cheated!" << endl;
        if(d==1)
            cout << "Case #" << c << ": " << o << endl;
        if(d>1)
            cout << "Case #" << c << ": Bad magician!" << endl;
        c++;
    }
    return 0;
}
