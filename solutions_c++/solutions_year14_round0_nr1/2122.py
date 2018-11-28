#include<iostream>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<iomanip>

#define sd(x) scanf("%lld",&x)
#define MP make_pair
#define PB push_back
#define MOD 100000007
#define INF 100000007
#define M 1000000
#define F first
#define S second
#define ll long long
#define LL long long

using namespace std;
int a[20], b[5][5];
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t, op = 1;
    cin>>t;
    while(t--){
        cout<<"Case #"<<op<<": ";
        op++;
        int x, y, ans = 0, i, j;
        for(i = 0; i <= 16; i++){
            a[i] = 0;
        }
        cin>>x;
        for(i = 0; i < 4; i++){
            for(j = 0; j < 4; j++){
                cin>>b[i][j];
            }
        }
        x--;
        for(j = 0; j < 4; j++){
            a[b[x][j] ]++;
        }
        cin>>x;
        for(i = 0; i < 4; i++){
            for(j = 0; j < 4; j++){
                cin>>b[i][j];
            }
        }
        x--;
        for(j = 0; j < 4; j++){
            a[b[x][j] ]++;
        }
        for(i = 0; i <= 16; i++){
            if(a[i] == 2){
                ans ++;
                y = i;
            }
        }
        if(ans == 1){
            cout<<y<<endl;
        }
        else if(ans > 1){
            cout<<"Bad magician!"<<endl;
        }
        else{
            cout<<"Volunteer cheated!"<<endl;
        }

    }
    return 0;
}

/*
int main ()
{
  freopen ("myfile.txt","w",stdout);
  cout<<"This sentence is redirected heheto a file.";
  fclose (stdout);
  return 0;
}
*/
