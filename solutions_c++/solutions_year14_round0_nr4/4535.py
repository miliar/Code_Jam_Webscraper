#include<fstream>
#include<set>
#include<cmath>
#include<vector>
#include<map>
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
        int N;
        cin >> N;
        vector<double> v1(N), v2(N);
        for(int i = 0 ; i < N; i++)
            cin >> v1[i];
        for(int i = 0 ; i < N; i++)
            cin >> v2[i];
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());
        /*
        for(int i = 0 ; i < N; i++)
            cout << v1[i] << " ";
        cout << endl;
        for(int i = 0 ; i < N; i++)
            cout << v2[i] << " ";
        cout << endl;*/
        int P1 = 0, P2 = 0;
        int k = 0;
        int end = N-1;
        for(int i = 0; i < N; i++)
        {
            if(v1[i] > v2[k])
            {
                P1++;
                k++;
            }
            else
            {
                end--;
                P2++;
            }
        }
        int p1 = 0, p2 = 0;
        for(int i = 0; i < N; i++)
        {
            int g = 1;
            for(int j = 0 ; j  < N; j++)
            {
                if (v2[j] > v1[i])
                {
                    p2++;
                    g = 0;
                    v2[j] = -10;
                    break;
                }
            }
            if(g) p1++;
        }
        v1.clear();
        v2.clear();
        
        cout << "Case #" << t <<": " << P1 <<  " " << p1 << endl;

    }
    return 0;
}
