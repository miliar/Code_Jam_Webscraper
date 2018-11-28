/*#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

multiset<int> :: iterator it;
multiset<int> que;

int main()
{
    int n;
    cin >> n;
    while(n--){
        int k;
        cin >> k;
        que.insert(k);
        it = que.find(k);
        if(que.size() > 1){
            if(it != que.end()){
                it++;
                cout << *it << "----";
                it--;
                cout << *it << endl;
            }
        }
    }
    it = que.begin();
    while(it != que.end()){
        cout << *it << endl;
        it++;
    }
    return 0;
}
*/
/*
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <stack>
#include <cstring>

using namespace std;

stack<int> st;
multiset<int> tab;
multiset<int> :: iterator it;
char mod[3][20] = {"Push","Pop","PeekMedian"};

int main()
{
    int n, k;
    char s[20];
    scanf("%d", &n);
    while(n--){
        scanf("%s",s);
        if(strcmp(s, mod[0]) == 0){
            scanf("%d", &k);
            st.push(k);
            tab.insert(k);
            if(tab.size() == 1)it = tab.begin();
            else if(tab.size() % 2){
                if(k <= )
            }
        }
        else if(strcmp(s, mod[1]) == 0){

        }
        else {

        }
    }
    return 0;
}*/

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int tab[5] = {1, 4, 9, 121, 484};
int ans[1001];

void init()
{
    ans[0] = 0, ans[1] = 1;
    for(int i = 2, j = 1; i <= 1000; i++){
        if(i == tab[j]){
            //cout <<  i <<  endl;
            ans[i] = ans[i - 1] + 1;
            j++;
        }
        else ans[i] = ans[i - 1];
    }
    //cout << ans[1000] << endl;
}

int main()
{
    freopen("C-small-attempt2.in","r",stdin);
    freopen("C-small-attempt2.out","w",stdout);

    init();
    int t, a, b;
    scanf("%d",&t);
    //printf("%d\n", t);
    for(int ca = 1; ca <= t; ca++){
        scanf("%d%d", &a, &b);
        //cout << ans[b] << ' ' << ans[a] << endl;
        printf("Case #%d: %d\n", ca, ans[b] - ans[a - 1]);
        //printf("Case #%d: %d %d\n", ca, a, b);
    }
    return 0;
}
