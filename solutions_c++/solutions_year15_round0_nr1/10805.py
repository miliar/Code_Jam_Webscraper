#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <list>

int main()
{
    using namespace std;

    char num;
    int start;
    int count = 0;
    vector<int> tmpVector;
    int nTest,intNum;
    cin >> start;
    nTest = start;
    while (cin >> num){
        intNum = (int)(num - '0');
        tmpVector.push_back(intNum);
    }
    vector<vector<int>> audience;
    for(int i=0;i<tmpVector.size();i++){
        vector<int> audi;
        int maxShy = tmpVector[i];
        for(int k=0;k<maxShy+1;k++){
            audi.push_back(tmpVector[i+k+1]);
        }
        audience.push_back(audi);
        i = i + maxShy + 1;
    }
    for(int i=0;i<audience.size();i++){
        int nFriend = 0;
        int currentStand = 0;
        for(int j=0;j<audience[i].size();j++){
            if(currentStand >= j){
                currentStand = currentStand + audience[i][j];
            }
            else{
                int lack = j - currentStand;
                nFriend = nFriend + lack;
                currentStand = currentStand + audience[i][j] + lack;
            }
        }
        cout << "Case #" << i+1 << ": " << nFriend << endl;
    }
    
    return 0;
}