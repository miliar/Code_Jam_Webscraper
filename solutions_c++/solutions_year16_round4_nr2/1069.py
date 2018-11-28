#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

double p[1000];
double maxp = 0;
void nchoosekp(int n, int k, vector<int> &path,vector<int> &pathp, int level, int curv, double &sump);
void nchoosek(int n, int k, vector<int> &path, int level, int curv)
{
    if (path.size() == k) {
        //Do something
        double sump = 0;
        vector<int> pathp;
        nchoosekp(k, k/2, path, pathp, 0, -1, sump);
        if (sump > maxp)
            maxp = sump;
    }
    for (int i=curv+1; i<n; i++)
    {
        path.push_back(i);
        nchoosek(n, k , path, level+1, i);
        path.pop_back();
    }
}
void nchoosekp(int n, int k, vector<int> &path,vector<int> &pathp, int level, int curv, double &sump)
{
    if (pathp.size() == k) {
        double mul = 1;
        for (int i=0; i<k; i++)
        {
            mul *= p[path[pathp[i]]];
//            cout << i <<" ";
//            cout << pathp[i] << " ";
//            cout << path[pathp[i]] <<" ";
//            cout << p[path[pathp[i]]]<<endl;
//            cout <<mul <<endl;
        }
        for (int i=0;i<n;i++)
        {
            int flag = 1;
            for (int j=0;j<k; j++)
                if (pathp[j] == i)
                {
                    flag = 0;
                    break;
                }
            if (flag)
                {mul *= (1-p[path[i]]);//cout << (1-p[path[i]]) <<endl;cout <<mul <<endl;}
        }


        }
        //printf("%.2lf\n",mul);
        //cout <<mul;
        sump += mul;
    }
    for (int i=curv+1; i<n; i++)
    {
        pathp.push_back(i);
        nchoosekp(n, k , path, pathp, level+1, i, sump);
        pathp.pop_back();
    }
}
int main()
{
    vector<int> path;
    //nchoosek(16,8,path,0, -1);
    int tt;
    cin >>tt;
    for (int tc=1; tc<=tt; tc++)
    {
        int n, k;
        cin >> n >> k;

        for (int i=0;i<n;i++)
            cin >> p[i];
        //cout << p[0] << p[1];
        maxp = 0;

        nchoosek(n,k,path, 0,-1);
        //printf("Case #%d: %.2lf\n", tc, maxp);
        cout << "Case #" << tc << ": " << maxp << endl;
    }
    return 0;
}
