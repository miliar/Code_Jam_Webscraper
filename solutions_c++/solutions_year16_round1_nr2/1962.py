#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <algorithm>
//#include <set>

using namespace std;

const int maxN = 100;
int lists[maxN][maxN];
int n,cases;



/*int solve2(vector<int>& result){
    unordered_map<int,vector<int>> firstMap;
    vector<int> firsts;
    vector<vector<int>> grid(n,vector<int>(n,0));
    for(int i = 0;i<cases;i++){
        firsts.insert(lists[i][0]);
        //if(firstMap.find(lists[i][0]) == firstMap.end()){
        firstMap[lists[i][0]].push_back(i);
    }
    sort(firsts.begin(),firsts.end());
    int start = firsts.front();
    int end = firsts.back();
    if(firstMap[start].size() == 2){
        int l1 = firstMap[start][0];
        int l2 = firstMap[start][1];
        for(int i = 0;i<n;i++){
            grid[0][i] = lists[l1][i];
            grid[i][0] = lists[l2][i];
        }
        for(int i = 2;i<n;i++){
            int listNum = grid[0][i];

        }
    }

    grid[0] =
    return 0;
}*/

int solve(vector<int>& result){
    unordered_map<int,int> counts;
    for(int i = 0;i<cases;i++){
        for(int j = 0;j<n;j++){
            counts[lists[i][j]]++;
        }
    }
    for(auto it = counts.begin();it != counts.end();it++){
        if(it->second %2 == 1)
            result.push_back(it->first);
    }
    sort(result.begin(),result.end());
}

/*void getSubString(string& s,int index,string currRes){
    if(currRes.length() == s.length())
        if(currRes < result) result = currRes;
}*/

int main()
{
    ifstream in("large.txt");
    ofstream out("largeout.txt");
    //ifstream in("in.txt");
    //ofstream out("out.txt");
    if (! in.is_open()){
        cout << "Error opening file";
    }
    int t;
    string s;
    //int n;
    in>>t;
    //vector<int> result;
    int lineCount = 1;
    while(t--){
        in>>n;
        cases = 2*n-1;
        for(int i = 0;i<cases;i++){
            //in>>lists[i][0]>>lists[i][1]>>lists[i][2];
            for(int j = 0;j<n;j++)
                in>>lists[i][j];
        }
        vector<int> result;
        solve(result);
        out<<"Case #"<<lineCount<<":";
        for(auto re:result) out<<" "<<re;
        out<<endl;
        lineCount ++;
    }
    //for(auto ele:result)
    //    out<<ele<<endl;
    in.close();
    out.close();
    return 0;
}
