//
//  pa.cpp
//  
//
//  Created by 宋元堯 on 2016/5/8.
//
//

#include <iostream>
#include <queue>

using namespace std;

struct Party {
    char name;
    int people;
    Party(char c, int n){
        name = c;
        people = n;
    }
    Party(){}
};

bool operator<(const Party& lhs, const Party& rhs)
{
    return lhs.people < rhs.people;
}

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    int T, testcase = 1;
    cin >> T;
    while(T--){
        cout << "Case #" << testcase++ << ":";
        int N;
        cin >> N;
        int people[N], sum = 0;
        priority_queue<Party> pq;
        for(int i = 0; i < N; ++i){
            int n;
            cin >> n;
            people[i] = n;
            sum += n;
        }
        if(sum % 2 == 1){
            int mx_idx = max_element(people, people + N) - people;
            cout << ' ' << (char)('A' + mx_idx);
            people[mx_idx]--;
        }
        for(int i = 0; i < N; ++i){
            if(people[i]) pq.push(Party('A' + i, people[i]));
        }
        while(!pq.empty()){
            Party now = pq.top();
            pq.pop();
            cout << ' ' << now.name;
            now.people--;
            if(now.people) pq.push(now);
            now = pq.top();
            pq.pop();
            cout << now.name;
            now.people--;
            if(now.people) pq.push(now);
        }
        cout << endl;
    }
    return 0;
}
