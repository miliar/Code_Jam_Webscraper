#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

#define fo(i, j) for(int i = 1; i < j; i++)


struct litera{
    char letter;
    int count, N;
};

class TheRepeater{
private:
    vector< vector<litera> > a;
    int count, T, N;

public:
    TheRepeater(){
        count = T = 0;
    }

    void run(){
        cin >> T;

        for(int i = 0; i < T; i++){
            cout << "Case #" << i+1 << ": ";
            solve();
        }

    }

    void solve(){
        string x;
        a.clear();

        cin >> N;
        for(int i = 0; i < N; i++)
        {
            cin >> x;
            litera temp;
            vector<litera> t;

            temp.letter = x[0];
            temp.count = 1;
            t.push_back(temp);

            fo(i, int(x.length())){
                if(x[i-1] == x[i])
                    t[t.size()-1].count++;
                else{
                    temp.letter = x[i];
                    temp.count = 1;
                    t.push_back(temp);
                }
            }
            a.push_back(t);
        }

        check();
    }

    void check(){
        int t = a[0].size();
        count = 0;
        for(int i = 1; i < a.size(); i++)
            if(a[i].size() != t){
                cout << "Fegla Won" << endl;
                return;
            }

        int max[t];

        for(int i = 0; i < t; i++)
        {

            max[i] = 0;
            for(int j = 0; j < a.size(); j++)
            {
                if(j > 0) if(a[j][i].letter != a[j-1][i].letter) { cout << "Fegla Won" << endl; return; }
                max[i] += a[j][i].count;
                //max[i] = (a[j][i].count > max[i]) ? a[j][i].count : max[i];
            }
            max[i] /= a.size();

        }

        for(int i = 0; i < t; i++)
        {
            for(int j = 0; j < a.size(); j++)
            {
                count += abs(max[i] - a[j][i].count);
            }

        }

        cout << count << endl;
    }
};
