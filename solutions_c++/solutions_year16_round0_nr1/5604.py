// codeforces2016.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"


#include <string>
#include <algorithm>
#include <math.h>
#include <vector>
#include <queue>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>
#include <iostream>
#include <set>
#include <cstring>
#include <map>
#include <iomanip>
#include <sstream>
#include <utility>
#include <iterator>
#include <ctype.h>
#include <cmath>

#define pi 3.1415926535
#define ll long long
#define SIZE 100010
#define base 1000000007LL

//#include <bits/stdc++.h>

using namespace std;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    long long t,n, temp_n;
    string line;
    cin >> t;
    for (int i = 1; i <= t; i++){
        cin >> n;
        temp_n = n;
        
        if (n == 0) {cout << "Case #" << i << ": " << "INSOMNIA" << endl; continue;}
        else
        {
            n -= n;
            set<char> s = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
            while (s.size() != 0){
                n += temp_n;
                line = to_string(n);
                for (int i = 0; i < line.length(); i++){
                    if (s.find(line[i]) != s.end()) 
                        s.erase(s.find(line[i]));
                }
            }
            cout << "Case #" << i << ": " << n << endl;
        }

    }

    return 0;
}



//TASK 1april 
//int user_like_obj[11] = { 0};
//int main(){
//    int f,obj,t;
//    cin >> f >> obj >> t;
//    for (int k = 0; k < f; k++){
//        for (int i = 0; i < obj; i++){
//            for (int j = i; j < i+1; j++){
//                char like;
//                cin >> like;
//                if (like == 'Y'){
//                    user_like_obj[j]++;
//                }
//            }
//        }
//    }
//    int ans=0;
//    for (int i = 0; i < 11; i++){
//        if (user_like_obj[i] >= t){
//            ans++;
//        }
//    }
//    cout << ans <<"kitten"<< endl;
//    return 0;
//}


//TASK 656 F
//int main(){
//    string s;
//    cin >> s;
//    int sum=0;
//    for (int i = 0; i < s.length(); i++){
//        if (s[i] == 'A'){
//            sum++;
//        }
//        else if (s[i] == '1'){
//            sum += 10;
//        }
//        else if (s[i] == '0'){
//        }
//        else {
//            sum += int(s[i]-'0');
//        }
//    }
//    cout << sum << endl;
//    return 0;
//}





////TASK Round Edu 1 D
//char c[1001][1001] = {};
//int vis[1001][1001] = {};
//int p[100001] = {};
//int n, m, k, x, y, ans, i, j;
//void visit(int x, int y){
//    if (x == 0 || y == 0 || x == n + 1 || y == m + 1) return;
//    if (c[x][y] == '*') { ans++; return; }
//    if (vis[x][y] != 0) return;
//    vis[x][y] = i;
//    visit(x + 1, y);
//    visit(x, y + 1);
//    visit(x - 1, y);
//    visit(x, y - 1);
//    return;
//}
//
//char ch;
//int main(){
//    cin >> n >> m >> k;
//    for (i = 1; i <= n; i++){
//        for (j = 1; j <= m;){
//            //cin >> ch;
//            ch = getchar();
//            if (ch != '\n'){
//                c[i][j] = ch;
//                j++;
//            }
//        }
//    }
//    for (i = 1; i <= k; i++){
//        cin >> x >> y;
//        ans = 0;
//        if (!vis[x][y]) visit(x, y);
//        else ans = p[vis[x][y]];
//        p[i] = ans;
//        printf("%d\n", ans);
//    }
//    return 0;
//}




//Edu Round 1 Edu B
//int main(){
//    string s;
//    int m,l,r,k;
//    cin >> s >> m;
//    for (int i = 0; i < m; i++){
//        cin >> l >> r >> k;
//        l--;
//        r--;
//        k %= (r-l+1);
//        s = s.substr(0, l) + s.substr(r - k +1,k)+ s.substr(l,r-l+1-k)+ s.substr(r+1);
//    }
//    cout << s << endl;
//    return 0;
//}


//TASK B 346
//vector<pair<int,string>> reg_name[100010];
//vector<pair<pair<int, int>, string>> v;
//set<string> used;
//int main(){
//    int n,m,reg,ball;
//    string name;
//    cin >> n >> m;
//    for (int i = 0; i < n; i++){
//        cin >> name >> reg >> ball;
//        v.push_back(make_pair(make_pair(reg,ball),name));
//    }
//    sort(v.begin(), v.end());
//    reverse(v.begin(), v.end());
//    for (int i = 0; i < n; i++){
//        reg = v[i].first.first;
//        if (reg_name[reg].size() < 3){
//            reg_name[reg].push_back(make_pair(v[i].first.second,v[i].second));
//        }
//    }
//    for (int i = 1,j=0; i <= m; i++){
//        if (reg_name[i].size() == 3 && reg_name[i][j+1].first == reg_name[i][j+2].first){
//            cout << "?" << endl;
//        }
//        else {
//            cout << reg_name[i][j].second << " " << reg_name[i][j + 1].second << endl;
//        }
//    }
//    return 0;
//}




//TASK C 346
//set<int> has_type;
//vector<int> buy_type;
//int main(){
//    int n,m,k,type;
//    cin >> n >> m;
//    for (int i = 0; i <n; i++){
//        cin >> type;
//        has_type.insert(type);
//    }
//    int cur_type = 1;
//    while (m >= cur_type){
//        if (has_type.find(cur_type) == has_type.end()){
//            buy_type.push_back(cur_type);
//            m -= cur_type;
//        }
//        cur_type++;
//    }
//    cout << buy_type.size() << endl;
//    for (auto elem = buy_type.begin(); elem != buy_type.end(); *elem++){
//        cout << *elem << " ";
//    }
//    return 0;
//}


//TASK A 346
//int main()
//
//{
//    int a, b, n;
//    cin >> n >> a >> b;
//    if (b == 0){
//        cout << a << endl;
//        return 0;
//    }
//    else {
//        int temp_b = b;
//        if (b < 0) b = abs(b);
//        while (b != 0){
//            if (a == n && temp_b > 0){
//                a = 1;
//            }
//            else if (a == 1 && temp_b < 0){
//                a = n;
//            }
//            else if (temp_b > 0){
//                a++;
//            }
//            else if (temp_b < 0){
//                a--;
//            }
//            b--;
//        }
//    }
//    cout << a << endl;
//    return 0;
//}





//VK CUP 2016 div2 C didn't solve
//int main(){
//    int n,d,h,from=1,to=2;
//    cin >> n >> d >> h;
//    double temp = d/2.0,d_h= h,d_d=d;
//    if (n == 2 && d == 1 && h == 1){
//        cout << "1 2" << endl;
//        return 0;
//    }
//    if (temp <= d_h && d_h <= d_d ){
//        for (int i = 0; i < n-1;i++){
//            while (h != 0){
//                cout << from <<" "<< to << endl;
//                from++;
//                to++;
//                h--;
//                n--;
//                d--;
//            }
//            from = 1;
//            while (d - h != 0){
//                d--;
//                n--;
//                cout << from << " " << to << endl;
//                from = to;
//                to++;
//            }
//            if (n > 1 && d != h )
//            {
//                cout << 1 << " "<<to << endl;
//                ++to;
//            }
//            else if (n > 1 && d == h){
//                cout << 2 << " " << to << endl;
//                ++to;
//            }
//        }
//    }
//    else {
//        cout << -1 << endl;
//    }
//    return 0;
//}

//VK CUP 2016 div2 B
//int ids[150010] ;
//int main(){
//    vector<int> f_d;
//    
//    int n,k,q,degree,type,id;
//    cin >> n >> k >> q;
//    for (int i = 0; i < n; i++){
//        cin >> degree;
//        f_d.push_back(degree);
//    }
//    vector<pair<int,int>> online;
//    vector<string > ans;
//    for (int i = 0; i < q; i++){
//        cin >> type >> id;
//        if (type == 1){
//            sort(online.begin(), online.end());
//            if (online.size() ==0 || online.size() < k)
//            {    
//                online.push_back(make_pair(f_d[id-1],id));
//                ids[id] = 1;
//            }
//            else if (f_d[id-1] > online[0].first)
//            {
//                int temp = online[0].second;
//                online[0].second = id;
//                online[0].first = f_d[id-1];
//                ids[id] = 1;
//                ids[temp] = 0;
//            }
//        }
//        else if (type == 2){
//            if (ids[id]){
//                ans.push_back("YES");
//            }
//            else{
//                ans.push_back("NO");
//            }
//        }
//    }
//    for (int i = 0; i < ans.size(); i++){
//        cout << ans[i] << endl;
//    }
//    return 0;
//}


