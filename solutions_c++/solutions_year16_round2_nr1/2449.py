#include<bits/stdc++.h>
using namespace std;
int i, j, k, l, x, y, z, m, n, p, q, r;
string s;
int t, cs = 1;
int ara[30];
vector < int >  ans;

int main()
{

    freopen("A-large.txt", "r", stdin);
    //freopen("a_large_out.txt", "w", stdout);
    cin >> t;
    while(t--){
        memset(ara, 0, sizeof(ara));
        cin >> s;
        ans.clear();

        for(int i = 0; i < s.size(); i++) ara[int(s[i] - 'A')]++;

        if(ara[25]){
            int x = ara[25];

            for(int i = 0; i < x; i++) {
                ans.push_back(0);
                ara[25]--;//z
                ara[4]--;//e
                ara[17]--;//r
                ara[14]--;//0
            }
        }

        if(ara[22]){
            int x = ara[22];
            for(int i = 0; i < x; i++){
                ans.push_back(2);
                ara[22]--;//w
                ara[19]--;//t
                ara[14]--;//0

            }
        }

        if(ara[6]){
            int x = ara[6];
            for(int i = 0; i < x; i++){
                ans.push_back(8);
                ara[4]--;//e
                ara[8]--;//i
                ara[6]--;//g
                ara[7]--;//h
                ara[19]--;//t

            }
        }
        if(ara[23]){
            int x = ara[23];
            for(int i = 0; i < x; i++){
                ans.push_back(6);
                ara[18]--;//s
                ara[8]--;//i
                ara[23]--;//x
            }
        }

        if(ara[20]){
            int x = ara[20];
            for(int i = 0; i < x; i++){
                ans.push_back(4);
                ara[5]--;//f
                ara[14]--;//o
                ara[20]--;//u
                ara[17]--;//r
            }
        }
        if(ara[19]){
            int x = ara[19];
            for(int i = 0; i < x; i++){
                ans.push_back(3);
                ara[19]--;//t
                ara[7]--;//h
                ara[17]--;//r
                ara[4] -= 2;//e
            }
        }




        if(ara[18]){
            int x = ara[18];
            for(int i = 0; i < x; i++){
                ans.push_back(7);
                ara[18]--;//s
                ara[4] -= 2;//e
                ara[21]--;//v
                ara[13]--;//n
            }
        }

        if(ara[21]){
            int x = ara[21];
            for(int i = 0; i < x; i++){
                ans.push_back(5);
                ara[5]--;//f
                ara[8]--;//i
                ara[21]--;//v
                ara[4]--;//e
            }
        }

        if(ara[14]){
            int x = ara[14];

            for(int i = 0; i < x; i++){
                ans.push_back(1);
                ara[14]--;//o
                ara[13]--;//n
                ara[4]--;//e
            }
        }

        if(ara[8]){
            int x = ara[8];
            for(int i = 0; i < x; i++){
                ans.push_back(9);
                ara[13] -= 2;//n
                ara[8]--;//i
                ara[4]--;//e
            }
        }

        sort(ans.begin(), ans.end());

        printf("Case #%d: ", cs++);

        for(int i = 0; i < ans.size(); i++) cout << ans[i] ;
        cout << endl;

    }


    return 0;
}
