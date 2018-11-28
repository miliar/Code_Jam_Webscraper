#include <bits/stdc++.h>

using namespace std;

#define pb push_back

int T;
string s;
vector<int> ans;
int ta[1000] = {0};
int temp[1000] = {0};

int main(){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	cin>>T;
	for(int t = 1; t <= T; t++){
        cin>>s;
        ans.clear();
        for(int i = 0; i < 1000; i++){
            ta[i] = temp[i] = 0;
        }

        for(int i = 0; i < s.length(); i++){
            ta[s[i]]++;
        }
        for(int i = 0; i < s.length(); i++){
            if(s[i] == 'Z'){
                temp['Z']++;
                temp['E']++;
                temp['R']++;
                temp['O']++;
                ans.pb(0);
            }
            else if(s[i] == 'W'){
                temp['T']++;
                temp['W']++;
                temp['O']++;
                ans.pb(2);
            }
            else if(s[i] == 'U'){
                temp['F']++;
                temp['O']++;
                temp['U']++;
                temp['R']++;
                ans.pb(4);
            }
            else if(s[i] == 'X'){
                temp['S']++;
                temp['I']++;
                temp['X']++;
                ans.pb(6);
            }
            else if(s[i] == 'G'){
                temp['E']++;
                temp['I']++;
                temp['G']++;
                temp['T']++;
                temp['H']++;
                ans.pb(8);
            }
        }
        for(int i = 0; i < 1000; i++){
            temp[i] = ta[i] - temp[i];
        }
        for(int i = 0; i < s.length(); i++){
            if(s[i] == 'O' && temp['O'] > 0){
                ans.pb(1);
                temp['N']--;
                temp['O']--;
                temp['E']--;
            }
            else if(s[i] == 'T' && temp['T'] > 0){
                ans.pb(3);
                temp['T']--;
                temp['H']--;
                temp['R']--;
                temp['E']--;
                temp['E']--;

            }else if(s[i] == 'F' && temp['F']  > 0){
                ans.pb(5);
                temp['F']--;
                temp['I']--;
                temp['V']--;
                temp['E']--;

            }else if(s[i] == 'S' && temp['S']  > 0){
                ans.pb(7);
                temp['S']--;
                temp['E']--;
                temp['V']--;
                temp['E']--;
                temp['N']--;
            }
        }
        for(int i = 0; i < s.length(); i++){
            if(s[i] == 'I' && temp['I'] > 0){
                temp['I']--;
                ans.pb(9);
            }
        }


        sort(ans.begin(), ans.end());

        cout<<"Case #"<<t<<": ";
        for(int i = 0; i < ans.size(); i++){
            cout<<ans[i];
        }
        cout<<endl;
	}

	return 0;
}