//VK CUP 2016 div2 A
//int main(){
//    vector<int> p,t;
//    int n, c,points,time,lim=0,rad=0;
//    cin >> n >> c;
//    for (int i = 0; i < n; i++){
//        cin >> points;
//        p.push_back(points);
//    }
//    for (int i = 0; i < n; i++){
//        cin >> time;
//        t.push_back(time);
//    }
//    time = 0;
//    for (int i = 0; i < n; i++){
//        time += t[i];
//        lim += max(0, p[i] - c*time);
//    }
//    time = 0;
//    for (int i = n-1; i >= 0; i--){
//        time += t[i];
//        rad += max(0, p[i] - c*time);
//    }
//    if (lim > rad){
//        cout << "Limak" << endl;
//    }
//    else if (lim < rad){
//        cout << "Radewoosh" << endl;
//    }
//    else if (lim == rad){
//        cout << "Tie" << endl;
//    }
//    return 0;
//}

//int main(){
//    unsigned int v; // count the number of bits set in v
//    unsigned int c; // c accumulates the total bits set in v
//    cin >> v;
//    //// option 1, for at most 14-bit values in v:
//    //c = (v * 0x200040008001ULL & 0x111111111111111ULL) % 0xf;
//
//    //// option 2, for at most 24-bit values in v:
//    //c = ((v & 0xfff) * 0x1001001001001ULL & 0x84210842108421ULL) % 0x1f;
//    //c += (((v & 0xfff000) >> 12) * 0x1001001001001ULL & 0x84210842108421ULL)
//    //    % 0x1f;
//
//    // option 3, for at most 32-bit values in v:
//    c = ((v & 0xfff) * 0x1001001001001ULL & 0x84210842108421ULL) % 0x1f;
//    c += (((v & 0xfff000) >> 12) * 0x1001001001001ULL & 0x84210842108421ULL) %
//        0x1f;
//    c += ((v >> 24) * 0x1001001001001ULL & 0x84210842108421ULL) % 0x1f;
//    cout << c << endl;
//    return 0;
//}

//int main(){ 
//    int v,c;
//    cin >> v;
//    for (c = 0; v; c++){
//        v &= v -1;
//    }
//    cout << c << endl;
//    return 0;
//}

// TASK K -didn't solve
//int main(){
//    int n , l,r,sum=0;
//    cin >> n ;
//    vector<vector<int>> v(n);
//    for (int i = 0; i < n; i++){
//        cin >> l >> r;
//        for (int j = l; j <= r; j++){
//            v[i].push_back(j);
//        }
//    }
//    int max_x,min_x,max_index,min_index;
//    for (int i = 0; i < n; i++){
//        for (int j = i+1; j < n; j++){
//            if (v[i].size() > v[j].size()){
//                max_x = v[i].size();
//                max_index= i;
//                min_index = j;
//                min_x = v[j].size();
//            }
//            else {
//                max_x = v[j].size();
//                min_x = v[i].size();
//                min_index = i;
//                max_index = j;
//            }
//            for (int k = 0; k < max_x; k++){
//                for (int z = 0; z < min_x; z++){
//                    int templ = v[max_index][k] ^ v[min_index][z];
//                    while (templ != 0){
//                        if (templ & 1){
//                            sum++;
//                        }
//                        templ >>=1;
//                    }
//                }
//            }
//        }
//    }
//    
//    cout << sum << endl;
//    return 0;
//}



   /* int n,k,a,sum=0;
    vector<int> v;
    cin >> n >> k;
    for (int i = 0; i < n; i++){
        cin >> a;
        sum += a;
        v.push_back(a);
    }
    for (int i = 0; i < n; i++){
        v.push_back(v[i]);
    }
    for (int i = 0; i < n; i++){
        for (int i = 0; i < k; i += k){

        }
    }
    return 0;
}*/


//bsuir qual 2016 TASK D
//int main(){
//
//    int n, m, color = 0;
//    cin >> n >> m;
//    char sym1 , sym2;
//    int div_four, non_four;
//   
//    if (n % 4 == 0 || m % 4 == 0){
//        int temp_col=0;
//        /*if (n % 4 == 0) {
//            div_four = n;
//            non_four = m;
//            }
//        else {
//            div_four = m;
//            non_four = n;
//            }*/
//        if (m % 4 == 0){
//            for (int i = 0; i < n; i++){
//                /*if (i % 4 == 0 && i != 0){*/
//                    color += temp_col + 1;
//                //}
//                    for (int j = 0,z=0; j < m; j+=4,z+=1){
//                        sym1 = 'a' + color + z;
//                        sym2 = 'a' + color + z;
//                        cout << sym1 << sym2 << sym1 << sym2;
//                        temp_col =z;
//                    }
//                    cout << endl;
//             }
//         } else {
//            string s;
//            for (int i = 0; i < n; i++){
//                //i += 4;
//                /*if (i % 4 == 0 && i != 0){*/
//                if (i % 4 == 0)
//                color += temp_col + 1;
//                s.clear();
//                for (int j = 0, z = 0; j < m; j++, z++){
//                    sym1 = 'a' + color + z;
//                    //sym2 = 'a' + color + z;
//                    s += sym1;
//                    temp_col = z;
//                }
//                cout << s;
//                        
//                //if (n /4 > 1) cout << endl;
//                    
//                cout << endl;
//                //i += 4;
//            }
//        }
//    } else {
//        if (n % 2 == 0 && m % 2 == 0){
//
//            int temp_col = 0;
//            if (n % 2 == 0) {
//                div_four = n;
//                non_four = m;
//            }
//            else {
//                div_four = m;
//                non_four = n;
//            }
//            for (int i = 0; i< div_four; i++){
//                if (i % 2 == 0 && i != 0){
//                    color += temp_col + 1;
//                }
//                for (int j = 0, z = 0; j < non_four; j += 2, z++){
//                    sym1 = 'a' + color + z;
//                    sym2 = 'a' + color + z;
//                    cout << sym1 << sym2;
//                    //cout << ((char)('a' + color + j) <<  (char)('a' + color + j));
//                    temp_col = z;
//                }
//                cout << endl;
//            }
//        }
//    }
//    
//    return 0;
//}

// TASK 1
//vector<vector<int>> g(SIZE);//, leaves(SIZE);
//vector<int>arr_a(SIZE),arr_b(SIZE),arr_c(SIZE);
////vector<vector<int>> ch(SIZE);
////bool used[SIZE] = { false };
////int has_leave = 0;
////vector<int> vertexes;
////set<int> set_leaves;
////void dfs(int v) {
////	used[v] = true;
////    vertexes.push_back(v);
////    int is_not_leave = 0;
////    for (vector<int>::iterator i = g[v].begin(); i != g[v].end(); ++i){
////        if (!used[*i]){
////            is_not_leave++;
////            /*ch[v].push_back(*i);*/
////            for (int j = 1; j <= vertexes.size(); j++) {// for set children without leaves
////                if (set_leaves.find(vertexes[j-1])==set_leaves.end())
////                ch[vertexes[j-1]].push_back(*i);  // --//--
////            }
////		    dfs(*i);
////        }
////        has_leave = *i;
////    }
////    if (!is_not_leave)
////        leaves[has_leave].push_back(v);
////    set_leaves.insert(v);
////}
//void dfs_dp(int x, int p){
//    for (int i = 0; i < g[x].size(); i++){
//        if (p == g[x][i]) continue;
//        dfs_dp(g[x][i],x);
//        arr_a[x] = max(arr_a[x], arr_b[g[x][i]] + 1 - arr_c[g[x][i]]);
//        arr_b[x] += arr_c[g[x][i]];
//    }
//    arr_a[x] += arr_b[x];
//    arr_c[x] = max(arr_a[x], arr_b[x]);
//}
//
//int main(){
//    int n,a,b;
//    cin >> n;
//    for (int i = 1; i < n; i++){
//        cin >> a >> b;
//        g[a].push_back(b);
//        g[b].push_back(a);
//    }
//    //dfs(1);
//    /*for (int i = 1; i < leaves.size(); i++){
//        for (int j = 0; j < leaves[i].size(); j++){
//            arr_a[leaves[i][j]] = 0;
//            arr_b[leaves[i][j]] = 0;
//        }
//    }*/
//    dfs_dp(1,1);
//    cout << arr_c[1] << endl;
//    //int sum = 0;
//    //for (int i = 0; i < leaves.size(); i++)
//    //    for (int j = 0; j<leaves[i].size(); j++)
//    //        cout << i << " has leaf " << leaves[i][j] << endl;
//    //for (int i = 0; i < ch.size(); i++)
//    //    for (int j = 0; j<ch[i].size(); j++){ 
//    //        cout << i << " has children " << ch[i][j] << endl;
//    //        //sum += ch[i][j];
//    //    }
//    ////cout << sum << endl;
//    return 0;
//}


//int main(){
//    int n,m,l,r,v;
//    set<int> s,s_temp;
//    vector<pair<pair<int, int>, int>> vec;
//    vector<int> q;
//    cin >> n >> m;
//    for (int i = 0; i < m; i++){
//        cin >> l >> r >> v;
//        vec.push_back(make_pair(make_pair(l,r),v));
//        s.insert(v);
//        s_temp.insert(v);
//    }
//    sort(vec.begin(), vec.end());
//    for (int i = 0; i<vec.size(); i++){
//        if (s.find(vec[i].second) != s.end())
//        {
//             q.push_back(vec[i].second);
//             s.erase(vec[i].second);
//        }
//    }
//    for (int i = 1,j=0; i <= n; i++){
//        if (s_temp.find(i) != s_temp.end()){
//            cout << i << " " << endl;
//        }
//        else {
//            cout << q[j] << " "<< endl;
//            j++;
//        }
//    }
//    return 0;
//}


