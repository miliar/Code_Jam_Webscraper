#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(vector<int> A, vector<int> B){
    return A[0] < B[0];
}
void solve(vector<vector<int> > vals, int i ){
    vector<int> result;
    
    cout << "Case #"<<i+1<< ": ";
    for (int j = 0; j < result.size(); j++)
        cout << result[i];
    cout << endl;

}
int main(int argc, char **argv)
{
    int test_cnt = 0;
    scanf("%d", &test_cnt);
    for (int i = 0; i < test_cnt; i++){
        int cnt = 0;
        scanf("%d", &cnt);
        vector<int> result;
        int vals[2501]={0};
        for (int j = 0; j < 2 * cnt - 1; j++){
            for (int k = 0; k < cnt; k++){
                int tmp;
                scanf("%d", &tmp);
                vals[tmp]++;
            }
        }
        for (int j = 1; j <=2500; j++ ){
            //cout << "vals ["<<j <<"]"<< vals[j] << endl;
            if (vals[j] % 2 == 1)
                result.push_back(j);
        }
        sort(result.begin(),result.end());
        cout << "Case #"<<i+1<< ": ";
        for (int j = 0; j < result.size(); j++)
            cout << result[j] <<" ";
        cout << endl;
        
        // prepare for next
        for (int j = 0; j < 2501 ; j++)
            vals[j] = 0;
        result.clear();
        
    }
    return 0;
}

