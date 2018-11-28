#include <iostream>
#include <vector>

using namespace std;

vector<int> fractile(int k, int c, int s);

int main(){
    
    int numOfTest = 0;
    int count = 0;
    string line;

    if(getline(cin, line)){
        numOfTest = stoi(line);
    }
    else{
        cout << "No testcase is specified.\n";
        return 1;
    }

    while(getline(cin, line)) {

        string::size_type sz1;
        string::size_type sz2;
        int k = stoi(line, &sz1);
        int c = stoi(line.substr(sz1), &sz2);
        int s = stoi(line.substr(sz1 + sz2));

        // cout << "Debug: " << k << ", " << c << ", " << s << endl;

        vector<int> result = fractile(k, c, s);
        cout << "Case #" << ++count << ":";

        int size = result.size();
        if(size){
            for(int i = 0; i < size; i++){
                cout << " " << result[i];
            }
            cout << endl;
        }
        else{
            cout << " IMPOSSIBLE" << endl;
        }
    }

    return 0;

}

vector<int> fractile(int k, int c, int s){
    vector<int> ans;

    if(c == 1 && s < k){
        return ans;
    }
    else if(s >= k){
        for(int i = 0; i < k; i++){
            ans.push_back(i+1);
        }
        return ans;
    }

    /* For small test case */
    for(int i = 2; i < k; i++){
        ans.push_back(i);
    }

    return ans;
}