//TASK 9
//stack<int> in, cur;
//int main(){
//    ll n,ans=0;
//    cin >> n;
//    for (int i = 0; i < n; i++){
//        int a;
//        cin >> a;
//        in.push(a);
//    }
//    int c;
//    while (in.size() != 1){
//        int a = in.top();
//        in.pop();
//        int b = in.top();
//        in.pop();
//        if (a > b){ 
//            cur.push(a);
//            in.push(b);
//        }
//        else if (a < b){
//            if (cur.size() != 0){
//                c = cur.top();
//            }
//            while (cur.size() != 0 && abs(c - a) < abs(b - a)){
//                cur.pop();
//                ans += abs(c-a);
//                a = c;
//                if (cur.size() != 0)
//                    c = cur.top();
//            }
//            ans += abs(a-b);
//            in.push(b);
//        }
//        else if (a == b){
//            in.push(a);
//        }
//    }
//    int a = in.top();
//    in.pop();
//    while (cur.size() != 0){
//        int b = cur.top();
//        cur.pop();
//        ans += abs(b - a); 
//        cur.push(b);
//        if (cur.size() >= 1){
//            a = cur.top();
//            cur.pop();
//        }
//        else{
//            break;
//        }
//    }
//    cout << ans << endl;
//    return 0;
//}


// TAKS 11
//4 3
//-1 -2 3 4
//ans: -1 -2 3
//ll a[100010];
//int main(){
//    ll n,k,i,j,neg=0;
//    ll mul = 1;
//    cin >> n >> k;
//    j = n-1;
//    for (i = 0; i < n; i++){
//        cin >> a[i];
//        if (a[i] < 0){
//            neg++;
//        }
//    }
//    sort(a,a+n);
//    if (neg == n && k % 2 != 0){
//        for (int i = n - 1; i >= n - k; i--){
//            mul *= (a[i]%base);
//            mul = mul % base;
//        }
//        mul %= base;
//        if (mul < 0)
//            mul += base;
//        cout << mul << endl;
//        return 0;
//    }
//    if (k % 2 != 0){
//        k--;
//        j--;
//    }
//    for ( i = 0; k > 0;){
//        if (a[i] * a[i + 1] > a[j] * a[j - 1]){
//            i+=2;
//            k-=2;
//        }
//        else {
//            j-=2;
//            k-=2;
//        }
//    }
//    
//    for (int ix = 0; ix < i; ix++){
//        mul *= (a[ix]%base);
//        mul = mul % base;
//    }
//    for (int ix = n - 1; ix > j; ix--){
//        mul *= (a[ix]%base);
//        mul = mul % base;
//    }
//    mul %= base;
//    if (mul < 0)
//        mul += base;
//    cout << mul << endl;
//    return 0;
//}





//bool comp(ll a, ll b){
//    return abs(a) < abs(b);
//}
//
//ll a[100010] = { 0 }, res[100010] = { 0 }, posres[100010],negres[100010],
//    posrem[100010],negrem[100010];
//int main(){
//    ll n,k,nnegnum=0,lenposres=0,lennegres=0,lenposrem=0,lennegrem=0,nnega=0,nposa=0,nnull=0;
//    //scanf("%ll %ll",&n,&k);
//    cin >> n >> k;
//    for (int i = 0; i < n; i++){
//        //scanf("%ll",&a[i]);
//        cin >> a[i];
//        if (a[i] < 0)
//            nnega++;
//        else if (a[i] > 0)
//            nposa++;
//        else if (a[i] == 0)
//            nnull++;
//    }
//    if (n - nnull < k)
//    {
//        printf("%d",0);
//        return 0;
//    } 
//    sort(a, a+n,comp);
//    for (int i = n-1,j=0; i >= n-k; i--,j++){
//        if (a[i] < 0){
//            nnegnum++;
//            negres[lennegres++] = a[i];
//        }
//        else {
//            posres[lenposres++] = a[i];
//        }
//        res[j] = a[i];
//    }
//    
//    for (int i = 0; i < n-k; i++){
//        if (a[i] < 0){
//            negrem[lennegrem++] = a[i];
//        }
//        else if (a[i] >= 0){
//            posrem[lenposrem++] = a[i];
//        }
//    }
//    sort(a, a + n);
//    //sort(a, a+n-k);
//    sort(res, res+k);
//    sort(posres, posres + lenposres);
//    sort(negres, negres + lennegres);
//    int loc_minposres = -1, loc_minnegres= -1, loc_minnegrem=-1,loc_maxposrem=-1;
//    ll minposres = *min_element(posres, posres + lenposres);
//    if (lenposres)
//        loc_minposres = distance(res, find(res,res+k,minposres));
//    
//    ll minnegres = *min_element(negres,negres+k);
//    if (lennegres)
//        loc_minnegres = distance(res,find(res,res+k,minnegres));
//    
//    ll minnegrem = *min_element(negrem,negrem+lennegrem);//1
//    if (lennegrem)
//        loc_minnegrem = distance(negrem,find(negrem,negrem+lennegrem,minnegrem));
//
//    ll maxposrem = *max_element(posrem,posrem + lenposrem);//2
//    if (lenposrem)
//        loc_maxposrem = distance(posrem, find(posrem,posrem+lenposrem,maxposrem));
//    ll d1=-1,d2=-1;
//    if (k < n){
//        if (nnegnum % 2 != 0){
//            if (loc_minnegrem != -1 && loc_minposres != -1 &&
//             (minnegrem != 0 || minposres != 0))
//                d1 = abs(abs(minnegrem) - abs(minposres));//1
//            if (loc_minnegres != -1 && loc_maxposrem != -1 &&
//             (minnegres != 0 || maxposrem != 0))
//                d2 = abs(abs(minnegres) - abs(maxposrem));//2
//            int maxd = max(d1,d2);
//            if (maxd == d1){ //1
//                swap(res[loc_minposres],negrem[loc_minnegrem]); 
//                nnegnum++;
//            }
//            else if(maxd == d2){
//                swap(res[loc_minnegres],posrem[loc_maxposrem]);
//                nnegnum--;
//            }
//        }
//    }
//    sort(res,res+k);
//    for (int i = 0; i < nnegnum; i++){
//    
//            res[i] = a[i];
//    }
//    for (int i = nnegnum,j=n-1; i <=k-nnegnum+1 ; i++,j--){
//        
//            res[i] = a[j];
//    }
//    ll mul = 1;
//    for (int i = 0; i < k; i++){
//        //cout << res[i] << " ";
//        mul *= (res[i] % base);
//        //mul *= res[i];
//    }
//    printf("%d\n",mul);
//    //cout << endl << "nnegnum = "<<nnegnum << endl;
//    //cout << "mul = " << mul << endl;
//    return 0;
//}




//TASK 15
//int start[100010] = { 0 }, arrend[100010] = { 0 };
//int cur = 0;
//int st, en, q;
//int main(){
//    string s;
//    cin >> s;
//    scanf_s("%d",&q);
//    for (int i = 0; i < q; i++){
//        scanf_s("%d %d",&st,&en);
//        st--;
//        en--;
//        if (st > en)
//            swap(st, en);
//        start[st]++;
//        arrend[en]++;
//    }
//    cur = cur + start[0];
//    if (cur % 2 == 0){
//        printf("%c", s[0]);
//    }
//    else {
//        if (islower(s[0]))
//            printf("%c", toupper(s[0]));
//        else if (isupper(s[0]))
//            printf("%c", tolower(s[0]));
//    }
//    for (int i = 1; i < s.length(); i++){
//        cur = cur + start[i] - arrend[i - 1];
//        if (cur % 2 == 0){
//            printf("%c", s[i]);
//        }
//        else {
//            if (islower(s[i]))
//                printf("%c", toupper(s[i]));
//            else 
//                printf("%c", tolower(s[i]));
//        }
//    }
//    printf("\n");
//    return 0;
//}





