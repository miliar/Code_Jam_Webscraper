#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;
struct sort_pred {
    bool operator()(const std::pair<int,int> &left, const std::pair<int,int> &right) {
        return left.second > right.second;
    }
};
int main()
{
    int t;
    cin >> t;
    int test = t;
    while(t--)
    {
        cout << "Case #" << test - t << ": ";
        int n , total = 0;
        cin >> n;
        int a[26];
        map<int , char , greater<int> > m;
        vector<pair<int , int> > V;
        for(int i = 0 ; i < n ; i++){
            cin >> a[i];
            m[i + 'a'] = a[i];
            total += a[i];
            V.push_back(make_pair(i , a[i]));
        }
        //cout << V[0].first << " " << V[0].second;
        sort(V.begin() , V.end() , sort_pred());
        int k = 0;
        while(1) {
            if(total <= 0)
                break;
            char ch = toupper(V[0].first + 'a');
            int per = (V[0].second * 100)/total;
            if(per > 50) {
                    cout << ch;
                    V[0].second = V[0].second - 1;
                    total--;
                    k++;
            }
            else {
                if(k == 0)
                    cout << ch;
                else
                    cout << " " << ch;
                V[0].second = V[0].second - 1;
                total--;
                k++;
            }
                sort(V.begin() , V.end() , sort_pred());

        }
        cout << endl;
    }
    return 0;
}
