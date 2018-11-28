#include<iostream>
#include<algorithm>

using namespace std;

#define display()   for(int it = 0; it < n; it++)   cout << arr[it].idx << "->" << arr[it].val << endl;

struct node{
    int val;
    char idx;
};

bool comp(node a, node b){
    return a.val >= b.val;
}

int main(){
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    for(int itrS = 0; itrS < t; itrS++){
        int n, cnt = 0;
        cin >> n;
        node arr[n];
        for(int i = 0; i < n; i++){
            cin >> arr[i].val;
            cnt += arr[i].val;
            arr[i].idx = 'A' + i;
        }
        sort(arr, arr + n, comp);
        cout << "Case #" << itrS + 1 << ": ";
        while(cnt){
            if(arr[1].val <= (cnt - 1) / 2){
                cout << arr[0].idx << " ";
                arr[0].val--;
                cnt--;
            }
            else{
                cout << arr[0].idx << arr[1].idx << " ";
                arr[0].val--;
                arr[1].val--;
                cnt -= 2;
            }
            sort(arr, arr + n, comp);
        }
        cout << endl;
    }
    return 0;
}
