#include<iostream>
#include<math.h>
#include<stack>
#include<queue>

using namespace std;

bool palindrome (long long n) {
    if (n < 10) return true;
    stack<int> stack;
    queue<int> queue;
    while (n > 0) {
        stack.push(n%10);
        queue.push(n%10);
        n /= 10;     
    }       
    while (!stack.empty()) {
        if (stack.top() != queue.front())
            return false;      
        stack.pop();    
        queue.pop();
    }
    return true; 
}

int main () {
    int T; cin >> T;
    for (int step=1; step<=T; step++) {
        long long A, B; cin >> A >> B;
        int result = 0;
        long long rootA = (long long)sqrt(A), rootB = (long long)sqrt(B);
        if (rootA*rootA < A) rootA++;
        for (long long i=rootA; i<=rootB; i++) {
            if (palindrome(i) && palindrome(i*i)) 
                result++; 
        }
        cout << "Case #" << step << ": " << result << endl;   
    }        
    return 0;
}