//TASK 4
//int  _mergeSort(int arr[], int temp[], int left, int right);
//int merge(int arr[], int temp[], int left, int mid, int right);
//
///* This function sorts the input array and returns the
//number of inversions in the array */
//int mergeSort(int arr[], int array_size)
//{
//    int *temp = (int *)malloc(sizeof(int)*array_size);
//    return _mergeSort(arr, temp, 0, array_size - 1);
//}
//
///* An auxiliary recursive function that sorts the input array and
//returns the number of inversions in the array. */
//int _mergeSort(int arr[], int temp[], int left, int right)
//{
//    long long mid, inv_count = 0;
//    if (right > left)
//    {
//        /* Divide the array into two parts and call _mergeSortAndCountInv()
//        for each of the parts */
//        mid = (right + left) / 2;
//
//        /* Inversion count will be sum of inversions in left-part, right-part
//        and number of inversions in merging */
//        inv_count = _mergeSort(arr, temp, left, mid);
//        inv_count += _mergeSort(arr, temp, mid + 1, right);
//
//        /*Merge the two parts*/
//        inv_count += merge(arr, temp, left, mid + 1, right);
//    }
//    return inv_count;
//}
//
///* This funt merges two sorted arrays and returns inversion count in
//the arrays.*/
//int merge(int arr[], int temp[], int left, int mid, int right)
//{
//    int i, j, k;
//    long long inv_count = 0;
//
//    i = left; /* i is index for left subarray*/
//    j = mid;  /* i is index for right subarray*/
//    k = left; /* i is index for resultant merged subarray*/
//    while ((i <= mid - 1) && (j <= right))
//    {
//        if (arr[i] <= arr[j])
//        {
//            temp[k++] = arr[i++];
//        }
//        else
//        {
//            temp[k++] = arr[j++];
//
//            /*this is tricky -- see above explanation/diagram for merge()*/
//            inv_count = inv_count + (mid - i);
//        }
//    }
//
//    /* Copy the remaining elements of left subarray
//    (if there are any) to temp*/
//    while (i <= mid - 1)
//        temp[k++] = arr[i++];
//
//    /* Copy the remaining elements of right subarray
//    (if there are any) to temp*/
//    while (j <= right)
//        temp[k++] = arr[j++];
//
//    /*Copy back the merged elements to original array*/
//    for (i = left; i <= right; i++)
//        arr[i] = temp[i];
//
//    return inv_count;
//}
//
///* Driver progra to test above functions */
//int arr[1000010];
//int main(int argv, char** args)
//{
//    int n;
//    cin >> n;
//    for (int i = 0; i < n; i++){
//        cin >> arr[i];
//    }
//    cout << mergeSort(arr, n) << endl;
//    return 0;
//}






//TASK 16
//int binpow_nonrec(int a, int n){
//    int res = 1;
//    while (n){
//        if (n & 1)
//            res *= a;
//        a *= a;
//        n>>=1;
//    }
//    return res;
//}
//
//
//
//
//
//vector<vector<ll>> matxmat(vector<vector<ll>>, vector<vector<ll>>, ll);
//
//vector<vector<ll>> binpow(vector<vector<ll>> e,vector<vector<ll>> a, ll n, ll size){
//    if (n == 0){
//        return e;
//    }
//    if (n % 2 == 1){
//        return matxmat(binpow(e, a, n - 1, size),a, size);
//    }
//    else {
//        vector<vector<ll>> b = binpow(e, a, n / 2, size);
//        return matxmat(b, b, size);
//    }
//}
//
//vector<vector<ll>> matxmat(vector<vector<ll>> a, vector<vector<ll>>b, ll size){
//    vector<vector<ll>> out(size);
//    for (int i = 0; i < size; i++){
//        out[i].resize(size);
//    }
//    for (int i = 0; i < size; i++){
//        for (int j = 0; j < size; j++){
//            for (int k = 0; k < size; k++){
//                out[i][j] = (out[i][j] + a[i][k] * b[k][j]) % base;
//            }
//        }
//    }
//    return out;
//}
//
//int main(){
//    ll n,m,u,v,i,j,len;
//    cin >> n >> m >> u >> v >> len;
//    u--;
//    v--;
//    vector<vector<ll>> g(n),e(n),out(n);
//
//    for (int i = 0; i < n; i++){
//        g[i].resize(n);
//        e[i].resize(n);
//        out[i].resize(n);
//    }
//        
//    for (int i = 0; i < n; i++){
//        for (int j = 0; j < n; j++){
//            if (i == j){
//                e[i][j]=1;
//            }
//        }
//    }
//    for (int ix = 0; ix < m; ix++){
//        cin >> i >> j;
//        i--;
//        j--;
//        g[i][j]++;
//        g[j][i]++;
//    }
//    out = binpow(e, g, len, n);
//    /*for (int i = 0; i < n; i++){
//        for (int j = 0; j < n; j++){
//            cout << out[i][j] << " ";
//        }
//        cout << endl;
//    }*/
//    cout << out[u][v] << endl;
//    return 0;
//}





//int binpow(int a, int n){
//    int res = 1;
//    while (n){
//        if (n & 1)
//            res *= a;
//        a *= a;
//        n>>=1;
//    }
//    return res;
//}
//
//long long g[110][110] = {0},ans[110][110]={0};
//int main(){
//    long long n,m,u,v,i,j;
//    long long len;
//    //cin >> n >>m >> u >> v >> len;
//    cin >> n;
//    for (int i = 0; i < n; i++){
//        for (int j = 0; j < n; j++){
//            cin >>  g[i][j]; 
//        }
//    }
//    /*for (int ix = 0; ix < m; ix++){
//        cin >> i >> j;
//        g[i][j]++;
//        g[j][i]++;
//    }*/
//    int mul = 1,sum=0;
//    for (int i = 0; i < n; i++){
//        for (int j = 0; j < n; j++){
//            mul = 1;
//            sum = 0;
//            for (int k = 0; k < n; k++){
//                mul = g[i][k] * g[k][j];
//                sum += mul;
//            }
//            ans[i][j] = sum;
//        }
//    }
//    for (int i = 0; i < n; i++){
//        for (int j = 0; j < n; j++){
//            cout << ans[i][j] << " ";
//        }
//        cout << endl;
//    }
//}







//vector<int> color(100010);
//vector<int> time_in(100010), time_out(100010);
//long long dfs_timer = 0,sum=0,down_vert=0;
//vector< vector < pair<int,int> > >g(100010);
//vector<vector<pair<int,int>> > g_parent_i(100010);
//void dfs(int v){
//    time_in[v] = dfs_timer++;
//    color[v] = 1;
//    for (vector<pair<int,int>>::iterator i = g[v].begin(); i != g[v].end(); ++i)
//    {
//    if (color[(*i).first] == 0)
//        {
//            g_parent_i[(*i).first].push_back(make_pair(v,(*i).second));
//            dfs((*i).first);
//        }
//    }
//    color[v] = 2;
//    time_out[v] = dfs_timer++;
//}
//int main(){
//    long long n,a,b,w;
//    cin >> n;
//    for (int i = 0; i < n-1; i++){
//        cin >> a >> b >> w;
//        g[a].push_back(make_pair(b,w));
//        g[b].push_back(make_pair(a,w));
//    }
//    dfs(1);
//    for (int i = 2; i <= n; i++){
//        down_vert = ((time_out[i] - time_in[i])/2) + 1;
//        sum += down_vert*(n - down_vert)*g_parent_i[i][0].second;
//    }
//    cout << ((sum * 2) % (10000000 +7))<< endl;
//    return 0;
//}





//int a[100010]={0};
//int main(){
//    string s;
//    pair<int,int> lr;
//    set<int> setx;
//    cin >> s;
//    int q;
//    cin >> q;
//    for (int i = 0; i < q; i++){
//        int l,r;
//        cin >> l >> r;
//        if (l > r){
//            swap(l,r);
//        }
//        for (int i = l - 1; i < r; i++){
//            a[i]++;
//            setx.insert(i);
//        }
//    }
//    for (set<int>::iterator it =setx.begin(); it != setx.end(); it++){
//        if (a[*it] % 2 != 0){
//            s[*it] = toupper(s[*it]);
//        }
//    }
//    cout << s << endl;
//    return 0;
//}


