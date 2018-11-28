#include <iostream>
#include <string>
#include <queue>
using namespace std;

void printResult(int caseNum, int result){
    cout<<"Case #"<<caseNum<<": "<<result<<endl;
}

int a[1010];

int foo(priority_queue<int> pque){
    if (pque.empty()) {
        return 0;
    }
    int top = pque.top();
    if (top <= 3) {
        return top;
    }
    
    priority_queue<int> ppque = pque;
    priority_queue<int> tque;
    while (!ppque.empty()) {
        int tmp = ppque.top();
        ppque.pop();
        -- tmp;
        if (tmp > 0) {
            tque.push(tmp);
        }
    }
    int result2 = foo(tque) + 1;
    
    pque.pop();
    pque.push(top / a[top]);
    pque.push(top - (top/a[top]));
    int result1 = foo(pque) + 1;
//    cout<<"top = "<<top<<"\t"<<"result1 = "<<result1<<"\tresult2 = "<<result2<<endl;
    return result1 < result2 ? result1 : result2;
}

int main(int argc, const char * argv[])
{
    for (int i = 1; i < 1010; ++ i) {
        if (i <= 3) {
            a[i] = 1;
        } else {
            int minCost = 1010;
            int j;
            for (j = 2; j <= i; ++ j) {
                int cost = j - 1;
                if (i % j != 0) {
                    cost += 1;
                }
                cost += i / j;
                if (cost < minCost) {
                    minCost = cost;
                } else {
                    break;
                }
            }
            a[i] = j - 1;
        }
    }
    int T;cin>>T;
    for (int kk = 1; kk <= T; ++ kk) {
        priority_queue<int> pque;
        
        int d;cin>>d;
        for (int i = 0; i < d; ++ i) {
            int tmp;cin>>tmp;
            pque.push(tmp);
        }
        
        printResult(kk, foo(pque));
    }
}

