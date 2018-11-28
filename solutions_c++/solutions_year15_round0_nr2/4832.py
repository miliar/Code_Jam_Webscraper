# include <bits/stdc++.h>

using namespace std;


int main(){
    int T; cin >> T;
    for(int t = 1; t <= T; ++t){
        int d; cin >> d;
        vector<int> mio(d);
        for(int i = 0; i < d; ++i)
            cin >> mio[i];
            
        sort(mio.begin(), mio.end());
        queue< pair<vector<int>, int> > Q;
        Q.push(make_pair(mio, 0));
        int supersol = 1 << 30;
        while(!Q.empty()){
            pair< vector<int>,int > tmp = Q.front();
            vector<int> current = tmp.first;
            int llevo = tmp.second;             
            supersol = min(llevo + current[current.size() - 1], supersol);
            Q.pop();
            //if(current[current.size() - 1] < 3) continue;
            for(int i = 1; i <= current[current.size() - 1]/2; ++i){
                vector<int> tmp_current = current;
                tmp_current[tmp_current.size() - 1] -= i;
                tmp_current.push_back(i);
                sort(tmp_current.begin(), tmp_current.end());
                tmp = make_pair(tmp_current, llevo + 1);
                if(tmp_current[tmp_current.size() - 1] > 1)
                    if(llevo + 1 < supersol)
                        Q.push(tmp);
            }
        }
        cout << "Case #" << t << ": " << supersol <<endl;
    }
    return 0;
}