//string temp = "xxxxxx";
//vector<char> v(6), vcopy(6);
//vector<string> vpermitions;
//string number = "xxxxxx";
//void recursion(int nlen, int n, int i=0){
//    for (;i <= 5 && n > nlen; i++){
//        number[nlen] = v[i];
//        recursion(++nlen, n);
//        if (n == nlen){
//            for (int j = 0; j<n; j++)
//                temp[j] = number[j];
//            temp.erase(temp.begin()+n, temp.end());
//            cout << temp << endl;
//            vpermitions.push_back(temp);
//        }
//    }
//    if (n == nlen){
//        number[nlen - 1] = v[i];
//        return ;
//        }
//    else 
//        recursion(nlen,n);
//
//}
//
//int main(){
//    int n,q;
//    string twos,ones;
//    //string temp="xxxxxx";
//    vector<pair<string,string>> pats;
//    cin >> n>> q;
//    for (int i = 0; i < q; i++){
//        cin >> twos >> ones;
//        pats.push_back(make_pair(twos,ones));
//    }
//    /*vector<char> v(6), vcopy(6);
//    vector<string> vpermitions;
//    string number = "xxxxxx";*/
//    v[0] = 'a';
//    v[1] = 'b';
//    v[2] = 'c';
//    v[3] = 'd';
//    v[4] = 'e';
//    v[5] = 'f';
//    vcopy = v;
//    recursion(0,n);
//    //for (int a = 0; a <= 5 && n >0; a++){
//    //    // vcopy = v;
//    //    if (find(vcopy.begin(), vcopy.end(), v[a]) != vcopy.end()){
//    //        number[0] = v[a];
//    //        //vcopy.erase(find(vcopy.begin(), vcopy.end(), v[a]));
//    //    }
//    //    else {
//    //        continue;
//    //    }
//    //    for (int b = 0; b <= 5 && n >1; b++){
//    //        // vcopy = v;
//    //        //vcopy.erase(find(vcopy.begin(), vcopy.end(), v[a]));
//    //        if (find(vcopy.begin(), vcopy.end(), v[b]) != vcopy.end()){
//    //            number[1] = v[b];
//    //            //vcopy.erase(find(vcopy.begin(), vcopy.end(), v[b]));
//    //        }
//    //        else {
//    //            continue;
//    //        }
//    //        for (int c = 0; c <= 5 && n >2; c++){
//    //            // vcopy = v;
//    //            //vcopy.erase(find(vcopy.begin(), vcopy.end(), v[a]));
//    //            //vcopy.erase(find(vcopy.begin(), vcopy.end(), v[b]));
//    //            if (find(vcopy.begin(), vcopy.end(), v[c]) != vcopy.end()){
//    //                number[2] = v[c];
//    //                //vcopy.erase(find(vcopy.begin(), vcopy.end(), v[c]));
//
//    //            }
//    //            else {
//    //                continue;
//    //            }
//    //            for (int d = 0; d <= 5 && n >3; d++){
//    //                // vcopy = v;
//    //                //vcopy.erase(find(vcopy.begin(), vcopy.end(), v[a]));
//    //                //vcopy.erase(find(vcopy.begin(), vcopy.end(), v[b]));
//    //                //vcopy.erase(find(vcopy.begin(), vcopy.end(), v[c]));
//    //                if (find(vcopy.begin(), vcopy.end(), v[d]) != vcopy.end()){
//    //                    number[3] = v[d];
//    //                    //vcopy.erase(find(vcopy.begin(), vcopy.end(), v[d]));
//    //                }
//    //                else {
//    //                    continue;
//    //                }
//    //                for (int e = 0; e <= 5 && n >4; e++){
//    //                    // vcopy = v;
//    //                    /* vcopy.erase(find(vcopy.begin(), vcopy.end(), v[a]));
//    //                    vcopy.erase(find(vcopy.begin(), vcopy.end(), v[b]));
//    //                    vcopy.erase(find(vcopy.begin(), vcopy.end(), v[c]));
//    //                    vcopy.erase(find(vcopy.begin(), vcopy.end(), v[d]));*/
//    //                    if (find(vcopy.begin(), vcopy.end(), v[e]) != vcopy.end()){
//    //                        number[4] = v[e];
//    //                        //vcopy.erase(find(vcopy.begin(), vcopy.end(), v[e]));
//    //                    }
//    //                    else {
//    //                        continue;
//    //                    }
//    //                    for (int f = 0; f <= 5 && n >5; f++){
//    //                        // vcopy = v;
//    //                        /* vcopy.erase(find(vcopy.begin(), vcopy.end(), v[a]));
//    //                        vcopy.erase(find(vcopy.begin(), vcopy.end(), v[b]));
//    //                        vcopy.erase(find(vcopy.begin(), vcopy.end(), v[c]));
//    //                        vcopy.erase(find(vcopy.begin(), vcopy.end(), v[d]));
//    //                        vcopy.erase(find(vcopy.begin(), vcopy.end(), v[e]));*/
//    //                        if (find(vcopy.begin(), vcopy.end(), v[f]) != vcopy.end()){
//    //                            number[5] = v[f];
//    //                            //vcopy.erase(find(vcopy.begin(), vcopy.end(), v[f]));
//    //                        }
//    //                        else {
//    //                            continue;
//    //                        }
//    //                        if (n >= 6){
//    //                            for (int i = 0; i<n; i++)
//    //                                temp[i] = number[i];
//    //                            temp.erase(temp.begin() + n, temp.end());
//
//    //                            //cout << temp << endl;
//    //                            vpermitions.push_back(temp);
//    //                        }
//    //                    }
//    //                    if (n == 5){
//    //                        for (int i = 0; i<n; i++)
//    //                            temp[i] = number[i];
//    //                        temp.erase(temp.begin() + n, temp.end());
//
//    //                        //cout << temp << endl;
//    //                        vpermitions.push_back(temp);
//    //                    }
//    //                }
//    //                if (n == 4){
//    //                    for (int i = 0; i<n; i++)
//    //                        temp[i] = number[i];
//    //                    temp.erase(temp.begin() + n, temp.end());
//    //                    //cout << temp << endl; 
//    //                    vpermitions.push_back(temp);
//    //                }
//    //            }
//    //            if (n == 3){
//    //                for (int i = 0; i<n; i++)
//    //                    temp[i] = number[i];
//    //                temp.erase(temp.begin() + n, temp.end());
//    //                //cout << temp << endl;
//    //                vpermitions.push_back(temp);
//    //            }
//    //        }
//    //        if (n == 2){
//    //            for (int i = 0; i<n; i++)
//    //                temp[i] = number[i];
//    //            temp.erase(temp.begin() + n, temp.end());
//    //            //cout << temp << endl;
//    //            vpermitions.push_back(temp);
//    //        }
//    //    }
//    //    if (n == 1){
//    //        for (int i = 0; i<n; i++)
//    //            temp[i] = number[i];
//    //        temp.erase(temp.begin() + n, temp.end());
//    //        //cout << temp << endl;
//    //        vpermitions.push_back(temp);
//    //    }
//    //}
//    int ok = 1;
//    int answer =0;
//    int per_on = 0;
//    for (int i = 0; i < vpermitions.size(); i++){
//        while (ok == 1){
//            for (int j = 0; j < pats.size(); j++){
//                size_t index = vpermitions[i].find(pats[j].first);
//                if (index == 0){
//                    vpermitions[i].erase(0,2);
//                    vpermitions[i].insert(0, pats[j].second);
//                    per_on = 1;
//                }
//                else {
//                    continue;
//                }
//            }
//            if (per_on){
//                per_on = 0;
//            }
//            else {
//                ok = 0;
//            }
//        }
//        if (vpermitions[i].length() == 1 && vpermitions[i] == "a"){
//            answer++;
//        }
//        ok = 1;
//    }
//    cout << answer << endl;
//    return 0;
//}
    


//int main(){
//    int n;
//    set<int> s;
//    vector<int> v;
//    cin >> n;
//    for (int i = 0; i < n; i++){
//        int tmp;
//        cin >> tmp;
//        s.insert(tmp);
//        v.push_back(tmp);
//    }
//    int a[3], b[3];
//    if (s.size() >= 3){
//        for (int i = 0; i < n; i++){
//            a[0] = v[i];
//            for (int i = 0; i < n; i++){
//                if (v[i] != a[0]){
//                    a[1] = v[i];
//                }
//                else {
//                    continue;
//                }
//                for (int i = 0; i < n; i++){
//                    if (v[i] != a[0] && v[i] != a[1]){
//                        a[2] = v[i];
//                    }
//                    else {
//                        continue;
//                    }
//                    
//                    copy(a,a+3,b);
//                    sort(b, b + 3);
//                    if (abs(b[0] - b[1]) == 1 && abs(b[1] - b[2]) == 1){
//                        cout << "YES" << endl;
//                        return 0;
//                    }
//                }
//                
//            }
//        }
//    }
//    cout << "NO" << endl;
//    return 0;
//}





//const long long INF = 100000000000;
//vector<char> used (1000000);
//vector< vector <int>> gtemp(1000000);
//int ncomp = 0;
//vector <vector <pair<int,int> > > g(100010);
//bool used[10010];
//vector<int> comp;
//void dfs(int v){
//    used[v] = true;
//    comp.push_back(v);
//    for (size_t i = 0; i < g[v].size(); ++i){
//        int to = g[v][i].first;
//        if (!used[to])
//            dfs(to);
//    }
//}
//
//
//void find_comps(int n){
//    for (int i = 1; i<=n; ++i)
//        used[i] = false;
//    for (int i = 1; i<=n; ++i)
//    if (!used[i]){
//        comp.clear();
//        dfs(i);
//        if (comp.size() > 0)
//            ncomp++;
//    }
//}
//int main(){
//    int n, m,ok,w=1;
//    cin >> n >> m;
//
//    for (int i = 0; i < m; i++)
//    {
//        int a, b;
//        cin >> a >> b;
//        ok = 0;
//        if (g[a].size() > 0)
//        {
//            for (int j = 0; j<g[a].size(); j++)
//            if (g[a][j].first == b)
//            {
//                ok = 1;
//            }
//            
//            if (ok == 0)
//                g[a].push_back(make_pair(b,w));
//            }
//        else {
//            g[a].push_back(make_pair(b, w));
//        }
//        ok = 0;
//        if (g[b].size() > 0){
//            for (int j = 0; j<g[b].size(); j++)
//            if (g[b][j].first == a)
//            {
//                ok = 1;
//            }
//            if (ok == 0)
//                g[b].push_back(make_pair(a,w));
//        }
//        else {
//            g[b].push_back(make_pair(a, w));
//        }
//    }
//    find_comps(n);
//    if (ncomp == 1){
//        if (m == 1 && n==1)
//            cout << 0 << endl;
//        else if (m - n + 1 >= 0)
//            cout << m - n + 1 << endl;
//        else
//            cout << -1 << endl;
//    }   else {
//        cout << -1 << endl;
//    }
//    return 0;
//}







