#include <bits/stdc++.h>
using namespace std;

int T;
int g[10][10];
int arr[4][4] = {0};
set<int> s[5];

int h(int n){
    int ret = 0;
    for(int i = 0; i<n; i++)
        for(int j = 0; j<n; j++)
            ret = (ret << 1) | arr[i][j];
    return ret;
}

int hg(int n){
    int ret = 0;
    for(int i = 0; i<n; i++)
        for(int j = 0; j<n; j++)
            ret = (ret << 1) | g[i][j];
    return ret;
}
void rev(int n, int k){
    int r = k;
    for(int i = n-1; i>=0; i--){
        for(int j = n-1; j>=0; j--){
            g[i][j] = r%2;
            r/=2;
        }
    }
    return;
}
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &T);


    //pregen

    int a[10], b[10];

    s[1].insert(1);
    s[2].insert(9);
    s[2].insert(6);
    s[2].insert(15);



    // ===== n = 3 =======
    a[0] = 1; a[1] = 2; a[2] = 3;
    b[0] = 1; b[1] = 2; b[2] = 3;
    do{
        do{
            for(int i = 0; i<3; i++){
                for(int j = 0; j<3; j++){
                    if (a[i]==b[j]) arr[i][j] = 1;
                    else arr[i][j] = 0;
                }
            }
            s[3].insert(h(3));
        }while(next_permutation(b, b+3)); //24
    }while(next_permutation(a, a+3)); //24

    a[0] = 1; a[1] = 2; a[2] = 2;
    b[0] = 1; b[1] = 2; b[2] = 2;
    do{
        do{
            for(int i = 0; i<3; i++){
                for(int j = 0; j<3; j++){
                    if (a[i]==b[j]) arr[i][j] = 1;
                    else arr[i][j] = 0;
                }
            }
            s[3].insert(h(3));
        }while(next_permutation(b, b+3)); //24
    }while(next_permutation(a, a+3)); //24

    a[0] = 2; a[1] = 2; a[2] = 2;
    b[0] = 2; b[1] = 2; b[2] = 2;
    do{
        do{
            for(int i = 0; i<3; i++){
                for(int j = 0; j<3; j++){
                    if (a[i]==b[j]) arr[i][j] = 1;
                    else arr[i][j] = 0;
                }
            }
            s[3].insert(h(3));
        }while(next_permutation(b, b+3)); //24
    }while(next_permutation(a, a+3)); //24

    // N = 4

    a[0] = 1; a[1] = 2; a[2] = 3; a[3] = 4;
    b[0] = 1; b[1] = 2; b[2] = 3; b[3] = 4;
    do{
        do{
            for(int i = 0; i<4; i++){
                for(int j = 0; j<4; j++){
                    if (a[i]==b[j]) arr[i][j] = 1;
                    else arr[i][j] = 0;
                }
            }
            s[4].insert(h(4));
        }while(next_permutation(b, b+4)); //24
    }while(next_permutation(a, a+4)); //24

    //1,1,2
    a[0] = 1; a[1] = 2; a[2] = 3; a[3] = 3;
    b[0] = 1; b[1] = 2; b[2] = 3; b[3] = 3;
    do{
        do{
            for(int i = 0; i<4; i++){
                for(int j = 0; j<4; j++){
                    if (a[i]==b[j]) arr[i][j] = 1;
                    else arr[i][j] = 0;
                }
            }
            s[4].insert(h(4));
        }while(next_permutation(b, b+4)); //24
    }while(next_permutation(a, a+4)); //24


    a[0] = 1; a[1] = 1; a[2] = 3; a[3] = 3;
    b[0] = 1; b[1] = 1; b[2] = 3; b[3] = 3;
    do{
        do{
            for(int i = 0; i<4; i++){
                for(int j = 0; j<4; j++){
                    if (a[i]==b[j]) arr[i][j] = 1;
                    else arr[i][j] = 0;
                }
            }
            s[4].insert(h(4));
        }while(next_permutation(b, b+4)); //24
    }while(next_permutation(a, a+4)); //24

    //
    a[0] = 1; a[1] = 3; a[2] = 3; a[3] = 3;
    b[0] = 1; b[1] = 3; b[2] = 3; b[3] = 3;
    do{
        do{
            for(int i = 0; i<4; i++){
                for(int j = 0; j<4; j++){
                    if (a[i]==b[j]) arr[i][j] = 1;
                    else arr[i][j] = 0;
                }
            }

            s[4].insert(h(4));
        }while(next_permutation(b, b+4)); //24
    }while(next_permutation(a, a+4)); //24

    //
    a[0] = 3; a[1] = 3; a[2] = 3; a[3] = 3;
    b[0] = 3; b[1] = 3; b[2] = 3; b[3] = 3;
    do{
        do{
            for(int i = 0; i<4; i++){
                for(int j = 0; j<4; j++){
                    if (a[i]==b[j]) arr[i][j] = 1;
                    else arr[i][j] = 0;
                }
            }
            s[4].insert(h(4));
        }while(next_permutation(b, b+4)); //24
    }while(next_permutation(a, a+4)); //24



    for (int cas = 1; cas<=T; cas++){
        printf("Case #%d: ", cas);

        int N;
        char ch;
        cin >> N;
        for(int i = 0; i<N; i++){
            for(int j = 0; j<N; j++){
                cin >> ch;
                if (ch == '0') g[i][j] = 0;
                else g[i][j] = 1;
            }
        }

        queue<pair<int,int> > q;

        q.push(make_pair(0, hg(N)));
        int ans = -1;
        bool seen[1000000] = {0};
        while(!q.empty()){

            int d = q.front().first;
            int id = q.front().second;


           // cout << id << endl;
            q.pop();

            if (s[N].count(id) !=0){
                ans = d;
                break;
            }


            rev(N, id);
            if (seen[hg(N)]) continue;
            seen[hg(N)] = true;
            for(int i = 0; i<N; i++){
                for(int j = 0; j<N; j++){
                    if (g[i][j] == 0){
                        g[i][j] = 1;

                        q.push(make_pair(d+1, hg(N)));

                        g[i][j] = 0;
                    }
                }
            }
            /*
            for (int i = 0; i<N; i++){
                for(int j = 0; j<N; j++){
                    cout << g[i][j];
                }
                cout << endl;
            }
            cout << endl;*/

        }

        cout << ans << endl;



    }


}
