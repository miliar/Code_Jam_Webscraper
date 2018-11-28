#include<iostream>
#include<vector>

using namespace std; 

int main(){
    int T; 
    cin >> T; 
    for(int t = 1; t <= T; t++){
        int ans1,ans2; 
        cin >> ans1 ; 
        vector<vector<int> > v1(4),v2(4); 
        for(int i = 0; i < 4; i ++){
            for(int j = 0; j < 4;  j++){
                int temp ; 
                cin >> temp ; 
                v1[i].push_back(temp); 
            }
        }
        cin >> ans2; 
        for(int i = 0; i < 4; i ++){
            for(int j = 0; j < 4;  j++){
                int temp ; 
                cin >> temp ; 
                v2[i].push_back(temp); 
            }
        }

        vector<int> ans ; 
        vector<int> r1 = v1[ans1-1];
        vector<int> r2 = v2[ans2-1]; 
        for(int i = 0; i < r1.size(); i++){
            int n1 = r1[i]; 
            for(int j = 0;j < r2.size(); j++){
                if(n1 == r2[j])
                    ans.push_back(n1);
            }
        }
        cout << "Case #" << t << ": "; 
        if(ans.size() == 1)
            cout << ans[0] << endl; 
        else if(ans.size() == 0)
            cout << "Volunteer cheated!" << endl; 
        else 
            cout << "Bad magician!" << endl; 
    }
}