//void dfs(int v){
//    used[v] = true;
//    comp.push_back(v);
//    for (size_t i = 0; i < g[v].size(); ++i){
//        int to = g[v][i];
//        if (!used[to])
//            dfs(to);
//    }
//}

//int main(){
//    int n,m,a,b,ok=0;
//    cin >> n >> m;
//    ++n;
//    vector < vector <pair<int, int>> > g(n);
//    for (int i = 0; i < m; i++)
//    {
//    	int a, b, w;
//    	cin >> a >> b;
//           /*ok = 0;
//           if (g[a].size() > 0){
//               for (int j = 0; j<g[a].size(); j++)
//               if (g[a][j].first == b)
//               {
//                   g[a][j].second = min(g[a][j].second,w);
//                   ok = 1;
//               }
//               if (ok == 0)
//                   g[a].push_back(make_pair(b,w));
//           }
//           else{
//               g[a].push_back(make_pair(b, w));
//           }
//           ok = 0;
//           if (g[b].size() > 0){
//               for (int j = 0; j<g[b].size(); j++)
//               if (g[b][j].first == a)
//               {
//                   g[b][j].second = min(g[b][j].second, w);
//                   ok = 1;
//               }
//               if (ok == 0)
//                   g[b].push_back(make_pair(a,w));
//           }
//           else{
//               g[b].push_back(make_pair(a, w));
//           }*/
//          /* g[a].push_back(make_pair(b, w));
//    	g[b].push_back(make_pair(a, w));*/
//    }
//    
//    return 0;
//}

//struct tnode{
//    tnode *left;
//    tnode *right;
//    tnode *parent;
//    int n_elements_under;
//    int data;
//    int index;
//};
//
//struct tnode *talloc(void){
//    return (struct tnode*) malloc(sizeof(struct tnode));
//}
//int sum = 0;
//void rec_to_right(struct tnode *p){
//    if (p->right != NULL){
//        p->right->index++;
//        sum++;
//        rec_to_right(p->right);
//    }
//    return ;
//}
//struct tnode *addtree(struct tnode *p, int data, struct tnode *parent){
//    if (p == NULL){
//        p = talloc();
//        p->data = data;
//        p->index = 0;
//        p->left = p->right = NULL;
//        p->parent = parent;
//        p->n_elements_under = 0;
//    }
//    else if (data < p->data){
//        p->index++;
//        /*p->n_elements_under++;*/
//        sum++;
//        p->left = addtree(p->left, data,p);
//        //if (p->left->parent->right != NULL)
//        //{
//        //    sum += p->left->parent->n_elements_under;
//        //    //rec_to_right(p->left->parent);
//        //}
//        /*if (p->left->parent != NULL){
//            if (p->left->parent->right != NULL){
//                p->left->parent->right->index++;
//            }
//        }*/
//    }
//    else if (data > p->data){
//        p->n_elements_under++;
//        p->right = addtree(p->right, data,p);
//    }
//    return p;
//}
//
//void sum_index_tree(struct tnode *p){
//    if (p != NULL){
//        sum_index_tree(p->left);
//        sum+= p->index;
//        sum_index_tree(p->right);
//    }
//}
//
//int main(){
//    int n,a;
//    vector<int> v;
//    for (int i = 0; i< 3; i++){
//        struct tnode *root;
//        root = NULL;     
//        cin >> n;
//        //n = 10e6;
//        sum =0;
//        ////for (int i = 0; i < n; i++){
//        ////    /*cin >> a;*/
//        ////    a = rand() % 100 +1;
//        ////    v.push_back(a);
//        ////    root = addtree(root, a, NULL);
//        ////}
//        for (int i = 0; i < n; i++){
//            cin >> a;
//            root = addtree(root, a, NULL);
//        }
//        ////for (int i = 0; i<n; i++)
//        ////    cout << v[i] << " ";
//        ////v.clear();
//        //sum_index_tree(root);
//        cout << endl;
//        cout << sum << endl << endl;
//    }
//    return 0;
//}

//int main(){
//    int x, temp;
//    vector<int> v,vcopy,vpermitions;
//    cin >> x;
//    int tempx = x;
//    while (tempx != 0){
//        v.push_back(tempx%10);
//        tempx /= 10;
//    }
//    int number[7];
//    vcopy = v;
//    for (int a = 0; a <= 9 && v.size() >0; a++){
//        vcopy = v;
//        if (find(vcopy.begin(), vcopy.end(), a) != vcopy.end()){
//            number[0] = a;
//            vcopy.erase(find(vcopy.begin(), vcopy.end(), a));
//        }
//        else {
//            continue;
//        }
//        for (int b = 0; b <= 9 && v.size() >1; b++){
//            vcopy = v;
//            vcopy.erase(find(vcopy.begin(), vcopy.end(), a));
//            if (find(vcopy.begin(), vcopy.end(), b) != vcopy.end()){
//                number[1] = b;
//                vcopy.erase(find(vcopy.begin(), vcopy.end(), b));
//            }
//            else {
//                continue;
//            }
//            for (int c = 0; c <= 9 && v.size() >2; c++){
//                vcopy = v;
//                vcopy.erase(find(vcopy.begin(), vcopy.end(), a));
//                vcopy.erase(find(vcopy.begin(), vcopy.end(), b));
//                if (find(vcopy.begin(), vcopy.end(), c) != vcopy.end()){
//                    number[2] = c;
//                    vcopy.erase(find(vcopy.begin(), vcopy.end(), c));
//                    
//                }
//                else {
//                    continue;
//                }
//                for (int d = 0; d <= 9 && v.size() >3; d++){
//                    vcopy = v;
//                    vcopy.erase(find(vcopy.begin(), vcopy.end(), a));
//                    vcopy.erase(find(vcopy.begin(), vcopy.end(), b));
//                    vcopy.erase(find(vcopy.begin(), vcopy.end(), c));
//                    if (find(vcopy.begin(), vcopy.end(), d) != vcopy.end()){
//                        number[3] = d;
//                        vcopy.erase(find(vcopy.begin(), vcopy.end(), d));
//                    }
//                    else {
//                        continue;
//                    }
//                    for (int e = 0; e <= 9 && v.size() >4; e++){
//                        vcopy = v;
//                        vcopy.erase(find(vcopy.begin(), vcopy.end(), a));
//                        vcopy.erase(find(vcopy.begin(), vcopy.end(), b));
//                        vcopy.erase(find(vcopy.begin(), vcopy.end(), c));
//                        vcopy.erase(find(vcopy.begin(), vcopy.end(), d));
//                        if (find(vcopy.begin(), vcopy.end(), e) != vcopy.end()){
//                            number[4] = e;
//                            vcopy.erase(find(vcopy.begin(), vcopy.end(), e));
//                        }
//                        else {
//                            continue;
//                        }
//                        for (int f = 0; f <= 9 && v.size() >5; f++){
//                            vcopy = v;
//                            vcopy.erase(find(vcopy.begin(), vcopy.end(), a));
//                            vcopy.erase(find(vcopy.begin(), vcopy.end(), b));
//                            vcopy.erase(find(vcopy.begin(), vcopy.end(), c));
//                            vcopy.erase(find(vcopy.begin(), vcopy.end(), d));
//                            vcopy.erase(find(vcopy.begin(), vcopy.end(), e));
//                            if (find(vcopy.begin(), vcopy.end(), f) != vcopy.end()){
//                                number[5] = f;
//                                vcopy.erase(find(vcopy.begin(), vcopy.end(), f));
//                            }
//                            else {
//                                continue;
//                            }
//                        }
//                        if (v.size() == 6){
//                            temp = number[0] * 100000 + number[1] * 10000 + number[2] * 1000 + number[3] * 100 + number[4]*10+number[5];
//                            //cout << temp << endl;
//                            if (temp >x)
//                            vpermitions.push_back(temp);
//                        }
//                    }
//                    if (v.size() == 5){
//                        temp = number[0] * 10000 + number[1] * 1000 + number[2] * 100 + number[3]*10 + number[4];
//                        //cout << temp << endl; 
//                        if (temp >x)
//                        vpermitions.push_back(temp);
//                    }
//                }
//                if (v.size() == 4){
//                temp = number[0] * 1000 + number[1] * 100 + number[2] * 10 + number[3];
//                //cout << temp << endl;
//                if (temp >x)
//                vpermitions.push_back(temp);
//                }
//            }
//            if (v.size()==3){
//                temp = number[0] * 100 + number[1] * 10 + number[2];
//                //cout << temp << endl;
//                if (temp >x)
//                vpermitions.push_back(temp);
//            }
//        }
//        if (v.size() == 2){
//            temp = number[0] * 10 + number[1];
//            //cout << temp << endl;
//            if (temp >x)
//            vpermitions.push_back(temp);
//        }
//    }
//    sort(vpermitions.begin(), vpermitions.end());
//    if (vpermitions.size()>=1)
//    cout << vpermitions[0] << endl;
//    else
//    cout << -1 << endl;
//    return 0;
//}


