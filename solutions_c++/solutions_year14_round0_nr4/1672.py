#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int war(vector<double> nao, vector<double> ken)
{
    int nao_point = 0;
    for(int i = nao.size() - 1; i >= 0; i --) {
        // Find the location of nao[i] in ken;
        int j;
        for(j = ken.size() - 1; j >= 0; j --) {
            if(nao[i] > ken[j]) break;
        }

        // When nao[i] is larger than anything in ken[j]
        if(j == ken.size() - 1) {
            nao_point ++;

            // Remove the first element of ken (give the smallest one)
            ken.erase(ken.begin(), ken.begin() + 1);

            continue;
        }
        ken.erase(ken.begin() + j + 1, ken.begin() + j + 2);
    }
    return nao_point;
}
int optimized(vector<double> nao, vector<double> ken)
{
    int nao_point = 0;
    int i = 0;

    // Keep ken[0] as the smallest element
    while (i < ken.size()) {
        int j;
        for(j = 0; j < nao.size(); j ++) {
            if(ken[i] < nao[j]) break;
        }
        // When everything of ken[i] is larger
        // than nao's element
        if(j == nao.size()) {
            return nao_point;
        }

        nao_point ++;
        
        nao.erase(nao.begin() + j, nao.begin() + j + 1);
        ken.erase(ken.begin() + i, ken.begin() + i + 1);
    }

    return nao_point;
}
int main()
{
    int tc, ori_tc;
    cin >> tc;

    ori_tc = tc;

    while (tc) {
        int num_block;
        cin >> num_block;

        vector<double> nao (num_block);
        vector<double> ken (num_block);

        for(int i = 0; i < num_block; i ++)
            cin >> nao[i];

        for(int i = 0; i < num_block; i ++)
            cin >> ken[i];
        
        sort(nao.begin(), nao.end());
        sort(ken.begin(), ken.end());

        cout << "Case #" << ori_tc - tc + 1 << ": " << optimized(nao, ken) << " " << war(nao, ken) << endl;
        tc --;
    }
}
