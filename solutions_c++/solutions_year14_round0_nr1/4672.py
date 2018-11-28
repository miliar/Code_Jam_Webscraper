#include<fstream>
#include<set>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
    int T;
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        int N, M;
        cin >> N;
        vector<int> v;
        set<int> s;
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
            {
                int a;
                cin >> a;
                if(i == N-1)
                {
                    v.push_back(a);
                    s.insert(a);
                }
            }
        cin >> M;
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
            {
                int a;
                cin >> a;
                if(i == M-1)
                {
                    v.push_back(a);
                    s.insert(a);
                }
            }
        cout << "Case #" << t << ": ";
        if(s.size() == 8) cout << "Volunteer cheated!" << endl;
        if(s.size() < 7) cout << "Bad magician!" << endl;
        if(s.size() == 7)
        {
            sort(v.begin(),v.end());
            for(int i = 0; i < v.size(); i++)
            {
                if(v[i] == v[i+1])
                {
                    cout << v[i] << endl;
                    break;
                }
            }
        }
        v.clear();
        s.clear();
    }
    return 0;
}