//
////a structure to represent a weighted edge in graph
//struct Edge
//{
//    int src, dest, weight;
//};
//
//// a structure to represent a connected, undirected and weighted graph
//struct Graph
//{
//    // V-> Number of vertices, E-> Number of edges
//    int V, E;
//
//    // graph is represented as an array of edges. Since the graph is
//    // undirected, the edge from src to dest is also edge from dest
//    // to src. Both are counted as 1 edge here.
//    struct Edge* edge;
//};
//
//// Creates a graph with V vertices and E edges
//struct Graph* createGraph(int V, int E)
//{
//    struct Graph* graph = (struct Graph*) malloc(sizeof(struct Graph));
//    graph->V = V;
//    graph->E = E;
//
//    graph->edge = (struct Edge*) malloc(graph->E * sizeof(struct Edge));
//
//    return graph;
//}
//
//// A structure to represent a subset for union-find
//struct subset
//{
//    int parent;
//    int rank;
//};
//
//// A utility function to find set of an element i
//// (uses path compression technique)
//int find(struct subset subsets[], int i)
//{
//    // find root and make root as parent of i (path compression)
//    if (subsets[i].parent != i)
//        subsets[i].parent = find(subsets, subsets[i].parent);
//
//    return subsets[i].parent;
//}
//
//// A function that does union of two sets of x and y
//// (uses union by rank)
//void Union(struct subset subsets[], int x, int y)
//{
//    int xroot = find(subsets, x);
//    int yroot = find(subsets, y);
//
//    // Attach smaller rank tree under root of high rank tree
//    // (Union by Rank)
//    if (subsets[xroot].rank < subsets[yroot].rank)
//        subsets[xroot].parent = yroot;
//    else if (subsets[xroot].rank > subsets[yroot].rank)
//        subsets[yroot].parent = xroot;
//
//    // If ranks are same, then make one as root and increment
//    // its rank by one
//    else
//    {
//        subsets[yroot].parent = xroot;
//        subsets[xroot].rank++;
//    }
//}
//
//// Compare two edges according to their weights.
//// Used in qsort() for sorting an array of edges
//int myComp(const void* a, const void* b)
//{
//    struct Edge* a1 = (struct Edge*)a;
//    struct Edge* b1 = (struct Edge*)b;
//    return a1->weight > b1->weight;
//}
//
//void KruskalMST(struct Graph* graph)
//{
//    int V = graph->V;
//    struct Edge result[10010];  // Tnis will store the resultant MST
//    int e = 0;  // An index variable, used for result[]
//    int i = 0;  // An index variable, used for sorted edges
//
//    // Step 1:  Sort all the edges in non-decreasing order of their weight
//    // If we are not allowed to change the given graph, we can create a copy of
//    // array of edges
//    qsort(graph->edge, graph->E, sizeof(graph->edge[0]), myComp);
//
//    // Allocate memory for creating V ssubsets
//    struct subset *subsets =
//        (struct subset*) malloc(V * sizeof(struct subset));
//
//    // Create V subsets with single elements
//    for (int v = 0; v < V; ++v)
//    {
//        subsets[v].parent = v;
//        subsets[v].rank = 0;
//    }
//
//    // Number of edges to be taken is equal to V-1
//    while (e < V - 1)
//    {
//        // Step 2: Pick the smallest edge. And increment the index
//        // for next iteration
//        struct Edge next_edge = graph->edge[i++];
//
//        int x = find(subsets, next_edge.src);
//        int y = find(subsets, next_edge.dest);
//
//        // If including this edge does't cause cycle, include it
//        // in result and increment the index of result for next edge
//        if (x != y)
//        {
//            result[e++] = next_edge;
//            Union(subsets, x, y);
//        }
//        // Else discard the next_edge
//    }
//
//    // print the contents of result[] to display the built MST
//    /*printf("Following are the edges in the constructed MST\n");
//    for (i = 0; i < e; ++i)
//        printf("%d -- %d == %d\n", result[i].src, result[i].dest,
//        result[i].weight);*/
//    if (graph->E != e)
//        cout << graph->E - e << endl;
//    else
//        cout << -1 << endl;
//    return;
//}





//int ncomp = 0;
//vector <int> g[10010];
//bool used[10010];
//vector<int> comp;
//void dfs(int v){
//    used[v] = true;
//    comp.push_back(v);
//    for (size_t i = 0; i < g[v].size(); ++i){
//        int to = g[v][i];
//        if (!used[to])
//            dfs(to);
//    }
//}
//
//
//void find_comps(int n){
//    for (int i = 1; i<n; ++i)
//        used[i] = false;
//    for (int i = 1; i<n; ++i)
//    if (!used[i]){
//        comp.clear();
//        dfs(i);
//        if (comp.size() > 0)
//            ncomp++;
//    }
//}
//int main(){
//    int n, m;
//    cin >> n >> m;
//    n++;
//
//    for (int i = 0; i < m; i++)
//    {
//        int a, b, w;
//        cin >> a >> b;
//
//        g[a].push_back(b);
//        g[b].push_back(a);
//    }
//    find_comps(n);
//    cout << ncomp - 1 << endl;
//    return 0;
//}

//int main(){
//    int E,V,a,b;
//    cin >> V >> E;
//    struct Graph* graph = createGraph(V, E);
//    for (int i = 0; i < E; i++){
//        cin >> a >> b;
//        graph->edge[i].src = a-1;
//        graph->edge[i].dest = b-1;
//        graph->edge[i].weight = 0;
//    }
//    KruskalMST(graph);
//    return 0;
//}


//int main(){
//    int n,m,x1,y1,x2,y2;
//    cin >> n >> m >> x1 >> y1 >> x2 >> y2;
//    if (abs(x1 - x2) == abs(y1 - y2)){
//        cout << "NO" << endl;
//    }
//    else {
//        cout << "YES" << endl;
//    }
//    return 0;
//}
//int main(){
//
//    string s;
//    cin >> s;
//    int i = 0, j = s.length() - 1, pal = 0;
//    set<char> setchar;
//    while (s[i] == s[j] && i != (s.length() / 2) + 1)
//    {
//        setchar.insert(s[i]);
//        if (i == (s.length() / 2)){
//            pal = 1;
//            break;
//        }
//        i++;
//        j--;
//    }
//    if (!pal)
//        cout << s.length() << endl;
//    else if (pal && setchar.size() == 1){
//        cout << -1 << endl;
//    }
//    else {
//        cout << s.length() - 1 << endl;
//    }
//}
    /*int f=0,sec=0;
    for (int i = s.length()-1; i >=0; i--){
        if (s[0] == s[i])
            f++;
        else 
            break;
    }
    for (int j = 0; j < s.length(); j++){
        if (s[s.length()-1] == s[j])
            sec++;
        else 
            break;
    }
    f = s.length() - f;
    sec = s.length() - sec;
    int ans = max(f,sec);
    if (ans == 0){
        cout << -1 << endl;
    }
    else {
        cout << ans << endl;
    }*/
    //long long x;
    //vector<int> v,vpos;
    //int a[10] ={0};
    //set<int> s;
    //cin >> x;
    //int tempx = x;
    //int i =0;
    //while (x != 0){
    //    int rem = x%10;
    //    v.push_back(rem);
    //    a[i++] = rem;
    //    x /=10;
    //}
    ///*for (int i = 0; i< v.size(); i++)
    //    s.insert(v[i]);*/
    //int num=0;
    //generate(v.size(), v.size(), a);
    
    
    /*for (int i = 0; i < vpos.size(); i++)
    {
        cout << vpos[i] << endl;
    }*/

//int main()
//{
//    long long x;
//    cin >> x;
//    if (x % 10 != 0 || x <10){
//        cout << x % 10 << endl;
//    }
//    else {
//        cout << "NO" << endl;
//    }
//    return 0;
//}
//void dfs(int v) {
//	used[v] = true;
//		for (vector<int>::iterator i = gtemp[v].begin(); i != gtemp[v].end(); ++i)
//			if (!used[*i])
//		dfs(*i);
//}
//int main(){
//    int x,raz,i,min,j,n,k;
//    bool flag;
//    vector<int> v;
//    cin >> x;
//    int temp =x;   
//    while (temp != 0){
//        v.push_back(temp%10);
//        temp /=10;
//    }
//    vector<int> obr(v.size());
//    int num ;
//    while (1){
//        flag = false;
//        for (i = v.size() - 2; i >= 0; i--){
//            if (v[i] < v[i + 1]){
//                flag = true;
//                break;
//            }
//        }
//        if (flag == false){
//            break;
//        }
//        raz = v[i+1];
//        n = v.size();
//        for (j = i + 1; j < n; j++){
//            if (((v[j] - v[i]) < raz) && (v[i] < v[j])){
//                min = j;
//            }
//        }
//        int tmp = v[i];
//        v[i] = v[min];
//        v[min] = tmp;
//        for (j = i + 1; j < n; j++){
//            obr[j] = v[j];
//        }
//        j = i +1;
//        for (k = n - 1; k >= i + 1; k--){
//            v[j] = obr[k];
//            j++;
//        }
//    }
//}


