#include <bits/stdc++.h>
// 'Case #1: '
using namespace std;
    long long n,k,last;
    int vis[11];
    int i;
    int casesCount=0;
    bool finish;

    //0, 1, 2, 3, 4, 5, 6, 7, 8, and 9
int main()
{
    int tc;
    cin >> tc;
    ofstream myfile;
    myfile.open ("output.txt");
    while (tc--){
        casesCount++;
        i=0;
        cin >> n;
        if (n==0) {
             myfile << "Case #" << casesCount << ": INSOMNIA\n";
             continue;
        }
        std::fill(vis,vis+11,0);
        while (vis[10]!=10){
            i++;
            k = n*i;
            last = k;
            finish = false;
            while (k!=0&&!finish){
                int reminder = k%10;
                if (!vis[reminder]){
                   vis[reminder]=true;
                   vis[10]++;
                   if (vis[10]==10) finish = true;
                }
                k/=10;
            }
        }
        myfile << "Case #" << casesCount << ": "<< last << "\n";
    }
    return 0;
}
