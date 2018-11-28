#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

std::string solve(){
    int N,M;
    cin >> N >> M;
    vector<int> nums100;
    vector<int> nums;
    vector<int> rowMax;
    vector<int> colMin;
    vector<int> colMax;
    vector<int> columns;
    colMin.resize(M);
    colMax.resize(M);
    for (int i=0;i<M;i++){
        colMin[i] = 1000;
        colMax[i] = -1;
    }
    for (int i=0;i<N;i++){
        for (int j=0;j<M;j++){
            int n;
            cin >> n;
            if (n < colMin[j])
                colMin[j] = n;
            if (n > colMax[j])
                colMax[j] = n;
            nums.push_back(n);
            nums100.push_back(1000);
        }
        int maxInRow = *max_element(nums.begin()+i*M, nums.begin()+(i+1)*M);
        rowMax.push_back(maxInRow);
//        cerr << maxInRow << endl;
    }

    string result;
    result = "YES";
    //ПО максимуму строк
    for (int i=0;i<N;i++)
        for (int j=0;j<M;j++)
            nums100[i*M+j] = rowMax[i];

    //По минимуму столбцов
    for (int j=0;j<M;j++){
        bool equal = true;
            for (int i1=0;i1<N;i1++)
                if (nums100[i1*M+j] != nums[i1*M+j])
                {
                    equal = false;
                    break;
                }
        if (!equal)
            for (int i=0;i<N;i++){
                nums100[i*M+j] = colMin[j];
            }
    }
    // Compare
    for (int i=0;i<N;i++)
        for (int j=0;j<M;j++)
            if (nums100[i*M+j] != nums[i*M+j])
            {
                result = "NO";
                break;
            }
    return result;
}

int main(int argc, char *argv[])
{
    int n;
    cin >> n;
    for (int i=1; i<=n;i++){
        cout << "Case #" << i << ": " << solve() << endl;
    }
    return 0;
}