//20C Usual Dijkstra 
//const long long INF = 1000000000000;
//int main(){
//	int n,m,a,b,ok=0;
//	cin >> n >> m;
//	++n;
//	vector < vector <pair<int, int>> > g(n);
//	for (int i = 0; i < m; i++)
//	{
//		int a, b, w;
//		cin >> a >> b >> w;
//        ok = 0;
//        if (g[a].size() > 0){
//            for (int j = 0; j<g[a].size(); j++)
//            if (g[a][j].first == b)
//            {
//                g[a][j].second = min(g[a][j].second,w);
//                ok = 1;
//            }
//            if (ok == 0)
//                g[a].push_back(make_pair(b,w));
//        }
//        else{
//            g[a].push_back(make_pair(b, w));
//        }
//        ok = 0;
//        if (g[b].size() > 0){
//            for (int j = 0; j<g[b].size(); j++)
//            if (g[b][j].first == a)
//            {
//                g[b][j].second = min(g[b][j].second, w);
//                ok = 1;
//            }
//            if (ok == 0)
//                g[b].push_back(make_pair(a,w));
//        }
//        else{
//            g[b].push_back(make_pair(a, w));
//        }
//       /* g[a].push_back(make_pair(b, w));
//		g[b].push_back(make_pair(a, w));*/
//	}
//    cin >> a >> b;
//	int s = a;//1
//
//	vector<long long> d(n, INF), p(n);
//	d[s] = 0;
//	vector<char> u(n);
//	for (int i = 0; i < n; i++)
//	{
//		int v = -1;
//		for (int j = 0; j < n; ++j)//b
//		if (!u[j] && (v == -1 || d[j] < d[v]))
//			v = j;
//		if (d[v] == INF)
//			break;
//		u[v] = true;
//
//		for (size_t j = 0; j < g[v].size(); ++j)
//		{
//			int to = g[v][j].first,
//				len = g[v][j].second;
//			if (d[v] + len < d[to]){
//				d[to] = d[v] + len;
//				p[to] = v;
//			}
//		}
//	}
//	vector<int> path;
//    cout << d[b] << endl;
//	
//	return 0;
//}

    /*int n,k,v1,v2;
    cin >> n;
    for (int i = 0; i < n-1; i++){
        cin >> v1 >> v2;
        g[v1].push_back(v2);
    }
    mt.assign(n+1,-1);
    for (int v = 0; v < n; ++v){
        used.assign(n,false);
        try_kuhn(v);
    }
    for (int i = 0; i<n; ++i)
    if (mt[i] != -1)
        printf("%d %d\n", mt[i]+1, i+1);
    return 0;
}*/
    /*int n, a, maxi, maxj,ok=0;
    cin >> n;
    cin >> maxi;
    cin >> maxj;
    for (int i = 0; i < n-2; i++){
        cin >> a;
        if (ok == 0){
            maxi = max(maxi,a);
            ok = 1;
        }
        else if (ok == 1){
            maxj = max(maxj,a);
            ok = 0;
        }
    }
    cout << maxi * maxj << endl;
    return 0;
}*/
    /*int n, p;
    double sum_apples=1,sum=0,plus=0;
    int half=0;
    vector<string> v;
    cin >> n >> p;
    for (int i = 0; i < n; i++){
        string s;
        cin >> s;
        v.push_back(s);
        if (s == "halfplus")
            plus++;
        if (s == "half")
            half++;
    }
    
    for (int i = n-1; i >=0; i--){
        if (v[i] == "halfplus"){
            if (i == n - 1)
            {
                sum_apples = 1;
            }
            else {
                sum = 2*sum_apples+0.5;
                if (sum - (ll)sum == 0.5)
                    sum += 0.5;
                sum_apples = sum;
            }
        }
        else if (v[i] == "half"){
            sum = 2*sum_apples;
            sum_apples = sum;
        }
    }
   
    sum -= plus*0.5;
    sum = sum*p;
    
    cout << (ll)sum << endl;*/

    /*double n,m,ans=0,sum_m=0;
    vector<int> v[11];
    cin >> n >> m;
    for (int i = 1; i <= n; i++){
        int a; 
        cin >> a;
        v[a].push_back(i);
    }
    ans = n*(n-1)/2;
    for (int i = 1; i <= m; i++){
        sum_m += v[i].size()*(v[i].size()-1)/2;
    }
    cout << (ll)(ans-sum_m) << endl;
    return 0;
    }*/

//
//
//int gcd(int a, int b) {
//    if (b == 0)
//        return a;
//    else
//        return gcd(b, a % b);
//}
//
//
//ll get_hash(string line){
//    const int p = 31;
//    ll hash = 0, p_pow = 1;
//    for (int i = 0; i < line.length(); i++){
//        hash += (line[i] - 'a' + 1)*p_pow;
//        p_pow *= p;
//    }
//    return hash;
//}
//
//
//bool RabinKarp(string line, string subline){
//
//    return 0;
//}

    /*int n,m;
    string line,reversed_line;
    vector<string> v_pattern, v_pattern_lower;
    vector<ll>hashes;
    ll hsub;
    cin >> n >> line >> m;
    reversed_line = string(line.rbegin(),line.rend());
    
    for (int i = 0; i < m; i++){
        string in_line;
        cin >> in_line;
        v_pattern.push_back(in_line);
    
        for (int i = 0; i < in_line.length(); i++){
            in_line[i] = tolower(in_line[i]);
        }
        v_pattern_lower.push_back(in_line);
    }
    for (int i = 0; i < m; i++){
        hsub = get_hash(v_pattern_lower[i]);
        hashes.push_back(hsub);
        
    }
    ll hline = get_hash(line);
    for (int i = 0; i < m; i++){
        if (RabinKarp(reversed_line, v_pattern_lower[i])){
            cout << v_pattern[i] << ' ';
        }
    }
    
 }*/
    


    /*int m,pow=0;
    cin >> m;
    vector<int> v;
              
    for (int i = 1,j=1,z=5; i <= 600000; i++,j++,z+=5)    {
        if (j == 5)        {
            int d = 0;
            int temp = z;
            while (temp % 5 == 0){
                temp /= 5;
                d++;
            }
            int temp_i = i;
            for (int j = 1; j <= d-1; j++){
                v.push_back(temp_i);
                temp_i++;
            }
            i +=d-1;
            j = 0;
        }
    }
    for (int i = 0; i < v.size(); i++)    {
        if (v[i] == m)        {
            cout << 0 ;
            return 0;
        }
        if (v[i] < m){
            pow++;
        }
    }
    int temp = 5;
    for (int i = 1; i <= m; i++)    {
       temp += 5;
    }
    temp -= 5*pow;
    cout << 5 << endl;
    for (int i = temp-5; i < temp; i++)
        cout << i << ' ';
    return 0;
}*/

    /*int a,b,c;

    cin >> a >> b >> c;
   
    if ((c % gcd(a, b)) == 0){
        
        for (int i = 0; i <= 10000; i++){
            for (int j = 0; j <= 10000; j++){
                if (a*i+b*j == c){
                    cout << "Yes" << endl;
                    return 0;
                }
            }
        }
    }
    cout << "No" << endl;
    return 0;*/


//
//template<class T>
//void mergeSort(T a[], long lb, long ub){
//    long split;
//
//    if (lb < ub) {
//        split = (lb + ub) / 2;
//
//        mergeSort(a, lb, split);
//        mergeSort(a, split + 1, ub);
//        merge(a, lb, split, ub);
//    }
//}
//
//template<class T>
//void merge(T a[], long lb, long split, long ub){
//    long pos1 = lb;
//    long pos2 = split + 1;
//    long pos3 = 0;
//
//    T *temp = new T[ub - lb + 1];
//
//    while (pos1 <= split && pos2 <= ub){
//        if (a[pos1] < a[pos2])
//            temp[pos3++] = a[pos1++];
//        else
//            temp[pos3++] = a[pos2++];
//    }
//
//    while (pos2 <= ub)
//        temp[pos3++] = a[pos2++];
//    while (pos1 <= split)
//        temp[pos3++] = a[pos1++];
//
//    for (pos3 = 0; pos3 < ub - lb + 1; pos3++)
//        a[lb + pos3] = temp[pos3];
//
//
//}

    /*int a[8] = { 3, 7, 8, 2, 4, 6, 1, 5 };
    
    mergeSort(a, 0, 8);*/
    
   /* int nflash=0,mfile,x=0;
    cin >> nflash >> mfile;
    vector<int> v;
    for (int i = 0; i < nflash; i++){
        int t;
        cin >> t;
        v.push_back(t);
    }
    
    sort(v.begin(), v.end());
    reverse(v.begin(), v.end());
    int i = 0;
    while (x < mfile ){
        x += v[i];
        i++;
    }
    cout << i << endl;
	return 0;*/


