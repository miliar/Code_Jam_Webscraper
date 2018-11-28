# include<iostream>
# include<vector>
# include<algorithm>
using namespace std;

int m, n;
int lawn[101][101];
bool same_row(int x, int target) {
    for (int i=0; i< n; i++)
        if (lawn[x][i] != target)
            return false;
    return true;
}

bool same_col(int x, int target) {
    for (int k=0; k<m; k++)
        if (lawn[k][x] != target)
            return false;
    return true;
}

void mow_lawn(vector<vector<int > >  &a, int target) {
    //mow from left
    for (int i=0; i<m; i++) {
        if (same_row(i, target)) {
            for (int k=0; k< n; k++)
                a[i][k] = target;
        }
    }
    //mow from top
    for (int i=0; i<n; i++) {
        if (same_col(i, target)){
            //cerr << "same col " << i << " " << target << endl;
            for (int k=0; k<m; k++)
                a[k][i] = target;
        }
    }
}
bool result(vector<vector< int > > &a) {
    for (int i=0; i<m; i++) {
        for (int j=0; j<n; j++) {
            if (lawn[i][j] != a[i][j])
                return  false;
            }
        }
    return true;
}

int main() {
    freopen("input.txt", "rt", stdin);
    //freopen("output.txt", "wt", stdout);

    int t,kase=1;
    cin >> t;
    while (kase <= t) {
        cin >> m >> n;
        vector<int > numbers;
        vector<vector<int > > dummy(m, vector<int>(n));
        for (int i=0; i<m; i++)
            for (int j=0; j<n; j++) {
                cin >> lawn[i][j];
                numbers.push_back(lawn[i][j]);
            }

        sort(numbers.begin(), numbers.end());
        int last = numbers.size()-1;
        int max = numbers[last];
        for (int i=0; i<m; i++)
            for (int j=0; j<n; j++)
                dummy[i][j] = max;

        while (last > 0) {
            last--;
            mow_lawn(dummy, numbers[last]);
        }
       if(result(dummy))
            cout << "Case #" << kase++ << ": YES\n";
        else
            cout << "Case #" << kase++ << ": NO\n";

    }
    return 0;
}

